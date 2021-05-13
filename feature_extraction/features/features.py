# Features were extracted from each signal segment, which produced a vector of ten elements:
# four scalars features (MAV, ZC, SSL, WL) plus six AR coefficients.

import numpy as np
from collections import deque



# Create a class of features
class Feature:
    def __init__(self, input_len):
        self.n = input_len
        # self.y = 0
        # self.a = 24/25*np.ones([8,1])
        self.y = np.zeros(8)
        self.a = 24/25
        self.mav_data_queue = deque(maxlen=self.n)


# This  is a first order IIR filter, a∈[0,1]
# -----------y[n] = (1-a)*x[n] + a*y[n-1]-----------
    def filter(self,x):  # x, self.y: 1x8
        # self.y = (1-self.a[self.i]) * x + self.a[self.i] * self.y
        self.y = (1 - self.a) * x + self.a * self.y
        return self.y

# MAV: Mean Absolute Value

    def MAV(self, in_data):  # 512*8
        mav_data = np.zeros((0,8))  # 8 columns
        for sample in in_data:
            aaa = self.filter(np.array(abs(sample)))
            mav_data = np.row_stack((mav_data, aaa))
        return mav_data

# Use a first order IIR filter
#     def MAV(self, in_data):  # 512*8
#         mav_data = []
#         for self.i in range(0,8):
#             col_data = in_data[:,self.i]
#             abs_data = np.absolute(col_data)
#             # filter
#             for n in range(0, len(abs_data)):
#                 abs_data[n] = self.filter(abs_data[n])
#             mav_data.append(list(abs_data))
#         return mav_data
