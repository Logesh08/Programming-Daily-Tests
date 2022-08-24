 # String Characters Mixing

# The program must accept two string values S1 and S2 (Both are of equal length) as the input. The program must consider every character in string S2 (from the first character to the last character) and replace the character being considered with the corresponding character which is in the same position in S1. Finally, the program must print the modified string values as the output.

# Boundary Condition(s):
# 2 <= Length of S1, S2 <= 100

# Input Format:
# The first line contains the values of string S1 and S2 separated by a space.

# Output Format:
# The first line contains the modified string values separated by space(s).

# Example Input/Output 1:
# Input:
# money agile

# Output:
# mgile aoile agnle agiee agily

# Example Input/Output 2:
# Input:
# computer vertical

# Output:
# certical vortical vemtical verpical vertucal vertital verticel verticar








a,b = input().split()
for i in range(len(a)):
    print(b[:i]+a[i]+b[i+1:],end=' ')