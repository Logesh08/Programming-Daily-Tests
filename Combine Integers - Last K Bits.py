# Combine Integers - Last K Bits
# The program must accept N integers and an integer K as the input. The program must combine the consecutive integers by adding only if they have the same last K bits. Then the program must print the resulting integer values as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Each integer value <= 10^8
# 1 <= K <= 30

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.
# The third line contains K.

# Output Format:
# The first line contains the integer values separated by a space based on the given conditions.

# Example Input/Output 1:
# Input:
# 8
# 45 101 13 38 30 42 47 215
# 3

# Output:
# 159 68 42 262

# Explanation:
# 45 -> 101101
# 101 -> 1100101
# 13 -> 1101
# 38 -> 100110
# 30 -> 11110
# 42 -> 101010
# 47 -> 101111
# 215 -> 11010111
# 1st, 2nd and 3rd integers can be combined as 159 (45+101+13).
# 4th and 5th integers can be combined as 68 (38+30).
# 6th integer cannot be combined with other integers. So 42 remains the same.
# 7th and 8th integers can be combined as 262 (47+215).
# Hence the output is
# 159 68 42 262

# Example Input/Output 2:
# Input:
# 4
# 13 87 99 25
# 1

# Output:
# 224









input()
arr=list(map(int,input().split()))
k=int(input())
s=int(bin(arr[0])[-k:])
e=arr[0]
for i in arr[1:]:
    t = int(bin(i)[-k:])
    if t == s:
        e += i 
    else:
        print(e,end=' ')
        e = i
        s = t
print(e)

