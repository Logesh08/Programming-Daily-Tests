# Combinations - Only Consonants
# The program must accept a string S containing only alphabets as the input. The program must print all the combinations containing only the consonants of the minimum length 2 as the output. The combinations must be printed in the order as shown in the Example Input/Output section. If there is no such combination, then the program must print -1 as the output.

# Boundary Condition(s):
# 2 <= Length of S <= 15

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains C.

# Example Input/Output 1:
# Input:
# cat

# Output:
# ct

# Explanation:
# Here S = cat.
# The 7 possible combinations are c, a, ca, t, ct, at and cat.
# ct is the only combination formed by the consonants whose length is 2.

# Example Input/Output 2:
# Input:
# CROW

# Output:
# CR
# CW
# RW
# CRW

# Example Input/Output 3:
# Input:
# aeiouAEIOU

# Output:
# -1

# Example Input/Output 4:
# Input:
# pqrs

# Output:
# pq
# pr
# qr
# pqr
# ps
# qs
# pqs
# rs
# prs
# qrs
# pqrs







# from itertools import combinations
# s = input().strip()
# v='aeiouAEIOU'
# l  = len(s)
# printed = False
# arr = []
# for i in range(l):
#     for j in range(i+1,l):
#         if s[i] not in v and s[j] not in v:
#             if s[i] not in arr:
#                 arr.append(s[i])
#             if s[j] not in arr:
#                 arr.append(s[j])
# for i in range(2,len(arr)+1):
#     for i in (list(combinations(arr,i))):
#         print(''.join(i))
#         printed = True
# if not printed:
#     print(-1)

l=[x for x in input().strip() if x not in "aeiouAEIOU"]
if len(l)<2:
    print(-1)
    quit()
else:
    for i in range(3,2**(len(l))):
        t=i
        if((i & (~(i-1)))==i):
            continue
        for j in l:
            if t%2==1:
                print(j,end="")
            t//=2
        print()