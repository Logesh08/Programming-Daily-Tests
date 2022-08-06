# The program must accept a pattern P as a string and another string S as input. The program must print the words in S which are similar to the given pattern P and of the same length as P. The word is said to be similar to the pattern if the occurrence count of character matches. If there is no word following the pattern P, then print -1 as the output.

# Boundary Condition(s):
# 2 <= The length of P <= 99
# 1 <= The length of S <= 10000

# Input Format:
# The first line contains a pattern P.
# The second line contains a string S.

# Output Format:
# The first line contains either the matching word(s) or -1. 

# Example Input/Output 1:
# Input:
# rrhjkrrr
# mmghieee hrrjkrrr akasjd kkalixxx acd

# Output:
# mmghieee kkalixxx 

# Explanation:
# The given pattern contains two 'r', one 'h', one 'j', one 'k' and three 'r'.
# The first word contains two 'm', one 'g', one 'h', one 'i' and three 'e', which is similar to the given pattern.
# Thus the first word is printed.
# The second word contains one 'h', two 'r', one 'j', one 'k' and three 'r', which is not similar to the pattern.
# The third word contains one 'a', one 'k', one 'a', one 's', one 'j' and one 'd', which is not similar to the pattern.
# The fourth word contains two 'k', one 'a', one 'l', one 'i' and three 'x', which is similar to the given pattern.
# Thus the fourth word is printed.
# The fifth word contains one 'a', one 'c' and one 'd', which is not similar to the pattern.

# Example Input/Output 2:
# Input:
# apple
# mango orange

# Output:
# -1








s = list(input().strip())
arr = input().split()
def getPattern(x):
    cur = 1
    t=""
    c = x.pop(0)
    while x:
        n = x.pop(0)
        if n==c:
            cur += 1
        else:
            t += str(cur)
            cur = 1
            c = n
    t+=str(cur)
    return t 
p = getPattern(s)
match = [pattern for pattern in arr if getPattern(pattern)==p]
print(*match if match else [-1])