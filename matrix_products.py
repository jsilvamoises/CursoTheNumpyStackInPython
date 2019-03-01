# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:23:04 2019

@author: Usuario
"""
import numpy as np


A = np.array([[1,2],[3,4]])

Ainv = np.linalg.inv(A)
Ainv
Ainv.dot(A)
A.dot(Ainv)
np.linalg.det(A)
np.diag(A)

np.diag([1,10])

a = np.array([1,2])
b = np.array([3,4])

np.outer(a,b)
np.inner(a,b)
a.dot(b)
np.diag(A).sum()

np.trace(A)

X = np.random.randn(100,3)
cov = np.cov(X)
cov
cov.shape
cov = np.cov(X.T)
cov

np.linalg.eigh(cov)

np.linalg.eig(cov)


A = np.array([[1,1],[1.5,4]])
B = np.array([2200,5050])

np.linalg.solve(A,B)
