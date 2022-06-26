# Immediate Smaller To M
# Given an integer array of size N and an integer M as input, the program must print the immediate smaller array element to M. If there no smaller array element to M, then the print -1.

# Boundary Condition(s):
# 2 <= N <= 100

# Input Format:
# The first line contains the value of N.
# The second line contains the N values separated by space(s).
# The third line contains the value of M.

# Output Format:
# The first contains the immediate smaller array element to M.

# Example Input/Output 1:
# Input:
# 5
# 2 1 3 4 5
# 3

# Output:
# 2

# Example Input/Output 2:
# Input:
# 10
# 32 65 56 26 78 84 89 43 67 45
# 15

# Output:
# -1





n = int(input())
arr = list(map(int,input().split()))
m = int(input())
for i in range(m)[::-1]:
    if i in arr:
        print(i)
        exit()
print(-1)