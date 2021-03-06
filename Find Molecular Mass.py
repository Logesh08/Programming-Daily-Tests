# Find Molecular Mass
# The program must accept a string S representing a chemical formula as the input. The program must print the molecular mass for the given chemical formula as the output. The given chemical formula contains the following elements (Element Name -> Symbol -> Atomic Mass).
# Hydrogen -> H -> 1
# Helium -> He -> 4
# Carbon -> C -> 12
# Nitrogen -> N -> 14
# Oxygen -> O -> 16
# Magnesium -> Mg -> 24
# Sulfur -> S -> 32
# Calcium -> Ca -> 40
# Copper -> Cu -> 63

# Boundary Conditions(s):
# 1 <= Length of S <= 50

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains an integer value representing the molecular mass for the given chemical formula.

# Example Input/Output 1:
# Input:
# H2O

# Output:
# 18

# Explanation:
# H2O -> 2 Hydrogen and 1 Oxygen
# Molecular Mass = (2 * 1) + 16 = 18.

# Example Input/Output 2:
# Input:
# C3H8O3

# Output:
# 92

# Explanation:
# C3H8O3 -> 3 Carbon, 8 Hydrogen and 3 Oxygen
# Molecular Mass = (3 * 12) + (8 * 1) + (3 * 16) = 92.

# Example Input/Output 3:
# Input:
# CuSO4

# Output:
# 159

# Example Input/Output 4:
# Input:
# C12H15

# Output:
# 159








s=(input().strip())
dic = {"H":1,"He":4,"C":12,"N":14,"O":16,"Mg":24,"S":32,"Ca":40,"Cu":63}
t=""
Sum=0
s=list(s)
for i in range(len(s)):
    if s[i] in "eau":
        s[i] += "1"
while s:
    if s[0].isdigit():
        i = "0"
        while s and s[0].isdigit():
            i += s.pop(0)
        Sum += dic[t] * int(i)
        t=''
    else:
        t += s.pop(0)
if t:
    Sum += dic[t]
print(Sum)