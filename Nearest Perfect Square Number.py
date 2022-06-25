# Nearest Perfect Square Number
# An integer N is passed as the input to the program. The program must print the nearest perfect square number of N.

# Boundary Condition(s):
# 1 <= N <= 9999

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains the nearest perfect square.

# Example Input/Output 1:
# Input:
# 26

# Output:
# 25

# Example Input/Output 2:
# Input:
# 49

# Output:
# 49






from math import sqrt,floor
n=int(input())
l=r=n 
def isPerfct(x):
    if sqrt(x) - floor(sqrt(x))!=0:
        return False
    return True
while not isPerfct(l) and not isPerfct(r):
    l-=1
    r+=1 
if isPerfct(r):
    print(r)
else:
    print(l)