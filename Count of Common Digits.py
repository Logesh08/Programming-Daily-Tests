# Count of Common Digits
# An array of N integers is passed as input. The program must print the count of common digits in all of the N integers.

# Boundary Condition(s):
# 1 <= N <= 999999999999999999

# Input Format:
# The first line contains the value of N.
# The second line contains the value of N integers separated by space(s).

# Output Format:
# The first line contains the count of common digits in N integers.

# Example Input/Output 1:
# Input:
# 5
# 959646672 544814198 526566015 71285331 598788243

# Output:
# 1

# Explanation:
# The digit 5 is common in given integers.

# Example Input/Output 2:
# Input:
# 10
# 123456789 234567890 134567890 124567890 123567890 123467890 123457890 123456890 123456790 123456780

# Output:
# 0

# Explanation:
# There is no common digit in given integers.












input()
arr = input().split()
count = 0
for i in range(10):
    flag = True
    for val in arr:
        if str(i) not in val:
            flag=False
            break
    if flag:
        count+=1
print(count)