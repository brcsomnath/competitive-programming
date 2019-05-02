'''
Matrix Chain Multiplication | DP-8
Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
The problem is not actually to perform the multiplications, but merely to decide in which order 
to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative. 
In other words, no matter how we parenthesize the product, the result will be the same. For example, 
if we had four matrices A, B, C, and D, we would have:

(ABC)D = (AB)(CD) = A(BCD) = ....
However, the order in which we parenthesize the product affects the number of simple arithmetic 
operations needed to compute the product, or the efficiency. For example, suppose A is a 10 × 30 matrix, 
B is a 30 × 5 matrix, and C is a 5 × 60 matrix. Then,

(AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
'''

def process(arr):
    N = len(arr)
    dp = [[float('inf')] for i in range(N)] for j in range(N)

    for i in range(N):
        dp[i][i] = 0
    
    for length in range(2, N):
        for start in range(N-L):
            end = start + length
            for finish in range(start + 1, end):
                dp[start][end] = min(dp[start][end], dp[start][finish] + dp[finish+1][end] + arr[start-1]*arr[finish]*arr[end])
    return dp[1][N-1]