# Fill Matrix with Alphabets
# The program must accept an integer matrix of size R*C containing only 1s and 0s. The program must accept an alphabet CH. CH may be upper case or lower case. The program must replace the 1s with the alphabets starting from CH. The 0s must be replaced with alphabets starting from CH in the reverse order. If 'z' or 'Z' has occurred, the next alphabet must be 'a' or 'A'. If 'a' or 'A' has occurred in the reverse order, the next alphabet must be 'z' or 'Z'. The revised matrix must be printed as the output.

# Boundary Condition(s):
# 2 <= R, C <= 50

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.
# The R+2nd line contains CH.

# Output Format:
# The first R lines contain the revised matrix.

# Example Input/Output 1:
# Input:
# 3 4
# 0 1 0 1
# 0 0 0 0
# 1 0 0 1
# x

# Output:
# x x w y
# v u t s
# z r q a

# Explanation:
# Here R=3, C=4 and the given 3*4 matrix is
# 0 1 0 1
# 0 0 0 0
# 1 0 0 1
# The given alphabet CH is 'x'.
# After replacing the 1s with the alphabets starting from 'x' and 0s with the alphabets starting from 'x' in reverse order, the matrix becomes
# x x w y
# v u t s
# z r q a

# Example Input/Output 2:
# Input:
# 4 4
# 0 0 0 1
# 0 0 0 0
# 0 0 0 1
# 1 1 1 1
# C

# Output:
# C B A C
# Z Y X W
# V U T D
# E F G H






