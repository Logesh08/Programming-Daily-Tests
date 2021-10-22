# Matrix - Characters between Diagonals
# The program must accept a character matrix of size R*C as the input. The program must print the matrix based on the following conditions.
# - If R and C are equal, then the program must print the characters in the top-left to bottom-right diagonal. The remaining characters must be printed as asterisks.
# - Else the program must print the characters between the diagonals D1 and D2 (both inclusive). D1 is a diagonal which starts from the top-left cell and ends at the right edge(when R > C) or bottom edge(when R < C) of the matrix. D2 is a diagonal which starts from the bottom-right cell and ends at the left edge(when R > C) or top edge(when R < C) of the matrix. The remaining characters must be printed as asterisks.

# Boundary Condition(s):
# 2 <= R, C <= 50

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C characters separated by a space.

# Output Format:
# The first R lines contain the matrix based on the given conditions.

# Example Input/Output 1:
# Input:
# 9 5
# g k t u l
# h u n p l
# s t t s m
# k y j l c
# a k z a e
# k y r q h
# z b p g f
# v a k l k
# f h l y h

# Output:
# g * * * *
# h u * * *
# s t t * *
# k y j l *
# a k z a e
# * y r q h
# * * p g f
# * * * l k
# * * * * h

# Explanation:
# Here R = 9 and C = 5 (R > C).
# The diagonal D1 is highlighted below.
# g k t u l
# h u n p l
# s t t s m
# k y j l c
# a k z a e
# k y r q h
# z b p g f
# v a k l k
# f h l y h

# The diagonal D2 is highlighted below.
# g k t u l
# h u n p l
# s t t s m
# k y j l c
# a k z a e
# k y r q h
# z b p g f
# v a k l k
# f h l y h

# Hence the characters between the diagonals D1 and D2(both inclusive) are printed. The remaining characters are printed as asterisks.
# g * * * *
# h u * * *
# s t t * *
# k y j l *
# a k z a e
# * y r q h
# * * p g f
# * * * l k
# * * * * h

# Example Input/Output 2:
# Input:
# 4 9
# e i l u u x f c w
# w d f s m n d l h
# x z y h f v b o f
# j n p u k n d i r

# Output:
# e i l u u x * * *
# * d f s m n d * *
# * * y h f v b o *
# * * * u k n d i r

# Example Input/Output 3:
# Input:
# 4 4
# z B z G
# S H C G
# A C G o
# J o v m

# Output:
# z * * *
# * H * *
# * * G *
# * * * m





def copy_mat(x, y):
    while x < r and y < c:
        m1[x][y] = m[x][y]
        x += 1
        y += 1
r, c = map(int, input().split())
m = [input().split() for i in range(r)]
m1 = [['*'] * c for i in range(r)]
if r > c:
    for i in range(0, r - c + 1):
        copy_mat(i, 0)
else:
    for j in range(0, c - r + 1):
        copy_mat(0, j)
for i in m1:
    print(*i)