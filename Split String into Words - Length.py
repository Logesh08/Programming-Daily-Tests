# Split String into Words - Length
# The program must accept an integer N, a string S and N integers as the input. The string S contains N words without any space. The N integers represent the length of words in the string S. The program must sort the words in the string S based on their length. If two or more words have the same length, then the program must sort those words in the order of their occurrence. Finally, the program must print the revised string S as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 2 <= Length of S <= 10^4
# 1 <= Each integer value <= 100

# Input Format:
# The first line contains N.
# The second line contains S.
# The third line contains N integers separated by a space.

# Output Format:
# The first line contains the revised string S.

# Example Input/Output 1:
# Input:
# 4
# lioncattigerrat
# 4 3 5 3

# Output:
# catratliontiger

# Explanation:
# There are 4 words in the given string.
# 4 -> lion
# 3 -> cat
# 5 -> tiger
# 3 -> rat
# After sorting the words based on their length, the string S becomes
# catratliontiger

# Example Input/Output 2:
# Input:
# 7
# applegrapesmangocuckooPineappleNoodlesPizza
# 5 6 5 6 9 7 5

# Output:
# applemangoPizzagrapescuckooNoodlesPineapple







n = int(input())
s=input().strip()
arr = list(map(int,input().split()))
new = []
t=""
cur = arr.pop(0)
now = 1
for i in s:
    t+=i
    if now == cur:
        new.append(t)
        try:
            cur = arr.pop(0)
        except:
            break
        now = 0
        t=""
    now += 1
print(*sorted(new,key = len),sep="")