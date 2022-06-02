# Character Repeating N Times
# A string S and an integer N are passed as input. The program must print the characters occurring exactly N times in the order of their occurrence.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= Length of String <= 1000

# Input Format:
# The first line contains the string and N value separated by space(s).

# Output Format:
# The first line contains the specified output.

# Example Input/Output 1:
# Input:
# attack 2

# Output:
# at

# Example Input/Output 2:
# Input:
# implementation 2

# Output:
# iment






s,n = input().split()
for c in sorted(set(s),key = lambda x: s.index(x)):
    if s.count(c)==int(n):
        print(c,end='')