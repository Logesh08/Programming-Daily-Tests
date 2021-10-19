# Inverted Right Angle Triangles Pattern
# The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 2 <= N <= 50

# Input Format:
# The first line contains N.

# Output Format:
# The first N lines contain the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 3

# Output:
# *-*-*-*-*
# --*-*-*
# ----*

# Explanation:
# Here N=3, so the pattern contains 3 lines of output.
# Two inverted right-angle triangles are printed using asterisks.
# The hyphens in the pattern represent the empty spaces.

# Example Input/Output 2:
# Input:
# 5

# Output:
# *-*-*-*-*-*-*-*-*
# --*-----*-----*
# ----*---*---*
# ------*-*-*
# --------*

# Example Input/Output 3:
# Input:
# 6

# Output:
# *-*-*-*-*-*-*-*-*-*-*
# --*-------*-------*
# ----*-----*-----*
# ------*---*---*
# --------*-*-*
# ----------*





n=int(input())
k=n*2-1
t=['*']*k
r='-'.join(t) 
p=2
q=(n-2)*2-1
print(r)
for i in range(n-2):
  s='-'*p+'*'+'-'*q+"*"+'-'*q+'*'
  p=p+2
  q=q-2
  print(s) 
print(p*"-"+"*")