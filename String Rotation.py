# String Rotation

# The program must accept the values of two string values (in clock wise rotation) S1 and S2 as input. If S2 is the rotated version of S1, then print YES as the output. Else print NO as the output.

# Boundary Condition(s):
# 2 <= Length of the string S1 and S2 <= 10000

# Input Format:
# The first line contains the string value S1.
# The second line contains the string value S2.

# Output Format:
# The first line contains either YES or NO. 

# Example Input/Output 1:
# Input:
# SkillRack
# ackSkillR

# Output:
# YES

# Example Input/Output 2:
# Input:
# skillrack
# illrackks

# Output:
# NO







a = input().strip()
b = input().strip()
a=a*2
print("YES" if b in a else "NO")