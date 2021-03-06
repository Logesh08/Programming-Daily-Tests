# Form List of Integers
# The program must accept N integers as the input. The program must form a list of integers based on the following conditions.
# - Initially, the list is empty.
# - For each integer X among the N integers, the program must add the integer X to the end of the list and then reverse the list.
# Finally, the program must print the integers in the list obtained as the output.

# HINT: Optimize your logic to avoid Time Limit Exceeded error.

# Boundary Condition(s):
# 1 <= N <= 10^5
# 1 <= Each integer value <= 10^9

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.

# Output Format:
# The first line contains N integer values separated by a space representing the integers in the list obtained.

# Example Input/Output 1:
# Input:
# 4
# 10 20 30 40

# Output:
# 40 20 10 30

# Explanation:
# Initially, the list is empty [].
# 1st integer: [] -> [10] -> [10].
# 2nd integer: [10] -> [10, 20] -> [20, 10].
# 3rd integer: [20, 10] -> [20, 10, 30] -> [30, 10, 20].
# 4th integer: [30, 10, 20] -> [30, 10, 20, 40] -> [40, 20, 10, 30].

# Example Input/Output 2:
# Input:
# 7
# 11 22 33 44 55 66 77

# Output:
# 77 55 33 11 22 44 66



ans=[]
n=int(input())
arr =  list(map(int,input().split()))
ans.append(arr[0])
for i in range(1,n):
    if i%2!=0:
        ans = [arr[i]]+ans
    else:
        ans.append(arr[i])
if n%2==0:
    print(*ans)
else:
    print(*ans[::-1])