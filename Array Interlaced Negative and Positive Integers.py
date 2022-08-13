# Array Interlaced Negative and Positive Integers

# The program must accept an integer array of size N as input. The program must print the negative integers interlaced with the positive integers as in the same order in the given array.

# Boundary Condition(s):
# 1 <= N <= 1000

# Input Format:
# The first line contains the value of N.
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains the negative integers interlaced with the positive integers separated by space(s).

# Example Input/Output 1:
# Input:
# 5
# 20 30 40 -16 -27

# Output:
# -16 20 -27 30 40

# Example Input/Output 2:
# Input:
# 4
# 2 10 8 5

# Output:
# 2 10 8 5


 
 
n = int(input())
arr = list(map(int,input().split()))
neg=[]
pos=[]
for i in arr:
    if i<0: neg.append(i)
    else: pos.append(i)
while neg or pos:
    if neg: print(neg.pop(0),end=' ')
    if pos: print(pos.pop(0),end=' ')