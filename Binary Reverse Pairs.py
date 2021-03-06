# Binary Reverse Pairs
# The program must accept N odd integers and print all possible pairs of integers (X, Y) where the binary representation of X is equal to the reverse of the binary representation of Y. If there is no such pair, then the program must print -1 as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Each integer value < 10^5

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.

# Output Format:
# The lines, each contains a pair of integers separated by a space or the first line contains -1.

# Example Input/Output 1:
# Input:
# 7
# 23 35 37 17 29 49 17

# Output:
# 23 29
# 35 49
# 17 17

# Explanation:
# 23 -> 10111
# 35 -> 100011
# 37 -> 100101
# 17 -> 10001
# 29 -> 11101
# 49 -> 110001
# 17 -> 10001
# The binary representation of 23 is equal to the reverse of the binary representation of 29.
# The binary representation of 35 is equal to the reverse of the binary representation of 49.
# The binary representation of 17 is equal to the reverse of the binary representation of 17.

# Example Input/Output 2:
# Input:
# 4
# 13 91 25 21

# Output:
# -1

# Example Input/Output 3:
# Input:
# 7
# 15 15 15 19 25 25 19

# Output:
# 15 15
# 15 15
# 15 15
# 19 25
# 19 25
# 25 19
# 25 19



input()
def toInt(x):
    return int(x,2)
def xtreme(x):
    return bin(int(x))[2:]
arr=list(map(xtreme,input().split()))
p=False
for i in range(len(arr)):
    x=arr[i]
    y = x[::-1]
    t=arr[i+1:]
    while y in t:
        t.remove(y)
        print(toInt(x),toInt(y))
        p=True
if not p: print(-1)

