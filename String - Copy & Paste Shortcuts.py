# String - Copy & Paste Shortcuts
# The program must accept a string S representing a sentence containing few instances of "Ctrl+C" and "Ctrl+V". The program must print the sentence after applying those keyboard shortcuts based on the following conditions.
# 1) "Ctrl+C" will copy all the words behind it (i.e., the words except the keyboard shortcuts).
# 2) "Ctrl+V" will do nothing if there is no "Ctrl+C" before it. Else the copied words will be pasted.
# 3) A "Ctrl+C" which follows another "Ctrl+C" will overwrite what it copies.
# Note: The pasting must add a space between words.

# Boundary Condition(s):
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the sentence after applying those keyboard shortcuts.

# Example Input/Output 1:
# Input:
# hi Ctrl+C Ctrl+V how are you

# Output:
# hi hi how are you

# Explanation:
# Ctrl+C copies the word hi.
# Ctrl+V pastes the word hi.
# Hence the output is
# hi hi how are you

# Example Input/Output 2:
# Input:
# Rat and Ctrl+V Cat Ctrl+C Ctrl+V Ctrl+C Ctrl+V

# Output:
# Rat and Cat Rat and Cat Rat and Cat Rat and Cat

# Example Input/Output 3:
# Input:
# apple mango Ctrl+C Ctrl+V Ctrl+V grapes banana

# Output:
# apple mango apple mango apple mango grapes banana

# Example Input/Output 4:
# Input:
# a Ctrl+C an Ctrl+C the Ctrl+V

# Output:
# a an the a an





string=input().split()
printVal=""
pasteVal=""
for subVal in string:
    if subVal=="Ctrl+C":
        pasteVal=printVal
    elif subVal=="Ctrl+V":
        printVal+=pasteVal
    else:
        printVal+=subVal+" "
print(printVal)
