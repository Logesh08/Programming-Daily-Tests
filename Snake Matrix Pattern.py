# Snake Matrix Pattern
# The program must accept an integer N as the input. The program must print the snake matrix pattern based on the following conditions.
# - The pattern contains N lines, where the integers from 1 to N*N occur in the horizontal zigzag direction.
# - In the 1st line, N-1 asterisks and the first N integers (1 to N) are printed.
# - In the 2nd line, N-2 asterisks and the next N integers (N+1 to 2*N in reverse order) are printed.
# - In the 3rd line, N-3 asterisks and the next N integers (2*N+1 to 3*N) are printed.
# - In the 4th line, N-4 asterisks and the next N integers (3*N+1 to 4*N in reverse order) are printed.
# - Similarly, the remaining lines are printed as the output.

# Boundary Condition(s):
# 2 <= N <= 50

# Input Format:
# The first line contains N.

# Output Format:
# The first N lines contain the snake matrix pattern based on the given conditions.

# Example Input/Output 1:
# Input:
# 4

# Output:
# * * * 1 2 3 4
# * * 8 7 6 5
# * 9 10 11 12
# 16 15 14 13

# Explanation:
# Here N = 4, so the pattern contains 4 lines, where the integers from 1 to 16 occur in the horizontal zigzag direction.

# Example Input/Output 2:
# Input:
# 7

# Output:
# * * * * * * 1 2 3 4 5 6 7
# * * * * * 14 13 12 11 10 9 8
# * * * * 15 16 17 18 19 20 21
# * * * 28 27 26 25 24 23 22
# * * 29 30 31 32 33 34 35
# * 42 41 40 39 38 37 36
# 43 45 45 46 47 48 49









p = 1 
n = int(input())
mat = []
row = []
for i in range(n*n):
    row.append(p)
    if p%n==0: 
        mat.append(row)
        row = []
    p += 1
    
for i in range(n):
    print('* '*(n-i-1),end='')
    if i%2==0: row = mat[i]
    else: row = mat[i][::-1]
    print(*row)