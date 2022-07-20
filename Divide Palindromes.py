# Divide Palindromes

# The program must accept a string S as the input. String S is formed by concatenating two palindromes. The program must divide and print the palindromes separately.
# Note: If the input string is "aaa", there are two possible outputs - 'a aa' and 'aa a'. The program must print the possible output with the first palindrome of minimum possible length 'a aa'. 

# Boundary Condition(s):
# 2 <= Length of S <= 100

# Input Format:
# The first line contains the string S.

# Output Format:
# The first line contains the two string values separated by a space.

# Example Input/Output 1:
# Input:
# cdcrotor

# Output:
# cdc rotor

# Explanation :
# The two palindromes are "cdc" and "rotor".

# Example Input/Output 2:
# Input:
# ababamadam

# Output:
# ababa madam

# Explanation :
# The substring "aba" is a palindrome but the substring "bamadam" is not a palindrome. Hence the output is "ababa madam". 








s = input().strip()
for i in range(1,len(s)):
    if s[:i]==s[:i][::-1] and s[i:]==s[i:][::-1]:
        print(s[:i],s[i:])
        break