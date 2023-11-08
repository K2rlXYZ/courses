package com.myllerbeck.puzzle15

import android.widget.Button
import androidx.constraintlayout.widget.ConstraintLayout


class State {
    var selected: Button? = null
    lateinit var gameBoardLayout: ConstraintLayout
    lateinit var controlBoardLayout: ConstraintLayout
    var undoableMoves: ArrayList<ArrayList<Button>> = arrayListOf()
    val maxNumUndo = 5
    var moves = 0
    var shuffleToggle = false
    var darkMode = false
}