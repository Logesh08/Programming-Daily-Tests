# Equal Number of 1's in Binary Representation

# The program must accept three integers X, Y and N as the input. The program must print the integers from X to Y (inclusive) with the number of 1's in their binary representatoin is equal to the number of 1's in the binary representation of N. If no integer matches the given condition, then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= X, Y, N <= 100000

# Input Format:
# The first line contains the values of X, Y and N separated by space(s).

# Output Format:
# The first line contains the integers separated by a space.

# Example Input/Output 1:
# Input:
# 2 10 3

# Output:
# 3 5 6 9 10 

# Explanation:
# The integers from 2 to 10 are 2, 3, 4, 5, 6, 7, 8, 9 and 10.
# The number of 1's in the binary representation of N (3 -> 0011) is 2.

# 2 -> 0010
# The count of 1's in the binary represention of 2 is 1 and 1 is not equal to 2.
# 3 -> 0011
# The count of 1's in the binary represention of 3 is 2 and 2 is equal to 2.
# Hence 3 is printed.
# 4 -> 0100
# The count of 1's in the binary represention of 4 is 1 and 1 is not equal to 2.
# 5 -> 0101
# The count of 1's in the binary represention of 5 is 2 and 2 is equal to 2.
# Hence 5 is printed.
# 6 -> 0110
# The count of 1's in the binary represention of 6 is 2 and 2 is equal to 2.
# Hence 6 is printed.
# 7 -> 0111
# The count of 1's in the binary represention of 7 is 3 and 3 is not equal to 2.
# 8 -> 1000
# The count of 1's in the binary represention of 8 is 1 and 1 is not equal to 2.
# 9 -> 1001
# The count of 1's in the binary represention of 9 is 2 and 2 is equal to 2.
# Hence 9 is printed.
# 10 -> 1010
# The count of 1's in the binary represention of 10 is 2 and 2 is equal to 2.
# Hence 10 is printed.

# Example Input/Output 2:
# Input:
# 20 30 2

# Output:
# -1








x,y,n = map(int,input().split())
n = bin(n)[2:].count('1')
arr = []
for i in range(x,y+1):
    cur = bin(i)[2:] [::-1]
    if cur.count('1') == n:
        arr.append(i)
print(*arr if arr else [-1])