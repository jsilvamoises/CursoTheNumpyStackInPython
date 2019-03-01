# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:41:26 2019

@author: Usuario
"""
import numpy as np
a = np.array([1,2])
b = np.array([2,1])


dot = 0

for e,f in zip(a,b):
    dot += e*f
    
print(dot)

print(a*b)

print(np.sum(a*b))

print((a*b).sum())

print(np.dot(a,b))

print(a.dot(b))

among = np.sqrt((a*a).sum())
print(among)

among = np.linalg.norm(a)
print(among)


cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(cosangle)

angle = np.arccos(cosangle)
print(angle)