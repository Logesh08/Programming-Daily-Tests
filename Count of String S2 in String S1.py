# Count of String S2 in String S1

# The program must accept two string values S1 and S2 as the input. The program must print the count of occurrence(s) of the string S2 in the string S1. 

# Boundary Condition(s):
# 2 <= Length of S1 <= 1000
# 2 <= Length of S2 <= 1000

# Input Format:
# The first line contains the values of S1 and S2 separated by a space.

# Output Format:
# The first line contains the count of occurrence(s) of the string S2 in the string S1.

# Example Input/Output 1:
# Input:
# abcdbcdbcbbcd bcd

# Output:
# 3

# Explanation:
# bcd has occurred in abcdbcdbcbbcd for thrice.

# Example Input/Output 2:
# Input:
# nsidsiddidsid id

# Output:
# 4


a,b = input().split()
print(a.count(b))