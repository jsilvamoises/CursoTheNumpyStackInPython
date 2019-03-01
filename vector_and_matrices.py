# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:09:48 2019

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt

M = np.array([[1,2],[3,4]])

L = [[1,2],[3,4]]
L[0]

M[0][0]
M[0,0]

M2 = np.matrix([[1,2],[3,4]])

M2

A = np.array(M2)
A.T # Transposta

plt.plot(A)

R = np.random.rand(100,2)
plt.plot(R)