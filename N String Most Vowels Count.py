# N String Most Vowels Count
# N strings are passed as input. The program must print the string with maximum vowels count. If more than one string have the maximum vowels count then print the first occurring string.

# Boundary Condition(s):
# 2 <= Length of String <= 1000
# 1 <= N <= 1000

# Input Format:
# The first line contains N.
# The next N lines contain a string value each.

# Output Format:
# The first line contains the string with most vowel count.

# Example Input/Output 1:
# Input:
# 3
# disk
# australia
# diego

# Output:
# australia

# Example Input/Output 2:
# Input:
# 5
# think
# better
# mockery
# implementation
# indigenous

# Output:
# implementation











n=int(input()) 
arr=[]
for _ in range(n):
    arr.append(input().strip()) 
def getCount(s):
    count=0
    for i in "aeiouAEIOU":
        count+=s.count(i)
    return count 
print(sorted(arr,key=lambda x:(-getCount(x),arr.index(x)))[0])