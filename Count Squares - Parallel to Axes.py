# Count Squares - Parallel to Axes
# The program must accept the coordinates (x, y) of N points on a graph as the input. The program must print the number of squares that can be formed parallel to the axes as the output.
# Note: Ignore the duplicate coordinates when finding the squares.

# Boundary Condition(s):
# 4 <= N <= 500
# -10 <= x, y <= 10

# Input Format:
# The first line contains N.
# The next N lines, each contains the coordinates(x, y) of a point on a graph.

# Output Format:
# The first line contains the number of squares that can be formed parallel to the axes.

# Example Input/Output 1:
# Input:
# 5
# 0 0
# 0 2
# 2 2
# 1 1
# 2 0

# Output:
# 1

# Explanation:
# The only square is formed using the points (0, 0), (0, 2), (2, 2) and (2, 0).

# Example Input/Output 2:
# Input:
# 13
# -2 2
# -1 2
# -2 1
# -1 1
# 2 2
# 1 1
# -1 -1
# 1 -1
# -1 -2
# 2 -2
# -2 -2
# 1 -2
# 0 0

# Output:
# 4

# Explanation:
# The four squares are formed using the below coordinates.
# Square 1: (-2, 2), (2, 2), (2, -2) and (-2, -2).
# Square 2: (-2, 2), (-1, 2), (-1, 1) and (-2, 1).
# Square 3: (-1, 1), (1, 1), (1, -1) and (-1, -1).
# Square 4: (-2, 1), (1, 1), (-2, -2) and (1, -2).

# Example Input/Output 3:
# Input:
# 12
# 2 -2
# -2 2
# 1 -1
# -2 -2
# 1 1
# -2 -2
# 2 2
# -1 -1
# 2 -2
# -1 1
# 2 2
# -2 2

# Output:
# 2














n = int(input())
cords = [list(map(int,input().split())) for _ in range(n)]
ans = []
def findSqares(x,y,formed):
    if len(formed)==4:
        if sorted(formed) not in ans:
            ans.append(sorted(formed))
        return
    for i in cords:
        if i not in formed:
            if i[0]==x:
                formed.append(i)
                findSqares(x,i[1],formed)
            if i[1]==y:
                formed.append(i)
                findSqares(i[0],y,formed)
            
    
for i in range(n):
    cur = cords[i]
    x,y = cur[0], cur[1]
    findSqares(x,y,[cur])
    
print(len(ans))
