# Long Pressed Keys Count
# The program must accept two string values S1 and S2 as the input. The string S1 indicates a message. A person types the message S1 using the keyboard. Some keys on his keyboard are sticky keys (i.e., If he types a character once, that character will appear on the screen more than once). The string S2 indicates the message he received on the screen. The program must print the number of times the keys are not working properly (i.e., the number of times the keys that have been pressed for a long time) as the output. If a character is repeated consecutively more than once in S1 and the corresponding key is pressed for a long time, then considered the count as 1.

# Boundary Condition(s):
# 1 <= Length of S1 <= Length of S2 <= 100

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first line contains an integer representing the number of times the keys are not working properly.

# Example Input/Output 1:
# Input:
# monkey
# moonkeeey

# Output:
# 2

# Explanation:
# The 2 long pressed keys are o and e.

# Example Input/Output 2:
# Input:
# skillrack
# sssskkkilllllrackkkk

# Output:
# 4

# Explanation:
# The 4 long pressed keys are s, k, l and k.

# Example Input/Output 3:
# Input:
# BOOKKEEPING
# BOOOKKKKKKEEPING

# Output:
# 2

# Explanation:
# The 2 long pressed keys are O and K.






a=input().strip() 
b=input().strip() 
res=0
while a: 
    if(a[0]==b[0]): 
      a=a[1:] 
      b=b[1:] 
    else: 
        c=b[0]
        res+=1 
        while b and b[0]==c: 
            b=b[1:]
if b: 
    res+=1
print(res)