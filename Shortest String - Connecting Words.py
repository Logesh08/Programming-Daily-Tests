# Shortest String - Connecting Words
# The program must accept a string S containing multiple words as the input. The words in a given string are always connected by at least one character at the ends (i.e., some characters at the end of each word occur at the beginning of the next word). The program must form the shortest string by connecting the words from left to right (i.e., removing the duplicate characters in the overlap). Finally, the program must print the shortest string as the output.

# Boundary Condition(s):
# 3 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the shortest string.

# Example Input/Output 1:
# Input:
# water terminator ortho holly yellow owl

# Output:
# waterminatorthollyellowl

# Explanation:
# Here S = "water terminator ortho holly yellow owl".
# The shortest string is formed by connecting the words as given below.
# water+terminator -> waterminator
# waterminator+ortho -> waterminatortho
# waterminatortho+holly -> waterminatortholly
# waterminatortholly+yellow -> waterminatorthollyellow
# waterminatorthollyellow+owl -> waterminatorthollyellowl

# Example Input/Output 2:
# Input:
# cat tap pig gun

# Output:
# catapigun

# Example Input/Output 3:
# Input:
# ant antman mandatory

# Output:
# antmandatory

# Example Input/Output 4:
# Input:
# ababab ababab bababa bababa

# Output:
# abababa





n=input().split() 
s=n[0] 
for i in n[1:]: 
    for j in range(len(i),0,-1): 
        if(s[-j:]==i[:j]): 
            s+=i[j:] 
            break 
print(s)