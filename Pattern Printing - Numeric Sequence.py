# Pattern Printing - Numeric Sequence
# Accept R rows and C columns as input. The program must print the pattern as shown in the Example Input/Output section as the output.

# Boundary Condition(s):
# 1 <= R, C <= 100

# Input Format:
# The first line contains the value of R and C.

# Output Format:
# The first R lines contain the desired pattern.

# Example Input/Output 1:
# Input:
# 4 6

# Output:
# 1 2 3 4 5 6
# 2 3 4 5 6 7
# 3 4 5 6 7 8
# 4 5 6 7 8 9

# Example Input/output 2:
# Input:
# 5 4

# Output:
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 5 6 7 8









x,y=map(int,input().split())
start = 1
for i in range(x):
    print(*range(start,start+y))
    start += 1 