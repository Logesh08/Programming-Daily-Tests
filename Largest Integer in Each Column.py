# Largest Integer in Each Column
# Given a matrix M of size R*C, the program must print the largest integer in each column.

# Boundary Condition(s):
# 2 <= R, C <= 50

# Input Format:
# The first line contains R and C separated by space.
# The next R lines contain C values each separated by space.

# Output Format:
# The first line contains the largest integer in each column separated by space.

# Example Input/Output 1:
# Input:
# 3 3
# 1 8 3 
# 4 6 5
# 7 2 9

# Output:
# 7 8 9

# Example Input/Output 2:
# Input:
# 2 3
# 23 34 45
# 45 65 12

# Output:
# 45 65 45












r,c = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(r)]
mat = list(map(list,zip(*mat)))
for row in mat:
    print(max(row),end=' ')