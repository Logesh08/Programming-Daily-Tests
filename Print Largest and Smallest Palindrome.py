# Print Largest and Smallest Palindrome
# A series of strings is passed as input. The program must print the largest and smallest palindrome in it. If more than one largest or smallest palindrome exist print the first occurring palindrome. If there is no palindrome then print -1.

# Boundary Condition(s):
# 1 <= length of string <=100

# Input Format:
# The first line contains series of strings separated by space(s).

# Output Format:
# The first line contains the largest palindrome.
# The second line contains the smallest palindrome.

# Example Input/Output 1:
# Input:
# aba abba abcba aabbaa z

# Output:
# aabbaa
# z

# Example Input/Output 2:
# Input:
# madam mam mem modulation malayalam 

# Output:
# malayalam
# mam














words = input().strip().split()
palindrom = [word for word in words if word==word[::-1]]
palindrom.sort(key=len)
if palindrom:
    l = len(palindrom[-1])
    for word in palindrom:
        if len(word)==l:
            print(word)
            break
    print(palindrom[0])
else:
    print(-1)