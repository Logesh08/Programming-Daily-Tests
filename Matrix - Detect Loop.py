# Matrix - Detect Loop
# The program must accept an integer matrix of size R*C containing only nonzero integers and the position of a cell in the matrix as the input. The program must traverse the matrix starting from the given cell based on the following conditions.
# - If the integer in the current cell is positive even, then move to the next cell in the top direction.
# - If the integer in the current cell is positive odd, then move to the next cell in the right direction.
# - If the integer in the current cell is negative even, then move to the next cell in the bottom direction.
# - If the integer in the current cell is negative odd, then move to the next cell in the left direction.
# The program must traverse the matrix till it exits the matrix(moving outside the matrix) or enters a loop(traversing the same set of cells repeatedly). The program must print "YES" if there is a loop when traversing the matrix. Else the program must print "NO" as the output.

# Boundary Condition(s):
# 2 <= R, C <= 50
# -1000 <= Matrix element value <= 1000

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.
# The (R+2)th line contains two integer values separated by a space representing the position of a cell in the matrix.

# Output Format:
# The first line contains YES or NO.

# Example Input/Output 1:
# Input:
# 5 5
# 75 50 43 -14 28
# 64 77 35 49 -54
# 73 62 54 41 -60
# 39 50 -37 -95 -17
# -69 28 75 37 16
# 2 2

# Output:
# YES

# Explanation:
# The starting position of the traversal is (2, 2).
# There is a loop in the given matrix which is highlighted below.
# 75 50 43 -14 28
# 64 77 35 49 -54
# 73 62 54 41 -60
# 39 50 -37 -95 -17
# -69 28 75 37 16
# So YES is printed as the output.

# Example Input/Output 2:
# Input:
# 6 4
# -35 -61 -51 -85
# 95 24 18 82
# 86 67 43 26
# 72 18 80 29
# 96 31 20 88
# 63 23 81 74
# 5 3

# Output:
# NO











