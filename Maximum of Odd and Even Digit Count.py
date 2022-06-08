# Maximum of Odd and Even Digit Count
# An integer N is passed as input. The program must print the odd digit count if odd digit count is greater than even digit count. Else the program must print the even digit count.

# Boundary Condition(s):
# 1 <= N <= 999999999

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains an integer.

# Example Input/Output 1:
# Input:
# 12345

# Output:
# 3

# Example Input/Output 2:
# Input:
# 8982374

# Output:
# 4






s = (input().strip())
od=ev=0
for c in s:
    if int(c)%2: od+=1
    else: ev+=1
print(max([od,ev]))