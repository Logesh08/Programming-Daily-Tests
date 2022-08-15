# DNA Pattern

# The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.
# Note: N must be always an even integer.

# Boundary Condition:
# 4 <= N <= 40

# Input Format:
# The first line contains the value of N.

# Output Format:
# The list of lines contain the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 4

# Output:
# -**
# *--*
# -**
# *--*
# -**

# Example Input/Output 2:
# Input:
# 8

# Output:
# ---**
# --*--*
# -*----*
# *------*
# -*----*
# --*--*
# ---**
# --*--*
# -*----*
# *------*
# -*----*
# --*--*
# ---**
# --*--*
# -*----*
# *------*
# -*----*
# --*--*
# ---**
# --*--*
# -*----*
# *------*
# -*----*
# --*--*
# ---**






n=int(input())
l=[]
x=n-2
y=0
for i in range(n//2):
    l.append("-"*y+"*"+"-"*x+"*")
    x-=2
    y+=1

l=l[::-1]+l[1:]
print(l[0])
for i in range(n//2):
    print(*l[1:],sep="\n")