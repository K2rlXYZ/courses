package com.myllerbeck.puzzle15

import android.app.Service
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.IBinder
import android.util.Log
import androidx.localbroadcastmanager.content.LocalBroadcastManager
import java.util.Timer
import kotlin.concurrent.timerTask

class BgrService : Service() {
    companion object {
        private val TAG = this::class.java.declaringClass!!.simpleName
    }

    private val broadcastReceiverInService = BroadcastReceiverInService()
    private val intentFilter = IntentFilter()

    private var running = false

    private var taskTimer = Timer()
    private var elapsedSeconds: Int = 0

    private inner class BroadcastReceiverInService : BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            when (intent?.action) {
                C.ACTION_SERVICE_PAUSE -> {
                    Log.d(TAG, "BgrService ACTION_SERVICE_PAUSE")
                    taskTimer.cancel()
                    running = false
                }

                C.ACTION_SERVICE_RESUME -> {
                    Log.d(TAG, "BgrService ACTION_SERVICE_RESUME")
                    startTimerService()
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

    override fun onCreate() {
        super.onCreate()

        intentFilter.addAction(C.ACTION_SERVICE_PAUSE)
        intentFilter.addAction(C.ACTION_SERVICE_RESUME)

        LocalBroadcastManager.getInstance(this)
            .registerReceiver(broadcastReceiverInService, intentFilter)

        Log.d(TAG, "BgrService onCreate")
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        Log.d(TAG, "BgrService onStartCommand")

        LocalBroadcastManager.getInstance(this).sendBroadcast(Intent(C.ACTION_SERVICE_START))

        startTimerService()

        return START_STICKY
    }

    private fun startTimerService() {
        if (!running) {
            running = true
            taskTimer = Timer()
            taskTimer.scheduleAtFixedRate(
                timerTask
                {
                    Log.d(TAG, "scheduledExecutorService running")
                    val intent = Intent(C.ACTION_TIME)
                    elapsedSeconds++
                    intent.putExtra(C.PAYLOAD_TIME, elapsedSeconds)
                    LocalBroadcastManager.getInstance(applicationContext).sendBroadcast(intent)
                },
                0, // initialDelay
                1000 // period(ms)
            )
        } else {
            Log.d(TAG, "taskTimer already running")
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        taskTimer.cancel()
        running = false
        LocalBroadcastManager.getInstance(this).unregisterReceiver(broadcastReceiverInService)

        Log.d(TAG, "BgrService onDestroy")
    }

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }
}