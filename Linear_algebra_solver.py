# this is also to test the branch
import numpy as np
def forward_subset(L, b):
    ans = np.matrix([[0.0] for _ in range(len(L))])
    curr = 0
    while curr < len(L):
        currSum = 0
        bCurr = b[curr, 0]
        for k in range(curr):
            currSum += L[curr, k] * ans[k, 0]
        ans[curr, 0] = (bCurr - currSum) / L[curr, curr]
        curr += 1
    return ans

def backward_subset(U, b):
    ans = np.matrix([[0.0] for _ in range(len(U))])
    curr = len(U) - 1
    while curr >= 0:
        currSum = 0
        bCurr = b[curr, 0]
        for k in range(curr + 1, len(U)):
            currSum += U[curr, k] * ans[k, 0]
        ans[curr, 0] = (bCurr - currSum) / U[curr, curr]
        curr -= 1
    return ans

def solve(L, U, b):
    """
    Solves the system of linear equations Ax = b using LU decomposition.
    
    Parameters:
    L (np.matrix): Lower triangular matrix from LU decomposition.
    U (np.matrix): Upper triangular matrix from LU decomposition.
    b (np.matrix): Right-hand side vector.
    
    Returns:
    np.matrix: Solution vector x.
    """
    y = forward_subset(L, b)
    x = backward_subset(U, y)
    return x
