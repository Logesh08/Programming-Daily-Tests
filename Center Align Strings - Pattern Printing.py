# Center Align Strings - Pattern Printing

# The program must accept a list of string values as the input. The program must center align the string values along with asterisks and hyphens as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= Number of strings <= 20
# 0 <= Length of each string <= 50

# Input Format:
# The list of lines contain a string in each line.

# Output Format:
# The list of lines contain the center aligned string values along with asterisks and hyphens.

# Example Input/Output 1:
# Input:
# This is a

# hypothetical
# situation

# Output:
# **************
# *--This is a-*
# *------------*
# *hypothetical*
# *--situation-*
# **************

# Example Input/Output 2:
# Input:
# Joe
# waited
# for the
# train

# Output:
# *********
# *--Joe--*
# *-waited*
# *for the*
# *-train-*
# *********







lines = []
try:
    while True:
        lines.append(input().strip())
except:
    n = max(list(map(len,lines)))
    print('*'*(n+2))
    for line in lines:
        i =1
        while len(line)!=n:
            if i%2:
                line = '-'+line
            else:
                line = line+'-'
            i +=1
        print('*'+line+'*')
    print('*'*(n+2))
    