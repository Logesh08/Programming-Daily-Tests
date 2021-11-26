# Two Right-Angle Triangles Pattern
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
# ----*
# --*-*-*
# *-*-*-*-*

# Explanation:
# Here N=3, so the pattern contains 3 lines of output.
# The asterisks in the pattern represent the two right-angle triangles and the hyphens in the pattern represent the empty spaces.

# Example Input/Output 2:
# Input:
# 5

# Output:
# --------*
# ------*-*-*
# ----*---*---*
# --*-----*-----*
# *-*-*-*-*-*-*-*-*

# Example Input/Output 3:
# Input:
# 6

# Output:
# ----------*
# --------*-*-*
# ------*---*---*
# ----*-----*-----*
# --*-------*-------*
# *-*-*-*-*-*-*-*-*-*-*














N = int(input())
start = 2*(N-1)
for ctr in range(N-1):
    stars = ["-"]*(2*(ctr+1)-1)
    stars[0] = "*"
    stars[-1] = "*"
    stars[len(stars)//2] = "*"
    print("-"*start+'-'.join(stars))
    start -= 2
lastCtr = 2*N-1
last = ["*"]*lastCtr
print('-'.join(last))