
# Count Set Bits - All Positions
# The program must accept an array of N integers as the input. The program must find the binary representation of each integer in the array. For each position from the LSB, the program must print the number of set bits occur in the N integers as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Each integer value <= 10^8

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.

# Output Format:
# The first line contains the number of set bits occur in the N integers.

# Example Input/Output 1:
# Input:
# 5
# 10 12 9 7 11

# Output:
# 3 3 2 4

# Explanation:
# 1010 -> 10
# 1100 -> 12
# 1001 -> 9
# 0111 -> 7
# 1011 -> 11
# 1st position from LSB, the set bits occur in 9, 7 and 11.
# 2nd position from LSB, the set bits occur in 10, 7 and 11.
# 3rd position from LSB, the set bits occur in 12 and 7.
# 4th position from LSB, the set bits occur in 10, 12, 9 and 11.

# Example Input/Output 2:
# Input:
# 2
# 15 33

# Output:
# 2 1 1 1 0 1








n = int(input())
arr = input().split()
nxt = []
m = 0
for i in arr:
    b = bin(int(i))[2:]
    nxt.append(b)
    if len(b)>m:
        m = len(b)
        maxVal = b
arr = []
for i in nxt:
    arr.append(i.zfill(m))
for i in range(m)[::-1]:
    s = 0
    for val in arr:
        if val[i]=='1': s += 1
    print(s,end= ' ')