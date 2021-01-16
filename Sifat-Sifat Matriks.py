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
    Trace = np.trace(A) 
    if Trace.imag == 0:
        print("\nTrace of A:", np.trace(A).real)
    else:
        print("\nTrace of A:", np.trace(A))
    
    # Determinant of a matrix
    det = np.linalg.det(A)
    if det.imag == 0:
        print("\nDeterminant of A: {:g}".format(det.real)) 
    else:
        print("\nDeterminant of A: {:g}".format(det))
        
    # Inverse of matrix A
    try:
        print("\nInverse of A:\n", np.linalg.inv(A))
    except np.linalg.LinAlgError or (det.real==0 and det.imag==0):
        print('\nA is Singular Matrix Then A doesn\'t have Inverse')
    
    k = 3 # A^3
    # Ganti nilai k untuk mencari nilai A^k
    A_powk = np.linalg.matrix_power(A, k) 
    print("\nMatrix A raised to power {}, A^{}:\n".format(k,k), A_powk, "\n")

    # Eigen Value and Vector Eigen
    eigvals, eigvecs = np.linalg.eig(A)
    for i in range(len(eigvals)):
        if eigvals[i].imag == 0:
            print('nilai eigen {} = '.format(i+1), "{:g}".format(eigvals[i].real))
        else:
            print('nilai eigen {} = '.format(i+1), "{:g}".format(eigvals[i]))
        
    print('\nmatriks vektor eigen = \n', eigvecs)

print('A = ') 
A = [list(map(complex, input().split()))]
n = len(A[0])
for i in range(n-1):
    A.append(list(map(complex, input().split())))
A = np.array(A).astype(complex) 
Properties_Matriks(A)
