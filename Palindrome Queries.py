# Palindrome Queries
# The program must accept a string S containing only lower case alphabets and Q queries as the input. Each query contains two integers L and R represent the starting position and ending position of a substring in S. For each query, the program must rearrange the alphabets in the specified substring to make a palindrome. If two or more palindromes are possible, then the program must consider the lexicographically smallest palindrome. The program must ignore the query if no palindrome is possible on rearranging the alphabets. After each query, the program must print the revised string as the output.

# Boundary Condition(s):
# 1 <= L < R <= Length of S <= 100
# 1 <= Q <= 100

# Input Format:
# The first line contains S.
# The second line contains Q.
# The next Q lines, each contains L and R separated by a space.

# Output Format:
# The first Q lines, each contains the revised string.

# Example Input/Output 1:
# Input:
# skillrack
# 1
# 3 5

# Output:
# sklilrack

# Explanation:
# Here the given string is skillrack and Q = 1.
# Query 1: L=3, R=5 and the substring is ill. After rearranging the alphabets in the substring to a palindrome, the string becomes sklilrack.

# Example Input/Output 2:
# Input:
# adccbcaacb
# 4
# 2 5
# 6 9
# 4 10
# 1 9

# Output:
# adccbcaacb
# adccbaccab
# adcabcccba
# abccdccbaa