# Print Ranges - Array
# The program must accept N integers and print the unique ranges in ascending order.

# Boundary Condition(s):
# 1 <= N <= 1000
# 0 <= Each integer value <= 1000

# Input Format:
# The first line contains N.
# The second line contains N integers separated by a space.

# Output Format:
# The first line contains the ranges separated by a space.

# Example Input/Output 1:
# Input:
# 8
# 4 6 1 9 7 0 2 3

# Output:
# 0-4 6-7 9-9

# Explanation:
# The integers in the range 0-4 are 0, 1, 2, 3 and 4.
# The integers in the range 6-7 are 6 and 7.
# The only integer in the range 9-9 is 9.

# Example Input/Output 2:
# Input:
# 8
# 4 8 7 5 6 3 3 5

# Output:
# 3-8

# Example Input/Output 3:
# Input:
# 5
# 15 10 12 12 12

# Output:
# 10-10 12-12 15-15





input()

arr = sorted(list(set(map(int,input().split()))))
start = arr[0]
end = -1
for i in arr:
    if end==1:
        start = i
        end = -1
    if i+1 in arr:
        pass
    else:
        print(start,i,sep='-',end=' ')
        end=1