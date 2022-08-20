# Rotate Every N Elements for K Times

# The program must accept an integer array of size M and two integers N and K as the input. The program must rotate every N elements (in anti-clockwise direction) in the array for K times. If the last part of the array contains less than N elements then rotate the remaining element left at the last for K times. Finally, the program must print the modified array as the output.

# Boundary Condition(s):
# 1 <= M <= 100
# 1 <= N <= N
# 1 <= K <= 99999

# Input Format:
# The first line contains the value of M.
# The second line contains M integers separated by space(s).
# The third line contains the values of N and K separated by a space.

# Output Format:
# The first line contains the modified array integers separated by space(s).

# Example Input/Output 1:
# Input:
# 10
# 71 65 74 88 63 100 45 35 67 11
# 4 1

# Output:
# 65 74 88 71 100 45 35 63 11 67

# Explanation:
# 71 65 74 88 63 100 45 35 67 11
# Here every 4 elements must be rotated 1 time.
# 71 65 74 88 is rotated as  65 74 88 71
# 63 100 45 35 is rotated as  100 45 35 63
# The last part of the array do not have 4 elements so the remaining elements must be rotated 1 time.
# So 67 11 is rotated as 11 67

# Example Input/Output 2:
# Input:
# 9
# 98 40 55 61 43 30 3 65 61
# 3 4

# Output:
# 40 55 98 43 30 61 65 61 3







m = int(input())
arr = input().split()
n,k=map(int,input().split())
for i in range(0,m,n):
    cur = arr[i:i+n]
    r = k % len(cur)
    print(*cur[r:]+cur[:r],end=' ')