# Minimum - Maximum in Subarrays
# The program must accept an integer array of size N and an integer K as the input. The program must find the maximum value in each subarray of size K in the given array. Then the program must print the minimum value among those maximum values as the output.

# Boundary Condition(s):
# 2 <= K <= N <= 10^4
# 1 <= Each integer value <= 10^8

# Input Format:
# The first line contains N and K separated by a space.
# The second line contains N integer values separated by a space.

# Output Format:
# The first line contains an integer representing the minimum value among the obtained maximum values.

# Example Input/Output 1:
# Input:
# 10 4
# 38 6 24 47 51 60 45 22 35 59

# Output:
# 47

# Explanation:
# Here N = 10 and K = 4.
# 1st subarray -> 38 6 24 47 -> Maximum = 47
# 2nd subarray -> 6 24 47 51 -> Maximum = 51
# 3rd subarray -> 24 47 51 60 -> Maximum = 60
# 4th subarray -> 47 51 60 45 -> Maximum = 60
# 5th subarray -> 51 60 45 22 -> Maximum = 60
# 6th subarray -> 60 45 22 35 -> Maximum = 60
# 7th subarray -> 45 22 35 59 -> Maximum = 59
# The minimum value among the obtained maximum values is 47.

# Example Input/Output 2:
# Input:
# 10 3
# 2 1 6 4 6 7 3 3 1 4

# Output:
# 3








n,k=map(int,input().split())
arr = list(map(int,input().split()))
ans = max(arr)
for i in range(n-k+1):
    ans=min([ans,(max(arr[i:i+k]))])
print(ans)