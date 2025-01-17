# Author: XU Tianyu & WANG Xiaoke
# Edit: 2021.3.10
# FM_Final Project: EMG_MAV

# Implement the calculation of MAV (mean absolute value) for all eight channels of the EMG.
# Plot the calculated value on top of the EMG plots.

import myo
import numpy as np
import time
import keyboard
# import math

# from collections                         import deque
from myo_ecn.listeners                   import ConnectionChecker
from myo_ecn.listeners                   import Buffer
from MultichannelPlot                    import MultichannelPlot
from features                            import Feature
from cursor                              import cursor


def main():
    # ================== setup myo-python (do not change) =====================
    myo.init(sdk_path='../../myo_sdk') # Compile Python binding to Myo's API
    hub = myo.Hub() # Create a Python instance of MYO API
    if not ConnectionChecker().ok: # Check connection before starting acquisition:
        quit()
    # =========================================================================
    # calculate the Mean Absolute Value
    # Setup our custom processor of MYO's events.
    # EmgBuffer will acquire new data in a buffer (queue):
    listener = Buffer(buffer_len = 512) # At sampling rate of 200Hz, 512 samples correspond to ~2.5 seconds of the most recent data.
    calculate = Feature(input_len = 512)
    # Setup multichannel plotter for visualisation:
    plotter = MultichannelPlot(nchan = 8, xlen = 512) # Number of EMG channels in MYO armband is 8 , window size is 15 for MAV
    freq = 200
    move = cursor(freq)


    # Tell MYO API to start a parallel thread that will collect the data and
    # command the MYO to start sending EMG data.
    with hub.run_in_background(listener): # This is the way to associate our listener with the MYO API.
        print('Streaming EMG ... Press shift-c to stop.')
        while hub.running:
            time.sleep(0.040)
            # Pull recent EMG data from the buffer
            emg_data = listener.get_emg_data()
            # Transform it to numpy matrix
            emg_data = np.array([x[1] for x in emg_data])

            # avoid len() report error
            if (emg_data.ndim==2):
                if (emg_data.shape[0]==512):
                    # calculate MAV of emg data
                    mav_data = calculate.MAV(emg_data)
                    mav_data = np.array(mav_data.T)

                    plotter.update_plot(mav_data)

                    move.move_cursor(mav_data)


            if keyboard.is_pressed('C'):
                print('Stop.')
                break


if __name__ == '__main__':
    main()
