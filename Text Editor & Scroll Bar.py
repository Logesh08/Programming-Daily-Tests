# Text Editor & Scroll Bar
# In a text editor, the text area shows X lines, where each line contains a maximum of Y characters. The text editor never breaks a word into multiple lines. Initially, the text editor is empty. The program must accept a string S as the input. The string S represents the text to be pasted into the text editor. The text editor automatically shows a vertical scroll bar based on the lengths of the words in the text. In a single scroll (up/down), the text editor moves the text by one line up/down. The program must print an integer representing the number of times the scroll bar to be moved down to reach the last line as the output.

# Note: The length of each word in S is always less than or equal to Y.

# Boundary Condition(s):
# 1 <= X, Y <= 100
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains X and Y separated by a space.
# The second line contains S.

# Output Format:
# The first line contains the number of times the scroll bar to be moved down to reach the last line.

# Example Input/Output 1:
# Input:
# 4 10
# Rat Cat Lion Tiger Elephant Ox Fox Eagle Dog Snake Owl Ostrich

# Output:
# 3

# Explanation:
# If the given text is pasted into the text editor, the text editor contains the following 7 lines, but only the first 4 lines are visible.
# Rat Cat
# Lion Tiger
# Elephant
# Ox Fox
# Eagle Dog
# Snake Owl
# Ostrich
# After scrolling the vertical scroll bar 3 times down, the text editor shows the last 4 lines as given below.
# Ox Fox
# Eagle Dog
# Snake Owl
# Ostrich
# Now it shows the last line, so 3 is printed as the output.

# Example Input/Output 2:
# Input:
# 5 12
# NoteBook pencil pen Scale Eraser Paper INK box Scissors GLUE

# Output:
# 1


x,y=map(int,input().split())
s=input().strip().split()
rows=0
while s:
    cur=''
    pos=0
    for word in s:
        if len(cur)+len(word) +1<=y +1:
            cur+=' ' +word
            pos+=1 
        else:
            break 
    rows+=1 
    s=s[pos:]
    print(cur) 
print(max(rows-x,0))