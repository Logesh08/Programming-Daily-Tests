# Remove Largest N Columns

# The program must accept an integer matrix of size RxC as input. The program must remove the largest N columns(based on column sum). Finally, the program must print the matrix.

# Boundary Condition(s):
# 1 <= R, C <= 50
# 1 <= N < C

# Input Format:
# The first line contains the values of R and C separated by a space.
# The next R lines contain C integers each separated by space(s).
# The R+2th line contains the value of N.

# Output Format:
# The first R lines contain C-N integers each separated by a space.

# Example Input/Output 1:
# Input:
# 3 3
# 5 6 1 
# 4 9 2 
# 8 3 7 
# 1

# Output:
# 5 1
# 4 2
# 8 7

# Explanation :
# The sum of the first column is (5+4+8) 17
# The sum of the second column is (6+9+3) 18
# The sum of the third column is (1+2+7) 10
# The value of N is 1, hence the second column alone is removed
# After removing the second column remaining columns are printed.

# Example Input/Output 2:
# Input:
# 4 3
# 4 8 9 
# 5 7 4
# 8 9 5
# 2 3 7
# 2

# Output:
# 4
# 5
# 8
# 2
 






r,c = map(int,input().split())
mat = (list(map(list,zip(*[list(map(int,input().split())) for _ in range(r)]))))
n = int(input())
for i in range(n):
    mat.remove(sorted(mat,key=sum)[-1])
for row in list(map(list,zip(*mat))):
    print(*row)