# Anagram

# Given two strings S1 and S2 as input containing only alphabets, the program must print YES if S1 is an anagram of S2. Else the program must print NO.
# Note: Two words are anagram of one another if their letters can be rearranged to form the other word.

# Boundary Condition(s):
# 1 <= Length of S1 <= 1000
# 1 <= Length of S2 <= 1000

# Input Format:
# The first line contains the string S1.
# The second line contains the string S2.

# Output Format:
# The first line contains the string YES or NO.

# Example Input/Output 1:
# Input:
# stool
# tools

# Output:
# YES

# Explanation :
# All the characters in the string S1 are present in the string S2.

# Example Input/Output 2:
# Input:
# state
# tasty

# Output:
# NO

# Explanation :
# The character 'e' in string S1 is not present in the string S2 and the character 'y' is not present in the string S1.






print('YES' if sorted((input().strip())) == sorted((input().strip())) else 'NO')
