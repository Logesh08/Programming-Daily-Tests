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













# method 1
x = int(input())
y = [list(map(int,input().split())) for i in range(x)]

t = []
c = 0
for i in y:
    p = [i]
    for j in range(1, 25):
        p.append([i[0]+j, i[1]])
        p.append([i[0]+j, i[1]-j])
        p.append([i[0], i[1]-j])
        d = True
        for k in p:
            if k not in y:
                d = False
        if d and sorted(p) not in t:
            # if x==12:
            #     print(p)
            t.append(sorted(p))
            c += 1
        p=[i]
print(c)






# method 2
n=int(input())
l=sorted(set([tuple(map(int,input().split())) for i in range(n)]))
n=len(l)
o=set()
for i in range(n):
    for j in range(i+1,n):
        if l[i][0]==l[j][0]:
            t=l[j][1]-l[i][1]
            if (l[i][0]+t,l[i][1]) in l and (l[i][0]+t,l[i][1]+t) in l:
                o.add(tuple(l[i]+l[j]))
print(len(o))