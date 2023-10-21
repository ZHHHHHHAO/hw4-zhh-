import numpy as np
import pylab
import scipy.integrate as integrate
#I typed these in Chat GPT
#A =[0 1 1 0 0 0]
#[0 0 1 1 0 0]
#[1 0 0 0 0 0]
#[0 1 0 0 1 0]
#[0 1 0 1 0 1]
#[0 0 0 0 1 0] 
#coding it in python

A = np.array([[0, 1, 1, 0, 0, 0],
              [0, 0, 1, 1, 0, 0],
              [1, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 0, 0, 0, 1, 0]])

# typed question in ChatGPT
# Normalize the columns of A

column_sums = A.sum(axis=0, keepdims=True)
M = A / column_sums

# typed question in ChatGPT
#r = np.ones(6),but it is wrong

r = np.ones(6)/6
print(r)
# create alpha
alpha = 0.85

# Create vector s with all entries equal to 1/6

s = np.full(6, 1/6)

# Convergence threshold

threshold = 1e-6
while True:

    # Update the rank using the formula

    r_prime = alpha * np.dot(M, r) + (1 - alpha) * s 

    # Check for convergence

    if np.all(np.abs(r_prime - r) < threshold):
        break

    # Update the rank vector for the next iteration

    r = r_prime
print("Converged Rank Vector:")
print(r_prime)

# Calculate the eigenvector corresponding to the largest eigenvalue of M

eigenvalues, eigenvectors = np.linalg.eig(M)
largest_eigenvalue_index = np.argmax(eigenvalues)
largest_eigenvector = np.real(eigenvectors[:, largest_eigenvalue_index])
print("\nEigenvector Corresponding to Largest Eigenvalue:")
print(largest_eigenvector)

#output of ChatGPT
#This code calculates the PageRank using the iterative approach as before and also calculates
#the eigenvector corresponding to the largest eigenvalue of matrix M. The comparison is printed 
#at the end, and you should observe that the PageRank result is closely related to the eigenvector 
#of M corresponding to the largest eigenvalue.

# Verification by ChatGPT
is_normalized = np.allclose(M.sum(axis=0), 1)
print("Are the columns of M normalized?", is_normalized)
is_alpha_not_equal_to_1 = alpha != 1
print("Is alpha not equal to 1?", is_alpha_not_equal_to_1)
vector_difference = largest_eigenvector - r_prime
print(vector_difference)