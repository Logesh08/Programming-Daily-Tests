# Transpose of Matrix

# Accept an integer matrix as the input. The program must print the transpose of the given matrix as the output.
# Note: Read the input carefully to avoid errors.

# Boundary Condition(s):
# 1 <= Number of rows and columns <= 100

# Input Format:
# The list of lines contain the elements of an integer matrix.

# Output Format:
# The list of lines contain the transpose of the given matrix.

# Example Input/Output 1:
# Input:
# 1 2 3
# 4 5 6
# 7 8 9

# Output:
# 1 4 7 
# 2 5 8 
# 3 6 9

# Example Input/Output 2:
# Input:
# 23 34 56 67 89
# 12 34 45 34 56
# 23 45 54 98 90

# Output:
# 23 12 23 
# 34 34 45 
# 56 45 54 
# 67 34 98 
# 89 56 90





mat = []
try:
    mat.append(input().split())
except:
    [print(*row) for row in list(zip(*mat))]