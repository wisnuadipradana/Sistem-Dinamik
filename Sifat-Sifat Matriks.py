# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:45:11 2021

@author: uzumakinagato
"""

import numpy as np

def Properties_Matriks(A):
    # Rank of a matrix
    print("\nRank of A:", np.linalg.matrix_rank(A))

    # Trace of matrix A
    print("\nTrace of A:", np.trace(A))

    # Determinant of a matrix
    print("\nDeterminant of A:", round(np.linalg.det(A),3))

    # Inverse of matrix A
    try:
        print("\nInverse of A:\n", np.linalg.inv(A))
    except np.linalg.LinAlgError or np.linalg.det(A)==0:
        print('\nA is Singular Matrix Then A doesn\'t have Inverse')
    
    k = 3 # A^3
    # Ganti nilai k untuk mencari nilai A^k
    print("\nMatrix A raised to power {}, A^{}:\n".format(k,k), np.linalg.matrix_power(A, k), "\n")
    
    # Eigen Value and Vector Eigen
    eigvals, eigvecs = np.linalg.eig(A)
    for i in range(len(eigvals)):
        print('nilai eigen {} = '.format(i+1), round(eigvals[i],3))
        
    print('\nmatriks vektor eigen = \n', eigvecs)
    
A = [list(map(int, input().split()))]
n = len(A[0])
for i in range(n-1):
    A.append(list(map(int, input().split())))
A = np.array(A)
Properties_Matriks(A)