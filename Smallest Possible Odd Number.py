# Smallest Possible Odd Number

# The program must accept two numbers N1 and N2 as input. The program must print the smallest possible odd number by combining all the digits from both the numbers N1 and N2 as the output. If there is no odd digit in N1 and N2, then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= N1, N2 <= 999999999

# Input Format:
# The first line contains two numbers N1 and N2 separated by space.

# Output Format:
# The first line contains the smallest possible odd number by combining the digits from both the numbers N1 and N2.

# Example Input/Output 1:
# Input:
# 1100 300

# Output:
# 1000013

# Example Input/Output 2:
# Input:
# 87 44

# Output:
# 4487








a,b=input().split()
s = list(a+b)
try:
    lOdd = sorted([c for c in s if int(c)%2])[-1]
except:
    print(-1)
    exit()
s.remove(lOdd)
s = sorted(s)
i = 0
while s[0]=="0":
    s[0],s[i+1] = s[i+1],"0"
    i += 1
print(''.join(s)+lOdd)