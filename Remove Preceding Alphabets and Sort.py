# Remove Preceding Alphabets and Sort
# The program must accept N string values containing only lower case alphabets as the input. All string values start with the same alphabet, but a certain number (possibly 0) of other alphabets appear before each string value. The program must remove those alphabets before each string, then the program must print the string values in sorted order.
# Note: There will be exactly one common character in the given N string values.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Length of each string <= 100

# Input Format:
# The first line contains N.
# The next N lines, each contains N string values separated by a space.

# Output Format:
# The first N lines contain the string values in sorted order.

# Example Input/Output 1:
# Input:
# 5
# pqreight
# cdgelephant
# xyeat
# abeagle
# hijklegg

# Output:
# eagle
# eat
# egg
# eight
# elephant

# Explanation:
# Here N=5.
# After removing the extra alphabets before each string, the string values become
# eight
# elephant
# eat
# eagle
# egg

# So the 5 string values are printed in sorted order.
# eagle
# eat
# egg
# eight
# elephant

# Example Input/Output 2:
# Input:
# 4
# abafruit
# egfrog
# kfood
# oipfish

# Output:
# fish
# food
# frog
# fruit




n=int(input())
arr=[input().strip() for _ in range(n)]
new=[]
ch=''
x=str(arr[0])
for c in list(x):
    flag=True
    for i in arr:
        if c not in list(str(i)): 
            flag = False
    if flag:
        ch=c
for i in arr:
    new.append(i[i.index(ch):])
print(*sorted(new),sep='\n')