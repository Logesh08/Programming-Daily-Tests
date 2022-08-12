# Longest Common Prefix

# The program must accept N string values as input. The program must print the longest common prefix string among N string values as the output. If there is no common prefix string then the program must print -1 as the output.

# Boundary Condition(s):
# 2 <= N <= 1000
# 1 <= Length of each string <= 100

# Input Format:
# The first line contains the value of N.
# The next N lines contain a string in each line.

# Output Format:
# The first line contains either the longest common prefix string among N string values or -1.

# Example Input/Output 1:
# Input:
# 4
# encages
# encrypt
# envelop
# environment

# Output:
# en

# Explanation:
# encages
# encrypt
# envelop
# environment
# The longest common prefix string is en.
# Hence the output is en

# Example Input/Output 2:
# Input:
# 3
# flower
# lower
# flyover

# Output:
# -1






n = int(input())
arr = [input().strip() for _ in range(n)]
i = 0
while True:
    try: 
        if len(set([s[i] for s in arr])) == 1:
            i+=1
        else:
            break
    except:
        break
print(arr[0][:i] if i>0 else -1)