# Matrix - Missing Digits Sorted Order
# The program must accept a matrix of size RxC containing only digits as the input.
# Each 3x3 submatrix in the given matrix contains 9 unique digits(1 - 9), but some digits are missing.
# The missing digits are denoted by hyphens. The program must find those missing digits in each 3x3 submatrix and replace the hyphens with the missing digits in sorted order. 
# Finally, the program must print the revised matrix as the output.
# Note: The values of R and C are always divisible by 3.

# Boundary Condition(s):
# 3 <= R, C <= 48

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines contain the matrix.

# Output Format:
# The first R lines contain the revised matrix.

# Example Input/Output 1:
# Input:
# 9 6
# 5 7 1 8 4 -
# - 9 - - 6 2
# 4 3 6 - 3 -
# 8 - 5 8 - 9
# 2 4 3 - - 1
# 6 - - 5 6 7
# 6 3 2 1 4 -
# - 5 - 3 5 9
# 7 4 8 6 - -

# Output:
# 5 7 1 8 4 1
# 2 9 8 5 6 2
# 4 3 6 7 3 9
# 8 1 5 8 2 9
# 2 4 3 3 4 1
# 6 7 9 5 6 7
# 6 3 2 1 4 2
# 1 5 9 3 5 9
# 7 4 8 6 7 8

# Explanation:
# Here R = 9 and C = 6
# After replacing the hyphens in each 3x3 submatrix with the missing digits in sorted order, the matrix becomes
# 5 7 1 8 4 1
# 2 9 8 5 6 2
# 4 3 6 7 3 9
# 8 1 5 8 2 9
# 2 4 3 3 4 1
# 6 7 9 5 6 7
# 6 3 2 1 4 2
# 1 5 9 3 5 9
# 7 4 8 6 7 8




R , C = map(int,input().split())
matrix = [list(map(str,input().split())) for _ in range(R)]
for row in range(0,R,3):
    for col in range(0,C,3):
        missing = []
        nums = list("123456789")
        for subRow in range(row,row+3):
            for subCol in range(col,col+3):
                if matrix[subRow][subCol] in nums:
                    nums[nums.index(matrix[subRow][subCol])] = '*'
        nums = [ele for ele in nums if ele != '*']
        index = 0
        for subRow in range(row,row+3):
            for subCol in range(col,col+3):
                if matrix[subRow][subCol] == '-':
                    matrix[subRow][subCol] = nums[index]
                    index+=1
for row in matrix:
    print(*row)