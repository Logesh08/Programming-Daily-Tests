# Array Print Every Mth Integer
# An array of N integers and an integer value M are given as input. The program must print every Mth integer in the array.

# Boundary Condition(s):
# 1 <= N <= 100000

# Input Format:
# The first line contains N and M separated by space(s).
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains every Mth integer values separated by a space.

# Example Input/Output 1:
# Input:
# 7 2
# 1 2 3 4 5 6 7

# Output:
# 2 4 6

# Example Input/Output 2:
# Input:
# 10 3
# 22 72 94 29 19 27 392 28 20 67

# Output:
# 94 27 20






n,m=map(int,input().split())
arr=input().split()
for i in range(n):
    if (i+1)%m==0:
        print(arr[i],end=' ')