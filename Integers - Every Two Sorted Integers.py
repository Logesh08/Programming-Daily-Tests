# Integers - Every Two Sorted Integers
# The program must accept N unique integers as the input. The program must print N-1 lines of output based on the following conditions.
# - In the 1st line, the program must print the integers from the smallest integer to the second smallest integer.
# - In the 2nd line, the program must print the integers from the second smallest integer to the third smallest integer.
# - In the 3rd line, the program must print the integers from the third smallest integer to the fourth smallest integer.
# - Similarly, the program must print the integers in the remaining lines as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Each integer value <= 10^5

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.

# Output Format:
# The first N-1 lines, each contains the integer values separated by a space.

# Example Input/Output 1:
# Input:
# 5
# 30 50 10 20 40

# Output:
# 10 20
# 20 10 50 30
# 30 50 10 20 40
# 40 20 10 50

# Explanation:
# 1st line: The integers from the smallest integer to the second smallest integer are printed.
# 10 20

# 2nd line: The integers from the second smallest integer to the third smallest integer are printed.
# 20 10 50 30

# 3rd line: The integers from the third smallest integer to the fourth smallest integer are printed.
# 30 50 10 20 40

# 4th line: The integers from the fourth smallest integer to the fifth smallest integer are printed.
# 40 20 10 50

# Example Input/Output 2:
# Input:
# 8
# 75 60 16 67 99 64 19 87

# Output:
# 16 67 99 64 19
# 19 64 99 67 16 60
# 60 16 67 99 64
# 64 99 67
# 67 16 60 75
# 75 60 16 67 99 64 19 87
# 87 19 64 99











n=int(input())
arr=(list(map(int,input().split())))
new=sorted(arr)
for i in range(n-1):
    start = arr.index(new[i])
    end = arr.index(new[i+1])
    print(*arr[start:end+1] if start<end else arr[end:start+1][::-1])
