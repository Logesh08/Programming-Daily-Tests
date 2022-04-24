# Shift Queries - Rows and Columns
# The program must accept an integer matrix of size R*C and Q queries as the input. Each query contains two integers X, K and a character CH. For each query, the program must modify the matrix based on the following conditions.
# - If CH is 'r', then the program must shift the integers in the Xth row by K positions to the right.
# - If CH is 'c', then the program must shift the integers in the Xth column by K positions to the bottom.
# After each query, the program must print the string value "Query ", the query number and the revised matrix as the output.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Matrix element value <= 10^5
# 1 <= Q, K <= 100
# 1 <= X <= R (when CH = 'r')
# 1 <= X <= C (when CH = 'c')

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integers separated by a space.
# The R+2nd line contains Q.
# The next Q lines from the R+3rd line, each contains X, K and CH separated by a space.

# Output Format:
# For each query, the first line contains a string value "Query ", the query number and the next R lines contain the revised matrix.

# Example Input/Output 1:
# Input:
# 4 5
# 53 26 70 29 52
# 67 24 46 14 34
# 58 43 64 67 58
# 35 46 61 77 29
# 2
# 2 3 r
# 4 1 c

# Output:
# Query 1
# 53 26 70 29 52
# 46 14 34 67 24
# 58 43 64 67 58
# 35 46 61 77 29
# Query 2
# 53 26 70 77 52
# 46 14 34 29 24
# 58 43 64 67 58
# 35 46 61 67 29

# Explanation:
# Here R=4, C=5 and Q=2, so the size of an integer matrix is 4*5.
# Query 1: The values of X, K and CH are 2, 3 and 'r' respectively.
# After shifting the integers in the 2nd row by 3 positions to the right, The matrix becomes
# 53 26 70 29 52
# 46 14 34 67 24
# 58 43 64 67 58
# 35 46 61 77 29

# Query 2: The values of X, K and CH are 4, 1 and 'c' respectively.
# After shifting the integers in the 4th column by 1 position to the bottom, The matrix becomes
# 53 26 70 77 52
# 46 14 34 29 24
# 58 43 64 67 58
# 35 46 61 67 29

# Example Input/Output 2:
# Input:
# 4 4
# 31 95 92 65
# 91 97 90 10
# 27 75 48 26
# 78 72 11 66
# 3
# 3 4 r
# 1 3 c
# 4 2 r

# Output:
# Query 1
# 31 95 92 65
# 91 97 90 10
# 27 75 48 26
# 78 72 11 66
# Query 2
# 91 95 92 65
# 27 97 90 10
# 78 75 48 26
# 31 72 11 66
# Query 3
# 91 95 92 65
# 27 97 90 10
# 78 75 48 26
# 11 66 31 72














r,c = map(int,input().split())
mat = [input().split() for _ in range(r)]
q = int(input())
for _ in range(q):
    print('Query',_+1)
    x,k,c = input().split()
    x = int(x) - 1
    k = int(k)
    if c == 'r':
        for __ in range(k):
            mat[x] = [mat[x][-1]]+mat[x][:-1]
    else:
        for __ in range(k):
            b = mat[-1][x]
            for i in range(1,r)[::-1]:
                mat[i][x] = mat[i-1][x]
            mat[0][x] = b
    for row in mat: print(*row)