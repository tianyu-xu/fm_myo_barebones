# Features were extracted from each signal segment, which produced a vector of ten elements:
# four scalars features (MAV, ZC, SSL, WL) plus six AR coefficients.

import numpy as np
from collections import deque
import math


# MAV: Mean Absolute Value
mav_data_queue = deque(maxlen = 512)
def MAV(in_data):  # 512*8
    mav_data = {}
    num_splitarray = np.linspace(0,496,64,dtype=int) #(step = 8, num = 64)
    for j in num_splitarray:
        for i in range(0,8):
            col_data = in_data[j:(j+16),i]
            abs_data = np.absolute(col_data)
            mav_data[i] = sum(abs_data)/len(abs_data)
            # mav_data.append(mav_datai)
        mav_data = list(mav_data)
        mav_data_queue.append(mav_data)
    return list(mav_data_queue)


# ZC:
