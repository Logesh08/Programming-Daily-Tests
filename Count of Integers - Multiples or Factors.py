# Count of Integers - Multiples/Factors
# The program must accept N integers. The program must print the count of integers which have other integers (among these N integers) having a different value as their multiple or as their factors.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= Each integer value <= 10^5

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.

# Output Format:
# The first line contains an integer value.

# Example Input/Output 1:
# Input:
# 5
# 10 5 70 10 4

# Output:
# 4

# Explanation:
# 10 has 5 as its factor as well as 70 as its multiple.
# 5 has 10 and 70 as its multiple.
# 70 has 5 and 10 as its factors.
# 10 has 5 as its factor as well as 70 as its multiple.
# 4 has no factors and no multiples.
# So 4 integers meet the conditions given.

# Example Input/Output 2:
# Input:
# 5
# 10 10 10 10 10

# Output:
# 0



n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(n):
    t=arr[i]
    for j in arr:
        if (j %t==0 or t%j==0)and j!=t:
            count+=1
            break
print(count)
