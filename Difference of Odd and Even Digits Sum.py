# Difference of Odd and Even Digits Sum
# Given an Integer N, the program must print the absolute difference of the sum of odd digits and sum of even digits. 

# Boundary Condition(s):
# 1 <= N <= 99999999999999

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the output as specified. 

# Example Input/Output 1:
# Input:
# 12345

# Output:
# 3

# Explanation:
# |(1+3+5) - (2+4)| = 3

# Example Input/Output 2:
# Input:
# 89235

# Output:
# 7

# Explanation:
# |(8+2) - (9+3+5)| = 7


o=e=0
for i in input().strip():
    i=int(i)
    if i%2:o+=i 
    else:e+=i 
print(abs(o-e))