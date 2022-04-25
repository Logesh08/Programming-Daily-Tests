
# Add Two Integers - Form K
# The program must accept N integers and an integer K as the input. The program must calculate and print the number of ways W to form the integer K by adding two integers among N integers as the output. Also, the sign of the integers can be changed to form K.

# Boundary Condition(s):
# 2 <= N <= 1000
# 2*(-10^5) <= K <= 2*(10^5)
# -10^5 <= Each integer value <= 10^5

# Input Format:
# The first line contains N and K separated by a space.
# The second line contains N integers separated by a space.

# Output Format:
# The first line contains an integer representing the number of ways to form K based on the given conditions.

# Example Input/Output 1:
# Input:
# 3 5
# -2 3 -3

# Output:
# 2

# Explanation:
# The 2 possible ways are given below.
# -2 and -3 = 2+3 = 5
# -2 and 3 = 2+3 = 5

# Example Input/Output 2:
# Input:
# 5 -3
# -1 -2 2 1 4

# Output:
# 6

# Explanation:
# The 6 possible ways are given below.
# -1 and -2 = (-1)+(-2) = -3
# -1 and 2 = (-1)+(-2) = -3
# -1 and 4 = 1+(-4) = -3
# -2 and 1 = (-2)+(-1) = -3
# 2 and 1 = (-2)+(-1) = -3
# 1 and 4 = 1+(-4) = -3















n,k=map(int,input().split())
arr = list(map(int,input().split()))
ways = 0
for i in range(n):
    for j in range(i+1,n):
        if -(arr[i]) + -(arr[j]) == k:
            ways+=1 
        elif arr[i] + arr[j] == k:
            ways+=1 
        elif -(arr[i]) + arr[j] == k:
            ways+=1 
        elif arr[i] + -(arr[j]) == k:
            ways+=1 
print(ways)