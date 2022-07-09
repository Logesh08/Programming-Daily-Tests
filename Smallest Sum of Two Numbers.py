# Smallest Sum of Two Numbers
# Accept an array of numbers with size N. The program must print the smallest sum of two numbers as the ouput.

# Boundary Condition(s):
# 2 <= N <= 30

# Input Format:
# The first line contains the value of N.
# The second line contains the N integers separated by space(s).

# Output Format:
# The first line contains the smallest sum value.

# Example Input/Output 1:
# Input:
# 4
# 1 2 5 9

# Output:
# 3

# Explanation:
# Here, sum of (1+2=3) is the smallest value by adding the pair elements in the given array of numbers.

# Example Input/Output 2:
# Input:
# 3
# 24 56 22

# Output:
# 46






input()
arr = sorted(list(map(int,input().split())))
print(arr[0]+arr[1])
