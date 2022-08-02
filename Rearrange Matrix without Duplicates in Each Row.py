# Rearrange Matrix without Duplicates in Each Row

# The program must accept an integer matrix of size RxC as input. The program must print YES if the given matrix can be rearranged in such a way that each row must not contain any duplicate values. Else the program must print NO as the output.

# Boundary Condition(s):
# 1 <= R, C <= 50
# 0 <= Matrix Elements <= 999999

# Input Format:
# The first line contains the value of R and C separated by space(s).
# The next R lines contain C integers separated by space(s).

# Output Format:
# The first line contains either YES or NO.

# Example Input/Output 1:
# Input: 
# 3 3
# 4 4 5 
# 5 6 7 
# 7 5 7 

# Output: 
# YES

# Explanation:
# One of the possible rearrangements,
# 4 5 7
# 4 5 7
# 6 5 7
# There is no repeated integer in each row.

# Example Input/Output 2:
# Input:
# 4 3
# 4 4 4
# 5 5 7
# 7 7 5
# 4 7 7

# Output:
# NO

# Explanation:
# One of the possible rearrangements,
# 4 5 7
# 4 5 7
# 4 5 7
# 4 7 7
# In the rearranged matrix, 7 is repeated within the last row.








r,c=map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(r)]
arr = []
for row in mat:
    for val in row:
        arr.append(val)
print(arr)
for i in set(arr):
    if arr.count(i)>c:
        print('NO')
        exit()
print('YES')