# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:12:14 2019
https://github.com/lazyprogrammer/machine_learning_examples
git clone https://github.com/lazyprogrammer/machine_learning_examples.git
@author: Usuario
"""
import numpy as np
import matplotlib.pyplot as plt
L = [1,2,3]
A = np.array([1,2,3])

for e in L:
    print(e)
    
for e in A:
    print(e)
    
  
L.append(4)

A = A + np.array([10,12])

plt.title("L")    
plt.plot(L)
plt.show()

plt.title("A")  
plt.plot(A)
plt.show()