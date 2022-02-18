# Floor Sweeper - Maximum Area
# The program must accept a character matrix of size N*N representing the floor of a room as the input. Each hash symbol indicates that the area is clean. Each asterisk indicates that the area is dirty. A floor sweeper of length L is available to clean the room. The program must print the maximum number of dirty areas that can be cleaned in one sweep vertically or horizontally as the output.

# Boundary Condition(s):
# 2 <= N <= 50
# 1 <= L <= N

# Input Format:
# The first line contains N.
# The next N lines, each contains N characters separated by a space.
# The N+2nd line contains L.

# Output Format:
# The first line contains an integer representing the maximum number of dirty areas that can be cleaned in one sweep vertically or horizontally.

# Example Input/Output 1:
# Input:
# 5
# # * # * *
# * * * * #
# * # # * #
# * * # # *
# # # * # #
# 2

# Output:
# 7

# Explanation:
# Here N = 5 and L = 2.
# The maximum number of dirty areas that can be cleaned is 7 (by sweeping the first 2 rows horizontally).
# Hence 7 is printed as the output.

# Example Input/Output 2:
# Input:
# 6
# # # * # # #
# # * # * # *
# # # * # # #
# * * # # # #
# # * # # # #
# # # * * # *
# 3

# Output:
# 8









n=int(input())
mat = [input().split() for _ in range(n)]
l = int(input())
Max = 0 
for i in range(n-l+1):
    t = 0
    for k in range(l):
        for j in range(n):
            if mat[i+k][j]=="*":
               t+=1
        Max = max([Max,t])
for j in range(n-l+1):
    t=0
    for k in range(l):
        for i in range(n):
            if mat[i][j+k] =="*":
                t+=1
        Max = max([Max,t])
            
print(Max)