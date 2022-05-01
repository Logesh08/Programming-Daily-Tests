# Remove Ranges - Overlaps
# The program must accept N ranges and a range X-Y as the input. The program must modify the N ranges by removing the integers in the given range X-Y. If all the integers in a range are removed, then the program must remove the entire range from the given ranges. If some integers in the middle of a range are removed, then the program must split the range into two by removing those integers. Finally, the program must print the remaining ranges in ascending order based on the start value S. If two or more ranges start with the same value, then the program must sort those ranges in ascending order based on the end value E. If no ranges remaining, then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= S <= E <= 1000
# 1 <= X <= Y <= 1000

# Input Format:
# The first line contains N.
# The second line contains N ranges separated by a space.
# The third line contains a range X-Y.

# Output Format:
# The lines contain the revised ranges or the first line contains -1 based on the given conditions.

# Example Input/Output 1:
# Input:
# 7
# 12-16 15-20 5-8 8-12 7-15 1-10 1-4
# 5-10

# Output:
# 1-4
# 1-4
# 11-12
# 11-15
# 12-16
# 15-20

# Explanation:
# Here the given range X-Y is 5-10.
# Range 1: The range 12-16 does not overlap with the given range 5-10.
# Range 2: The range 15-20 does not overlap with the given range 5-10.
# Range 3: The range 5-8 is within the given range 5-10. So the entire range 5-8 is removed.
# Range 4: The range 8-12 is overlapping with the given range 5-10. So the integers (8-10) are removed from the range 8-12. Now the range becomes 11-12.
# Range 5: The range 7-15 is overlapping with the given range 5-10. So the integers (7-10) are removed from the range 7-15. Now the range becomes 11-15.
# Range 6: The range 1-10 is overlapping with the given range 5-10. So the integers (5-10) are removed from the range 1-10. Now the range becomes 1-4.
# Range 7: The range 1-4 does not overlap with the given range 5-10.
# Hence the output is
# 1-4
# 1-4
# 11-12
# 11-15
# 12-16
# 15-20

# Example Input/Output 2:
# Input:
# 4
# 1-20 1-10 10-20 4-11
# 5-10

# Output:
# 1-4
# 1-4
# 4-4
# 11-11
# 11-20
# 11-20

# Example Input/Output 3:
# Input:
# 3
# 15-20 10-20 10-15
# 10-20

# Output:
# -1












input()
arr = input().split() 
s,e = map(int,input().split('-'))
ans = []
for r in arr:
    a,b=map(int,r.split('-'))
    if (a>=s and a<=e) or (b>=s and b<=e):
        if a>=s and a<=e:
            a = e+1
        if b>=s and b<=e:
            b = s-1
            
        if not (a==e+1 and b==s-1):
            ans.append([a,b])
    elif (a<s and b>=e) or (b>e and a<=s):
        ans.append([a,s-1])
        ans.append([e+1,b])
            
    else:
        if not (a==e+1 and b==s-1):
            ans.append([a,b])

if ans:
    ans = sorted(ans,key = lambda x: (x[0],x[1]))
    for i in ans:
        print(*i,sep='-')
else:
    print(-1)
    
    
