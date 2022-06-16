# Odd Integer Between Even Integers
# An array of N integers are given as input. The program must print all the odd integers present between two even integers in reverse order. Consider only the available adjacent elements when one adjacent element is missing.

# Boundary Condition(s):
# 2 <= N <= 10000

# Input Format:
# The first line contains N.
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains odd integers present between two even integers separated by a space.

# Example Input/Output 1:
# Input:
# 6
# 76 27 16 7 22 9

# Output:
# 9 7 27

# Example Input/Output 2:
# Input:
# 7
# 37 18 83 74 3 1 82

# Output:
# 83 37












n=int(input())
arr = list(map(int,input().split()))
t=[]
for i in range(n):
    if i==0:
        if arr[i]%2 and arr[i+1]%2==0:
            t.append(arr[i])
    elif i==n-1:
        if arr[i]%2 and arr[i-1]%2==0:
            t.append(arr[i])
    else:
        if arr[i]%2 and arr[i+1]%2==0 and arr[i-1]%2==0:
            t.append(arr[i])
print(*t[::-1])