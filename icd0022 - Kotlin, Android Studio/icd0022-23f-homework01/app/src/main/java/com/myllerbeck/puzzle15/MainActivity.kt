package com.myllerbeck.puzzle15

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.content.res.Configuration
import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.app.AppCompatDelegate
import androidx.core.view.children
import androidx.localbroadcastmanager.content.LocalBroadcastManager
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
    companion object {
        private val TAG = this::class.java.declaringClass!!.simpleName
    }

    private lateinit var state: State

    private val broadcastReceiverInMainActivity = BroadcastReceiverInMainActivity()
    private val intentFilter = IntentFilter()

    private inner class BroadcastReceiverInMainActivity : BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            when (intent?.action) {
                C.ACTION_TIME -> {
                    setTimerTextViewFromSeconds(intent.getIntExtra(C.PAYLOAD_TIME, 0))
                }

                else -> {
                    Log.e(
                        "BroadcastReceiverInMainActivity",
                        "Unknown action ${intent?.action ?: "action null"}"
                    )
                }
            }
            Log.d("BroadcastReceiverInMainActivity", intent?.action ?: "action null")
        }

    }

    private fun setTimerTextViewFromSeconds(time: Int) {
        val seconds = time % 60
        val totalMinutes = time / 60
        val minutes = totalMinutes % 60
        val hours = totalMinutes / 60
        var timeString = ""
        if (hours > 0) {
            timeString += hours.toString() + "h "
        }
        if (minutes > 0) {
            timeString += minutes.toString() + "m "
        }
        if (seconds > 0) {
            timeString += seconds.toString() + "s"
        }

        var timerTextString = getString(R.string.time_spent)
        timerTextString = timerTextString.split(":")[0]
        timerTextString += ": $timeString"
        findViewById<TextView>(R.id.timeSpentTextView).text = timerTextString
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        intentFilter.addAction(C.ACTION_TIME)
        intentFilter.addAction(C.ACTION_SERVICE_START)
        intentFilter.addAction(C.ACTION_SERVICE_DESTROY)
        intentFilter.addAction(C.ACTION_SERVICE_PAUSE)
        intentFilter.addAction(C.ACTION_SERVICE_RESUME)

        state = State()

        setBoardLayouts()
        shuffleSolvable()

        val serviceIntent = Intent(applicationContext, BgrService::class.java)
        startService(serviceIntent)
    }

    private fun setBoardLayouts() {
        if (resources.configuration.orientation == Configuration.ORIENTATION_PORTRAIT) {
            state.gameBoardLayout = findViewById(R.id.game_board)
            state.controlBoardLayout = findViewById(R.id.control_board)
        } else {
            state.gameBoardLayout = findViewById(R.id.game_board_landscape)
            state.controlBoardLayout = findViewById(R.id.control_board_landscape)
        }
    }

    private fun getButton(index: Int): Button {
        return state.gameBoardLayout.children.toList()[index] as Button
    }

    private fun getButtonIndex(button: Button): Int? {
        var index = 0
        for (button2 in state.gameBoardLayout.children) {
            if (button == button2) {
                return index
            }
            index++
        }
        return null
    }

    fun buttonOnClick(button: View) {
        if (state.selected != null) {
            tryMakeMove(button as Button)
            val tint = getColorStateList(R.color.colorButton)
            state.selected!!.backgroundTintList = tint
            state.selected = null
        } else {
            state.selected = button as Button
            val tint = getColorStateList(R.color.colorButtonSelected)
            state.selected!!.backgroundTintList = tint
        }
    }

    private fun tryMakeMove(button: Button) {
        val selectedButtonIndex = getButtonIndex(state.selected!!)!!
        val clickedButtonIndex = getButtonIndex(button)
        if ((selectedButtonIndex - 1 == clickedButtonIndex ||
                    selectedButtonIndex + 1 == clickedButtonIndex ||
                    selectedButtonIndex - 4 == clickedButtonIndex ||
                    selectedButtonIndex + 4 == clickedButtonIndex) &&
            (state.selected!!.text.toString() == getString(R.string._empty) ||
                    button.text.toString() == getString(R.string._empty))
        ) {

            val tempSTr = state.selected!!.text.toString()
            state.selected!!.text = button.text
            button.text = tempSTr

            if (state.undoableMoves.count() == state.maxNumUndo) {
                state.undoableMoves.removeFirst()
            }
            state.undoableMoves.add(arrayListOf(state.selected!!, button))

            state.moves += 1
            setMovesTextView(state.moves)
        }
    }

    private fun setMovesTextView(moves: Int) {
        var moveCountString = getString(R.string.move_count)
        moveCountString = moveCountString.split(" ")[0]
        moveCountString += (": $moves")
        findViewById<TextView>(R.id.moveCountTextView).text = moveCountString
    }

    fun undoButtonOnClick(button: View) {
        if (state.undoableMoves.isNotEmpty()) {
            val move = state.undoableMoves.last()
            state.undoableMoves.removeLast()
            val tempSTr = move[0].text.toString()
            move[0].text = move[1].text
            move[1].text = tempSTr
            state.moves -= 1
        }
    }

    private fun resetBoard() {
        val elements: ArrayList<String> = arrayListOf(
            "1", "2", "3", "4",
            "5", "6", "7", "8",
            "9", "10", "11", "12",
            "13", "14", "15", "-"
        )
        var i = 0
        for (button in state.gameBoardLayout.children) {
            button as Button
            button.text = elements[i]
            i++
        }
    }

    private fun shuffleRandomly() {
        val elements: ArrayList<String> = arrayListOf(
            "1", "2", "3", "4",
            "5", "6", "7", "8",
            "9", "10", "11", "12",
            "13", "14", "15", "-"
        )
        for (button in state.gameBoardLayout.children) {
            val randomIndex: Int = Random.nextInt(elements.size)
            button as Button
            button.text = elements[randomIndex]
            elements.removeAt(randomIndex)
        }
        state.undoableMoves.clear()
        state.moves = 0
        setMovesTextView(0)
    }

    private fun shuffleSolvable() {
        resetBoard()
        val randomMoves: Int = Random.nextInt(100) + 50
        state.selected =
            state.gameBoardLayout.children.first { b -> (b as Button).text.toString() == "-" } as Button
        var emptySquare = state.selected!!
        for (i in 0..randomMoves) {
            val index = getButtonIndex(emptySquare)
            var index2 = 0

            when (Random.nextInt(4)) {
                0 -> {
                    index2 = index?.plus(1) ?: -1
                }

                1 -> {
                    index2 = index?.minus(1) ?: -1
                }

                2 -> {
                    index2 = index?.plus(4) ?: -1
                }

                3 -> {
                    index2 = index?.minus(4) ?: -1
                }
            }
            if (index2 > 15) {
                when (Random.nextInt(2)) {
                    0 -> {
                        index2 = index?.minus(1) ?: -1
                    }

                    1 -> {
                        index2 = index?.minus(4) ?: -1
                    }
                }
            }
            if (index2 < 0) {
                when (Random.nextInt(2)) {
                    0 -> {
                        index2 = index?.plus(1) ?: -1
                    }

                    1 -> {
                        index2 = index?.plus(4) ?: -1
                    }
                }
            }

            val randomButton = getButton(index2)
            tryMakeMove(randomButton)
            state.selected = randomButton
            emptySquare = state.selected!!
        }
        state.undoableMoves.clear()
        state.selected = null
        state.moves = 0
        setMovesTextView(0)
    }

    private fun setReshuffleButtonText(newText: String) {
        findViewById<Button>(R.id.reshuffleButton).text = newText
    }

    fun reshuffleButtonOnClick(button: View?) {
        if (state.shuffleToggle) {
            shuffleRandomly()
            val newText = getString(R.string.reshuffle_board).split(":")[0] + ": solvable"
            setReshuffleButtonText(newText)
        } else {
            shuffleSolvable()
            val newText = getString(R.string.reshuffle_board).split(":")[0] + ": random"
            setReshuffleButtonText(newText)
        }
        state.shuffleToggle = !state.shuffleToggle
    }

    private fun setColorSchemaButtonText(newText: String) {
        findViewById<Button>(R.id.colorSchemaButton).text = newText
    }

    fun colorSchemaButtonOnClick(button: View?) {
        Log.d(TAG, "Changing color scheme")
        if (state.darkMode) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
            val newText = getString(R.string.color_schema).split(":")[0] + ": light"
            setColorSchemaButtonText(newText)
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
            val newText = getString(R.string.color_schema).split(":")[0] + ": dark"
            setColorSchemaButtonText(newText)
        }
        state.darkMode = !state.darkMode
    }

    override fun onRestart() {
        super.onRestart()
        Log.d(TAG, "MainActivity onRestart")
    }

    override fun onStart() {
        super.onStart()
        when (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) {
            Configuration.UI_MODE_NIGHT_NO -> {
                val newText = getString(R.string.color_schema).split(":")[0] + ": light"
                setColorSchemaButtonText(newText)
                state.darkMode = false
            }

            Configuration.UI_MODE_NIGHT_YES -> {
                val newText = getString(R.string.color_schema).split(":")[0] + ": dark"
                setColorSchemaButtonText(newText)
                state.darkMode = true
            }
        }
        Log.d(TAG, "MainActivity onStart")
    }

    override fun onResume() {
        super.onResume()

        LocalBroadcastManager.getInstance(this)
            .registerReceiver(broadcastReceiverInMainActivity, intentFilter)
        LocalBroadcastManager.getInstance(this).sendBroadcast(Intent(C.ACTION_SERVICE_RESUME))

        Log.d(TAG, "MainActivity onResume")
    }

    override fun onPause() {
        super.onPause()
        LocalBroadcastManager.getInstance(this).sendBroadcast(Intent(C.ACTION_SERVICE_PAUSE))
        LocalBroadcastManager.getInstance(this).unregisterReceiver(broadcastReceiverInMainActivity)
        Log.d(TAG, "MainActivity onPause")
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, "MainActivity onStop")
    }

    override fun onDestroy() {
        super.onDestroy()
        LocalBroadcastManager.getInstance(this).sendBroadcast(Intent(C.ACTION_SERVICE_DESTROY))
        Log.d(TAG, "MainActivity onDestroy")
    }

    override fun onSaveInstanceState(outState: Bundle, outPersistentState: PersistableBundle) {
        super.onSaveInstanceState(outState, outPersistentState)
        Log.d(
            TAG,
            "MainActivity onSaveInstanceState(outState: Bundle, outPersistentState: PersistableBundle)"
        )
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        Log.d(TAG, System.currentTimeMillis().toString())
        var index = 0
        var row: Int
        var column: Int
        for (button in state.gameBoardLayout.children) {
            row = index / 4
            column = index % 4
            outState.putString("$row,$column", (button as Button).text.toString())
            index++
        }
        for (i in state.undoableMoves.count() - 1 downTo 0) {
            val moveList = state.undoableMoves[i].map { button -> getButtonIndex(button) }
            outState.putIntegerArrayList("move$i", ArrayList(moveList))
        }
        outState.putInt("moves", state.moves)
        outState.putBoolean("dark_mode", state.darkMode)
        outState.putBoolean("shuffle_toggle", state.shuffleToggle)
        Log.d(TAG, System.currentTimeMillis().toString())
        Log.d(TAG, "MainActivity onSaveInstanceState(outState: Bundle)")
    }

    override fun onRestoreInstanceState(
        savedInstanceState: Bundle?,
        persistentState: PersistableBundle?
    ) {
        super.onRestoreInstanceState(savedInstanceState, persistentState)
        Log.d(
            TAG,
            "MainActivity onRestoreInstanceState(savedInstanceState: Bundle?, persistentState: PersistableBundle?)"
        )
    }

    override fun onRestoreInstanceState(savedInstanceState: Bundle) {
        super.onRestoreInstanceState(savedInstanceState)
        setBoardLayouts()
        Log.d(TAG, System.currentTimeMillis().toString())
        var index = 0
        var row: Int
        var column: Int
        for (button in state.gameBoardLayout.children) {
            row = index / 4
            column = index % 4
            val text = savedInstanceState.getString("$row,$column")
            (button as Button).text = text
            index++
        }
        for (i in 0..<state.maxNumUndo) {
            val move = savedInstanceState.getIntegerArrayList("move$i")
            if (move != null) {
                state.undoableMoves.add(move.map { ind -> getButton(ind) } as ArrayList<Button>)
            }
        }
        state.moves = savedInstanceState.getInt("moves")
        setMovesTextView(state.moves)
        state.darkMode = savedInstanceState.getBoolean("dark_mode")
        state.shuffleToggle = savedInstanceState.getBoolean("shuffle_toggle")

        if (state.shuffleToggle) {
            val newText = getString(R.string.reshuffle_board).split(":")[0] + ": random"
            setReshuffleButtonText(newText)
        } else {
            val newText = getString(R.string.reshuffle_board).split(":")[0] + ": solvable"
            setReshuffleButtonText(newText)
        }

        Log.d(TAG, System.currentTimeMillis().toString())
        Log.d(TAG, "MainActivity onRestoreInstanceState(savedInstanceState: Bundle)")
    }
}