# Sort Columns based on Sum

# The program must accept an integer matrix of size R*C as input. The program must sort the columns(ascending order) based on their sum. Finally, the program prints the matrix.

# Boundary Condition(s):
# 1 <= R, C <= 50

# Input Format:
# The first line contains the values of R and C.
# The next R lines contain C integers each separated by space(s).

# Output Format:
# The first R lines contain C integers each separated by a space.

# Example Input/Output 1:
# Input:
# 3 3
# 5 1 6 
# 4 2 9 
# 8 7 3 

# Output:
# 1 5 6
# 2 4 9
# 7 8 3

# Explanation :
# The sum of the first column is (5+4+8) 17
# The sum of the second column is (1+2+7) 10
# The sum of the third column is (6+9+3) 18
# Arrange(in ascending) the columns based on their sums.

# Example Input/Output 2:
# Input:
# 4 3
# 4 8 9 
# 5 7 4
# 8 9 5
# 2 3 7

# Output:
# 4 9 8
# 5 4 7
# 8 5 9
# 2 7 3







r,c = map(int,input().split())
mat = sorted(list(map(list,zip(*[list(map(int,input().split())) for _ in range(r)]))),key = lambda x: sum(x))
[print(*row) for row in zip(*mat)]