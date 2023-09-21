# Vertical Alignment - Two String Values

# The program must accept two string values S1 and S2 with spaces as the input. The program must align the characters in the vertically down side and then print them as shown in the Example Input/Output section.
# Note: After aligning both string values, all the white space characters must be replaced by hyphens.

# Boundary Condition(s):
# 2 <= Length of S1, S2 <= 1000

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first line contains the modified S1.
# The second line contains the modified S2.

# Example Input/Output 1:
# Input:
# hello world
# i am very happy

# Output:
# h-ll--wor-d----
# ieamoverylhappy

# Example Input/Output 2:
# Input:
# this is long text
# its not long

# Output:
# thi--is-long-----
# itssnot-long-text



# Max Execution Time Limit: 500 millisecs






a = list(input().strip().replace(" ","-"))
b = list(input().strip().replace(" ","-"))
for i in range(len(a)):
    if b[i]=='-' and a[i]!='-':
        b[i]=a[i]
        a[i]='-'
print(''.join(a))
print(''.join(b))