# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:48:34 2019

@author: Usuario
"""

import numpy as np
X = []
for line in open("lotofacil.csv"):
    row = line.split(";")
    sample = map(float,row)
    X.append(sample)
    
X = np.array(X)