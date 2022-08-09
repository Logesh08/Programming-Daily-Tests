# Left Rotation of Numbers

# The program must accept a list of integers and a list of rotation count as input. The program must print the rotated integers (anti-clockwise) as output.

# Boundary Condition(s):
# 1 <= Size of the integers list <= 30
# 1 <= Size of the rotations list <= 16

# Input Format:
# The first line contains the list of integers separated by space(s).
# The second line contains the list of rotations separated by space(s).

# Output Format:
# The list of lines contain the rotated integers.

# Example Input/Output 1:
# Input:
# 1 2 3 4 5
# 1 2 3

# Output:
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3

# Example Input/Output 2:
# Input:
# 45 67 89
# 3 4

# Output:
# 45 67 89
# 67 89 45






arr = input().split()
rotation = input().split()
for i in rotation:
    i=int(i); i%=len(arr)
    print(*arr[i:len(arr)]+arr[:i])