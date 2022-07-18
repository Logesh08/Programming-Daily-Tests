# Sum of Traversed Integers in Matrix

# The program must accept an integer matrix of size R*C as input. The program must traverse the matrix starting from the top left position to the rightmost column of the matrix (any row). For any position in the matrix, the allowed move is to go to the next column in the same row or one row above in the next column or one row below in the next column. Always choose the maximum value in these three possible positions (provided the positions exist in the matrix). The program must print the sum of traversed integers. If more than one row has the same maximum value, then choose the first occurring row from the top.

# Boundary Condition(s):
# 1 <= R, C <= 50

# Input Format:
# The first line contains the value of R and C separated by space(s).
# The next R lines contain C integers separated by space.

# Output Format:
# The first line contains the sum of traversed integers.

# Example Input/Output 1:
# Input:
# 3 3
# 2 55 40
# 1 58 30
# 3 23 20

# Output:
# 100

# Explanation:
# In the first column, the top left element is 2.
# In the second column, 58 is greater than 55. So, 58 is added with 2 (2 + 58 = 60).
# In the third column, 40 is greater than 30 and 20. So, 40 is added with 60 (60 + 40 = 100).
# The last column is reached. Hence, 100 is printed as output.

# Example Input/Output 2:
# Input:
# 3 5
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15

# Output:
# 50