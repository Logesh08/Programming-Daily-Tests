# City Missiles
# There are N cities arranged in a row and each city has a missile that will destroy another city to its left or right. The program must accept N pairs of integers(X, Y) as the input. The value of X indicates the position of a city. The value of Y indicates the number of positions that the missile can travel. The sign of Y indicates the direction in which the missile can travel. The program must print "YES" if there are any two cities which can destroy each other. Else the program must print "NO" as the output.

# Boundary Condition(s):
# 2 <= N <= 1000
# -1000 <= X <= 1000
# -1000 <= Y <= 1000 (where Y != 0)

# Input Format:
# The first line contains N.
# The next N lines, each contains 2 integers X and Y separated by a space.

# Output Format:
# The first line contains YES or NO.

# Example Input/Output 1:
# Input:
# 2
# 3 2
# 5 -2

# Output:
# YES

# Explanation:
# The position of the 1st city is 3. The missile from the 1st city can travel 2 positions to its right.
# The position of the 2nd city is 5. The missile from the 2nd city can travel 2 positions to its left.
# The missile from the 1st city can destroy the 2nd city.
# Similarly, the missile from the 2nd city can destroy the 1st city.
# Hence YES is printed as the output.

# Example Input/Output 2:
# Input:
# 3
# -4 3
# 2 -3
# 0 5

# Output:
# NO

# Explanation:
# The position of the 1st city is -4. The missile from the 1st city can travel 3 positions to its right.
# The position of the 2nd city is 2. The missile from the 2nd city can travel 3 positions to its left.
# The position of the 3rd city is 0. The missile from the 3rd city can travel 5 positions to its right.
# The missile from the 1st city can destroy the position -1 (no city at the position -1).
# The missile from the 2nd city can destroy the position -1 (no city at the position -1).
# The missile from the 3rd city can destroy the position 5 (no city at the position 5)
# There are no two cities that can destroy each other.
# Hence NO is printed as the output.









n=int(input())
x=[]
y=[]
arr=[]
for _ in range(n):
    m = input().split()
    arr.append(m)
    x.append(int(m[0]))
    y.append(int(m[1]))

for i in arr:
    a = int(i[0])
    b = int(i[1])
    if a+b in x:
        if(b+y[x.index(a+b)])==0:
            print('YES')
            exit()
print('NO')  