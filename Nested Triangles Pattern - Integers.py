# Nested Triangles Pattern - Integers
# The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 50

# Input Format:
# The first line contains N.

# Output Format:
# The first (2N+1) lines contain the pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 3

# Output:
# *
# *1*
# *121*
# *12321*
# *121*
# *1*
# *

# Explanation:
# Here N=3, so the pattern contains 7 lines((2*3)+1) of output.
# The 1st layer of the triangle contains asterisks.
# The 2nd layer of the triangle contains 1s.
# The 3rd layer of the triangle contains 2s.
# The 4th(inner) layer of the triangle contains 3.

# Example Input/Output 2:
# Input:
# 4

# Output:
# *
# *1*
# *121*
# *12321*
# *1234321*
# *12321*
# *121*
# *1*
# *



N = int(input())
arr = []
print("*")
for i in range(1,N+1):
    s = ""
    for j in range(1,i+1):
        s+=str(j)
    for j in range(j-1,0,-1):
        s+=str(j)
    arr.append(s)
    print("*"+s+"*")
arr.pop()
while arr:
    print("*"+arr.pop()+"*")
print("*")