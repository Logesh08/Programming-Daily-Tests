# Count of Concatenated Multiples

# The program must accept an integer array of size N and an integer X as the input. The program must print the count of pairs in the array such that the concatenation(s) of two integers in the pair is a multiple of X. For example, the concatenations of 25 and 40 are 2540 and 4025.
# Note: A pair cannot be formed with the integer at the same position in the array.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= X <= 999

# Input Format:
# The first line contains the value of N and X separated by space(s).
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains the count of pairs which are the multiples of X.

# Example Input/Output 1:
# Input:
# 5 11
# 45 1 10 12 11

# Output:
# 7

# Explanation:
# There are 7 pairs which produce the multiples of 11. They are
# (45, 1)  -> 451
# (45, 10) -> 4510
# (10, 45) -> 1045
# (1, 10)  -> 110
# (12, 1)  -> 121
# (10, 12) -> 1012
# (12, 10) -> 1210
# Hence the output is 7

# Example Input/Output 2:
# Input:
# 3 12
# 12 12 11

# Output:
# 2








n,x=map(int,input().split())
arr = input().split()
count = 0
for i in range(n):
    for j in range(i+1,n):
        if int(arr[i]+arr[j])%x==0:
            count += 1
        if int(arr[j]+arr[i])%x==0:
            count += 1
print(count)