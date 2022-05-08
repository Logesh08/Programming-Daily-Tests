# Compressed String Pattern Matching
# The program must accept two string values S1 and S2 as the input. The string S2 represents a pattern that has a nonzero integer value between every two alphabets. Each nonzero value in the pattern S2 indicates the number of alphabets to be present between the two alphabets in the string S1. The program must print YES if the pattern S2 matches the string S1 by ignoring the case of the alphabets. Else the program must print NO as the output.

# Boundary Condition(s):
# 3 <= Length of S1, S2 <= 100

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first line contains YES or NO.

# Example Input/Output 1:
# Input:
# InternationalAirport
# I18t

# Output:
# YES

# Explanation:
# S1 = InternationalAirport.
# S2 = I18t
# I18t -> There are 18 characters between I and t in the string S1.
# So the pattern S2 matches the string S1.
# Hence the output is YES.

# Example Input/Output 2:
# Input:
# ROADMAP
# r1a3p

# Output:
# YES

# Explanation:
# S1 = ROADMAP
# S2 = r1a3p
# r1a -> There is 1 character between r and a in the string S1.
# a3p -> There are 3 characters between a and p in the string S1.
# So the pattern S2 matches the string S1.
# Hence the output is YES.

# Example Input/Output 3:
# Input:
# InternationalAirport
# I4n4n7t

# Output:
# NO



import re
s = input().strip().lower()
pattern = re.split('(\d+)',input().strip().lower()) 
if pattern[0] == '': pattern.pop(0)
for i in range(0,len(pattern),3):
    start = pattern[i]
    count = int(pattern[i+1])
    end = pattern[i+2]
    if (len(s) - s[::-1].index(end) - s.index(start)  -2 ) != count:
        print('NO',count)
        exit()
print('YES')