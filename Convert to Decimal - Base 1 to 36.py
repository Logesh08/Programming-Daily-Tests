# Convert to Decimal - Base 1 to 36
# The program must accept a string N representing a number and an integer B representing a base as the input. The program must convert the number N from the base B to the decimal value D and print it as the output. If it is not possible to convert the number N to the decimal value from the base B, then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= Length of N <= 6
# 1 <= B <= 36

# Input Format:
# The first line contains N and B separated by a space.

# Output Format:
# The first line contains D or -1.

# Example Input/Output 1:
# Input:
# 11A 16

# Output:
# 282

# Explanation:
# Here N=11A and B=16.
# The decimal equivalent of (11A)16 is 282.
# Hence the output is 282.

# Example Input/Output 2:
# Input:
# 7b 12

# Output:
# 95

# Example Input/Output 3:
# Input:
# 154 5

# Output:
# -1










s,base = input().split()
print(int(s,int(base)))