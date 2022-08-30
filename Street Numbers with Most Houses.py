# Street Numbers with Most Houses

# N streets in a city are represented in N lines. A hyphen '-' represents a house and an asterisk '*' represents an empty ground. The streets are numbered from 1 to N from top to bottom. The program must print the street number having the most number of houses. If more than one street has the same number of maximum houses then the program must print the street numbers which has the maximum number of houses in ascending order.

# Boundary Condition(s):
# 1 <= N <= 1000
# 1 <= Length of each line <= 1000

# Input Format:
# The first line contains the value of N.
# The next N lines contain one string in each line.

# Output Format:
# The first line contains the street numbers which has the maximum number of houses separated by a space.

# Example Input/Output 1:
# Input:
# 6
# -
# --
# ----
# --*-*
# ---*-
# ---

# Output:
# 3 5

# Explanation:
# The street (line) numbers 3 and 5 has the maximum number of houses that is 4.

# Example Input/Output 2:
# Input:
# 5
# ----
# --**
# **-
# -*--
# ****

# Output:
# 1





n = int(input())
streets = [input() for _ in range(n)]
m = max(list(map(lambda x: x.count('-'),streets)))
for i in range(n):
    if streets[i].count('-')==m:
        print(i+1,end=' ') 