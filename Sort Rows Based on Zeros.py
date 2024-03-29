# Sort Rows Based on Zeros

# The program must accept an integer matrix of size RxC as the input. The program must print the positions of the rows sorted in ascending order based on the number of zeros. If more than one row have the same number of zeros then print those positions of rows in ascending order.

# Boundary Condition(s):
# 1 <= R, C <= 1000

# Input Format:
# The first line contains the values of R and C separated by a space.
# The next R lines contain C integers separated by space(s).

# Output Format:
# The first line contains R position of rows based on the given conditions.

# Example Input/Output 1:
# Input:
# 5 4
# 1 2 0 0
# 4 0 7 6
# 9 0 0 0
# 0 4 5 0
# 0 3 0 0

# Output:
# 2 1 4 3 5

# Explanation:
# The 1st row has 2 zeros.
# The 2nd row has 1 zero.
# The 3rd row has 3 zeros.
# The 4th row has 2 zeros.
# The 5th row has 3 zeros.
# The position of rows in sorted order are 2 1 4 3 5
# Hence the output is 2 1 4 3 5

# Example Input/Output 2:
# Input:
# 6 6
# 44 0 0 -78 77 0
# 98 0 25 -56 0 67
# 66 -21 13 0 73 51
# 0 -85 0 22 0 -92
# 36 14 85 46 41 0
# 69 98 0 95 93 37

# Output:
# 3 5 6 2 1 4









r,c = map(int,input().split())
mat = [input().split() for _ in range(r)]
org = mat.copy()
mat.sort(key = lambda x:x.count('0'))
for row in mat:
    print(org.index(row) + 1,end = ' ')