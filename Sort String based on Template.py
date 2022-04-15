# Sort String based on Template
# The program must accept two string values S1 and S2 containing only lower case alphabets as the input. The string S2 represents a template that contains only unique alphabets. The program must sort the alphabets in the string S1 based on the following conditions.
# - The alphabets that occur in the template S2 come first in the order of their occurrence.
# - Then the other alphabets must be sorted in alphabetical order.
# Finally, the program must print the revised string S1 as the output.

# Boundary Condition(s):
# 1 <= Length of S1 <= 1000
# 1 <= Length of S2 <= 26

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first line contains the revised string S1.

# Example Input/Output 1:
# Input:
# skillrack
# lkri

# Output:
# llkkriacs

# Explanation:
# Here S1=skillrack and S2=lkri.
# After sorting the alphabets in S1 based on the given conditions, the string becomes llkkriacs.

# Example Input/Output 2:
# Input:
# abcdzyxw
# day

# Output:
# daybcwxz

# Example Input/Output 3:
# Input:
# skillrack
# zyxwvutsrqponmlkjihgfedcba

# Output:
# srllkkica











a = list(input().strip())
b = input().strip()
def bro(x):
    if x in b:
        return b.index(x)
    else:
        return ord(x)
a = sorted(a,key = lambda x: (bro(x)))
print(''.join(a))