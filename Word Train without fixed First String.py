# Word Train without fixed First String

# The program must accept an integer N and values of N string as input. The program must print the word train of N string as shown in the Example Input/Output section.
# Note: The last alphabet will not be duplicated in N string values.

# Boundary Condition(s):
# 2 <= N <= 15
# 1 <= Length of String <= 100

# Input Format:
# The first line contains the value of N.
# The next N lines contain the values of N string.

# Output Format:
# The N lines contain the word train of N string as shown in the Example Input/Output section.

# Example Input/Output 1:
# 4
# orange
# pancrea
# neuro
# amazon

# Output:
# pancrea
# amazon
# neuro
# orange

# Explanation:
# The first alphabet in pancrea is not equal to the ending alphabet of any one of the strings. So, the first string is pancrea.
# The last alphabet in pancrea and the first alphabet in amazon is equal. So, the second string is amazon.
# The last alphabet in amazon and the first alphabet in neuro is equal. So, the third string is neuro.
# The last alphabet in neuro and the first alphabet in organ is equal. So, the fourth string is organ.

# Example Input/Output 2:
# Input:
# 3    
# tang
# elephant
# apple

# Output:
# apple
# elephant
# tang






n = int(input())
arr = [input().strip() for i in range(n)]
start = [i for i in arr if (i[0] not in [c[-1] for c in arr ])][0]
print(start)
arr.remove(start)
l = start[-1]
while arr:
    for i in arr:
        if i[0] == l:
            print(i)
            l = i[-1]
            arr.remove(i)
            break