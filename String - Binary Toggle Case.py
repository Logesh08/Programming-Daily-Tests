# String - Binary Toggle Case
# The program must accept a string S and an integer X as the input. The program must print two string values based on the following conditions.
# - For each 1s from MSB in the binary representation of X, the program must toggle the characters in the same position to upper case and for each 0s, the program must toggle the characters to lower case. The remaining characters in the string S must not be altered. Then the program must print the modified string in the first line of output.
# - For each 1s from LSB in the binary representation of X, the program must toggle the characters in the same position to upper case and for each 0s, the program must toggle the characters to lower case. The remaining characters in the string S must not be altered. Then the program must print the modified string in the second line of output.

# Note: The length of the string S is always greater than or equal to the number of bits in the binary representation of X.

# Boundary Condition(s):
# 1 <= Length of S <= 100
# 1 <= X <= 10^8

# Input Format:
# The first line contains S.
# The second line contains X.

# Output Format:
# The first line contains a string value.
# The second line contains a string value.

# Example Input/Output 1:
# Input:
# BasketBall
# 23

# Output:
# BaSKEtBall
# BaskeTbALL

# Explanation:
# Here the given string is BasketBall and the value of K is 23.
# The binary representation of 23 is 10111.
# BasketBall -> BaSKEtBall
# BasketBall -> BaskeTbALL

# Example Input/Output 2:
# Input:
# PAPER
# 10

# Output:
# PaPeR
# PApEr





s=list(input().strip())
o1=[x for x in s]
o2=[x for x in s]
n=bin(int(input()))[2:]
for i in range(len(n)):
    if n[i]=='1':
        o1[i]=o1[i].upper()
    else:
        o1[i]=o1[i].lower()
for i in range(-len(n),0,1):
    if n[i]=="1":
        o2[i]=o2[i].upper()
    else:
        o2[i]=o2[i].lower()
print("".join(o1))
print("".join(o2))