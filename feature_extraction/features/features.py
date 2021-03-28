# Features were extracted from each signal segment, which produced a vector of ten elements:
# four scalars features (MAV, ZC, SSL, WL) plus six AR coefficients.

import numpy as np
from collections import deque
from IIRFilter import LowPassIIR


# Create a class of features
class Feature:
    def __init__(self, input_len):
        self.n = input_len
        # self.mav_data_queue = deque(maxlen=self.n)

# MAV: Mean Absolute Value
# Use a first order IIR filter
    def MAV(self, in_data):  # 512*8
        mav_data = [[0] * 512 for i in range(0, 8)]
        for i in range(0,8):
            col_data = in_data[:,i]
            abs_data = np.absolute(col_data)
            # filter
            IIR = LowPassIIR(a=1/25)
            for n in range(0, len(abs_data)):
                abs_data[n] = IIR.filter(abs_data[n])

            mav_data[i] = abs_data  # 1*512
            # self.mav_data_queue.append(mav_data[i])
        mav_data = np.array(mav_data)
        return mav_data


# ZC:
