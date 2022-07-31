# Matrix Zig-zag Pattern

# The program must accept R, C and a series of K integers as input. The program must print the natural numbers in R*C matrix in zig-zag fashion. Each integer in the series denotes the count of the integer to be printed. (For example, 4 2 1 denotes 1 must be printed 4 times, 2 must be printed 2 times and 3 must be printed 1 time).
# Note: sum of counts = R*C

# Boundary Condition(s):
# 1 <= R, C <= 20
# 1 <= K <= 20

# Input Format:
# The first line contains the value of R and C separated by space.
# The second line contains the count of each integer separated by space(s).

# Output Format:
# The first R lines contains C integers separated by space.

# Example Input/Output 1:
# Input:
# 2 3
# 4 1 1

# Output:
# 1 1 1
# 3 2 1

# Explanation:
# Here, number of rows are 2 and columns are 3.
# Number of 1's are 4.
# Number of 2's is 1.
# Number of 3's is 1.
# Thus, the zigzag pattern is printed as output.

# Example Input/Output 2:
# Input:
# 4 4
# 1 2 1 4 2 3 3

# Output:
# 1 2 2 3
# 4 4 4 4
# 5 5 6 6
# 7 7 7 6









r,c = map(int,input().split())
arr = list(map(int,input().split()))
start = p = 1
t=[]
for i in arr:
    for j in range(i):
        t.append(start)
        if len(t)==c:
            print(*t if p%2 else t[::-1])
            p += 1
            t=[]
    start += 1