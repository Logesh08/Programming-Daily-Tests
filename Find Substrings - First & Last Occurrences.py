# Find Substrings - First & Last Occurrences
# The program must accept N string values as the input. The program must print the output based on the following conditions.
# - For each string, the program must mark the first occurrence of the last letter of the current string in the next string. If the last letter is not present, then mark the first letter in the next string. Consider the first string as the next string of the Nth string.
# - For each string, the program must mark the last occurrence of the first letter of the current string in the previous string. If the first letter is not present, then mark the last letter in the previous string. Consider the Nth string as the previous string of the first string.
# - Then the program must print the letters between the two positions marked on each string(both inclusive).

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Length of each string <= 100

# Input Format:
# The first line contains N.
# The next N lines, each contains a string value.

# Output Format:
# The first N lines, each contains a string value based on the given conditions.

# Example Input/Output 1:
# Input:
# 4
# jungle
# notebook
# king
# poem

# Output:
# jun
# ebook
# king
# poem

# Explanation:
# First occurrence of last letter:
# jungle -> j (m is the last letter of poem which is not present in jungle. So the first letter is marked)
# notebook -> e (e is the last letter of jungle)
# king -> k (k is the last letter of notebook)
# poem -> p (g is the last letter of king which is not present in poem. So the first letter is marked)

# Last occurrence of first letter:
# jungle -> n (n is the first letter of notebook)
# notebook -> k (k is the first letter of king)
# king -> g (p is the first letter of poem which is not present in king. So the last letter is marked)
# poem -> m (j is the first letter of jungle which is not present in poem. So the last letter is marked)

# In each string, the letters that occur between the two positions marked(both inclusive) are printed.
# Hence the output is
# jun
# ebook
# king
# poem

# Example Input/Output 2:
# Input:
# 5
# umbrella
# mango
# achoko
# coconut
# task

# Output:
# um
# a
# cho
# oconut
# task









n=int(input())
arr=[]
for i in range(n):
    arr.append(input().strip())
for i in range(n):
    if i==0:
        x = arr[-1][-1]
        y = arr[i+1][0]
    elif i==n-1:
        x = arr[i-1][-1]
        y = arr[0][0]
    else:
        x = arr[i-1][-1]
        y = arr[i+1][0]
    if x not in arr[i]: x=arr[i][0]
    if y not in arr[i]: y=arr[i][-1]
    c=arr[i]
    cpp=c[::-1]
    ixy= (len(cpp)-cpp.index(y))
    mow = c.index(x)
    if mow > ixy : 
        mow,ixy=ixy-1,mow+1
    print(c[mow:ixy])