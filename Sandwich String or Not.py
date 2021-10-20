# Sandwich String or Not
# The program must accept a string S as the input. The program must print "YES" if the given string a sandwich string. Else the program must print "NO" as the output. A sandwich string is a string that is formed by two identical ends and a different middle. The sandwich string contains only 2 unique characters.

# Boundary Condition(s):
# 1 <= Length of S <= 100

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains YES or NO.

# Example Input/Output 1:
# Input:
# XXYYYXX

# Output:
# YES

# Explanation:
# Here the given string is XXYYYXX.
# The given string has two identical ends as XX and the different middle as YYY.
# So YES is printed as the output.

# Example Input/Output 2:
# Input:
# 5@@5

# Output:
# YES

# Example Input/Output 3:
# Input:
# abababa

# Output:
# NO

# Example Input/Output 4:
# Input:
# aaaqqqaa

# Output:
# NO



S = input().strip()
P = S[0]
for i in range(1,len(S)):
    if(S[i]!=S[0]):
        break
    else:
        P+=S[i]
A = len(P)
W = S[-A:]
if(W == P):
    Q = S[len(P):-A]
    Q = list(Q)
    if(len(set(Q)) == 1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")