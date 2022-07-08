# Print Common Characters Two Strings
# Two strings S1 and S2 are passed as input. The program must print the characters present in both the strings in alphabetical order.

# Boundary Condition(s):
# 1 <= Length of Strings <= 1000

# Input Format:
# The first line contains S1 and S2 separated by space(s).

# Output Format:
# The first line contains the common characters separated by a space.

# Example Input/Output 1:
# Input:
# hello velocity

# Output:
# e l o

# Example Input/Output 2:
# Input:
# apple pepper

# Output:
# e p








(lambda x: print(*sorted([c for c in set(x[0]) if c in x[1]])))(input().split())