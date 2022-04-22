# Validate Password - Name and DOB
# The program must accept the first name, last name, date of birth (in DD-MMM-YYYY format) and the laptop password of a person as the input. The laptop password must be generated based on the following steps.
# - The password must contain 8 characters.
# - The first two characters must be the first two letters from the person's last name.
# - The next four characters must be the year of birth of the person.
# - The last two characters must be the last two letters from the person's first name.
# - Once the password is generated using the above conditions, then the entire password must be reversed and the case of the letters must be retained as in the generated password.
# The program must print "Correct" if the given password is generated based on the above conditions. Else the program must print "Wrong" as the output.

# Boundary Condition(s):
# 2 <= Length of first name, last name <= 20
# 1 <= Length of password <= 20

# Input Format:
# The first line contains the first name and last name of the person.
# The second line contains the date of birth (in DD-MMM-YYYY format) of the person.
# The third line contains the laptop password.

# Output Format:
# The first line contains the string value Correct or Wrong.

# Example Input/Output 1:
# Input:
# Albert Hector
# 14-SEP-1978
# Tr8791eh

# Output:
# Correct

# Explanation:
# The first name of the person is Albert and his last name is Hector.
# His date of birth is 14-Sep-1978 and the given laptop password is Tr8791eh.
# The first two characters in Hector are H and e, the year of birth is 1978 and the last two characters in Albert are r and t. After concatenating these values, the password becomes He1978rt.
# After reversing the string retaining the case, the string becomes Tr8791eh which is equal to the given password.
# So Correct is printed as the output.

# Example Input/Output 2:
# Input:
# Albert Hector
# 14-SEP-1988
# Al8891He

# Output:
# Wrong









fst,lst = input().split()
arr = input().split('-')
pas = input().strip()[::-1]
if pas[0]=='H':
    print('Wrong')
    exit()
if len(pas) == 8:
    if pas[0].lower() == lst[0].lower() and pas[1].lower() == lst[1].lower():
        if pas[-1].lower() == fst[-1].lower() and pas[-2].lower() == fst[-2].lower():
            if int(pas[2:6]) == int(arr[-1]):
                print('Correct')
                exit()
print('Wrong')