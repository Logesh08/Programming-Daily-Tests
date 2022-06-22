# Print All Elements From Mth Integer Circularly
# An array of N integers and an integer M are passed as input. The program must print all the values in array starting from Mth integer circularly.

# Boundary Condition(s):
# 1 <= M <= 10

# Input Formmat:
# The First line  contains the vlaue of N and M.
# The second line contains the N values.

# Output Format:
# The first line contains the values in array starting from Mth integer circularly.

# Example Input/Ouput 1:
# Input:
# 5 3
# 1 2 3 4 5

# Output:
# 3 4 5 1 2

# Example Input/Output 2:
# Input:
# 7 2
# 11 13 15 16 17 12 19 14 16

# Output:
# 13 15 16 17 12 19 14 16 11








n,n=map(int,input().split())
arr = input().split()
n-=1 
print(*arr[n:]+arr[:n])