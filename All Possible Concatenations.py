# All Possible Concatenations
# The program must accept two string values S1 and S2 as the input. The program must concatenate the given two string values in all 8 possible ways as given below.
# S1 + S2
# S1 + Reverse of S2
# Reverse of S1 + S2
# Reverse of S1 + Reverse of S2
# S2 + S1
# S2 + Reverse of S1
# Reverse of S2 + S1
# Reverse of S2 + Reverse of S1
# Finally, the program must print the 8 possible concatenated string values in sorted order.

# Boundary Condition(s):
# 1 <= Length of S1, S2 <= 100

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first 8 lines contain the sorted concatenations of S1 and S2.

# Example Input/Output 1:
# Input:
# skill
# rack

# Output:
# kcarlliks
# kcarskill
# llikskcar
# lliksrack
# racklliks
# rackskill
# skillkcar
# skillrack

# Explanation:
# S1 + S2 = skillrack
# S1 + Reverse of S2 = skillkcar
# Reverse of S1 + S2 = lliksrack
# Reverse S1 + Reverse of S2 = llikskcar
# S2 + S1 = rackskill
# S2 + Reverse of S1 = racklliks
# Reverse of S2 + S1 = kcarskill
# Reverse of S2 + Reverse of S1 = kcarlliks
# So the 8 concatenated string values are printed in sorted order.

# Example Input/Output 2:
# Input:
# abcd
# pqrst

# Output:
# abcdpqrst
# abcdtsrqp
# dcbapqrst
# dcbatsrqp
# pqrstabcd
# pqrstdcba
# tsrqpabcd
# tsrqpdcba






a=input().strip()
b=input().strip()
arr=[]
arr.append(a+b)
arr.append(a+b[::-1])
arr.append(a[::-1]+b)
arr.append(a[::-1]+b[::-1])
arr.append(b+a)
arr.append(b+a[::-1])
arr.append(b[::-1]+a)
arr.append(b[::-1]+a[::-1])
[print(i) for i in sorted(arr)]