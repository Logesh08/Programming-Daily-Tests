# Hyphen Asterisk Pattern
# Accept an integer N (only odd integer) as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 49

# Input Format:
# The first line contains the integer N.

# Output Format:
# The first N lines contain the desired pattern.

# Example Input/Output 1:
# Input:
# 5

# Output:
# *
# -*
# *-*
# -*
# *

# Example Input/Output 2:
# Input:
# 7

# Output:
# *
# -*
# *-*
# -*-*
# *-*
# -*
# *











arr = []
n = int(input())
for i in range(n//2 +1):
    t=""
    for j in range(i+1):
        if j%2==0:
            t = "*" + t
        else:
            t = "-" + t 
    print(t)
    arr.append(t)
arr.pop()
while arr:
    print(arr.pop())