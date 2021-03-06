# N String Values - First & Last
# The program must accept N string values and an integer K as the input. The program must form a string S based on the following conditions.
# - The string S is formed by concatenating the first K characters from the string values present in the odd positions and the last K characters from the string values present in the even positions alternatively.
# - Once K characters are used from the string values, they must be removed from the string values.
# Similarly, the program must repeat the above processes until all the characters are removed from all the string values. If the number of characters in a string is less than K, then all the characters from the string must be used and removed from that string, and then the value of K must be incremented by 1.
# Finally, the program must print the string S as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Length of each string <= 100
# 1 <= K <= 20

# Input Format:
# The first line contains N.
# The next N lines, each contains a string value.
# The N+2nd line contains K.

# Output Format:
# The first line contains S.

# Example Input/Output 1:
# Input:
# 4
# skillrack
# coding
# pythonprogramming
# 2computers
# 4

# Output:
# skildingpythterslraccoonprocompukgrammin2g

# Explanation:
# The way in which the string S formed is given below.
# skil + ding + pyth + ters + lrac + co + onpro + compu + k + grammin + 2 + g
# Hence the output is
# skildingpythterslraccoonprocompukgrammin2g

# Example Input/Output 2:
# Input:
# 5
# basket
# pencil
# notebook
# himalayanmountain
# candies
# 3

# Output:
# bascilnotaincanketpenebountdieokayanmoshimal

# Explanation:
# The way in which the string S formed is given below.
# bas + cil + not + ain + can + ket + pen + ebo + unt + die + ok + ayanmo + s + himal
# Hence the output is
# bascilnotaincanketpenebountdieokayanmoshimal






n=int(input())
l=[input().strip() for i in range(n)]
k=int(input())
t=""
while True:
    for i in l:
        if i!="":
            break
    else:
        break 
    for i in range(n):
        if len(l[i])>=k:
            if i%2==0:
                t+=l[i][0:k]
                l[i]=l[i][k:]
            else:
                t+=l[i][-k:]
                l[i]=l[i][0:len(l[i])-k]
        else:
            t+=l[i]
            l[i]="" 
            k+=1 
print(t) 