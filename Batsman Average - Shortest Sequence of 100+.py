# Batsman Average - Shortest Sequence of 100+
# The program must accept N integers representing the runs scored by a batsman in N matches. The program must find the shortest sequence of 100+ scores(consecutive 100+ scores) by the batsman. If two or more sequences of 100+ scores are of the same shortest length, then the program must consider the last sequence. Finally, the program must print the average score of the batsman in that shortest sequence as the output. The average score must be printed with the precision up to 2 decimal places.
# Note: There will be at least one 100+ score in N matches.

# Boundary Condition(s):
# 1 <= N <= 1000
# 1 <= Each integer value <= 500

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space representing the runs scored by the batsman in N matches.

# Output Format:
# The first line contains the average score of the batsman in that shortest sequence of 100+ scores.

# Example Input/Output 1:
# Input:
# 14
# 4 7 74 190 157 80 114 192 115 196 110 20 186 146

# Output:
# 166.00

# Explanation:
# 1st sequence of 100+ scores: 190 157
# 2nd sequence of 100+ scores: 114 192 115 196 110
# 3rd sequence of 100+ scores: 186 146
# There are two shortest sequences of 100+ scores: 1st and 3rd.
# The average score in the 3rd sequence(last shortest) is 166.00, which is printed as the output.

# Example Input/Output 2:
# Input:
# 12
# 72 173 190 122 29 160 100 213 363 99 100 101

# Output:
# 100.50



n=int(input())
arr=list(map(int,input().split()))
ans=[]
t=[]
flag=False
for i in arr:
    if i>=100:
        t.append(i)
        flag=True
    elif flag:
        flag=False
        ans.append(t)
        t=[]
if flag:
    ans.append(t)
ans.sort(key = lambda x:len(x))
answer=[row for row in ans if len(row)==len(ans[0])]
print("%.2f"%(sum(answer[-1])/len(answer[-1])))
