# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:50:08 2019

@author: Usuario
"""
import numpy as np
L = [1,2,3]
A = np.array([1,2,3])


for i in L:
    print(i)
    
for i in A:
    print(i)
    
L.append(5)

A2 = []

for i in A:
    A2.append(i+i)
    
print(np.sqrt(A))
print(np.log(A))
print(np.exp(A))

