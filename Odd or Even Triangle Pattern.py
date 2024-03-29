# Odd/Even Triangle Pattern

# The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 3 <= N <= 100

# Input Format:
# The first line contains N.

# Output Format:
# The lines containing the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 5

# Output:
# 1*3*5
# -7*9
# --11

# Example Input/Output 2:
# Input:
# 8

# Output:
# 2*4*6*8
# -10*12*14
# --16*18
# ---20




n = int(input())
half = n//2 + n%2
start = 2 - n%2
for i in range(half):
    arr = []
    for j in range(half - i):
        arr.append(str(start))
        start += 2
    print('-'*i +'*'.join(arr))