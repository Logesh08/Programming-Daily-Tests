// function hexCodeToString
// The function/method hexCodeToString accepts an argument hexCode. The string hexCode contains the hex codes of all the characters of a string separated by a space.

// The function/method hexCodeToString must find the string value from the given hex codes and return the resulting string.

// Note: The string hexCode contains the hex codes of alphabets, digits and space characters.

// Your task is to implement the function hexCodeToString so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 73 6b 69 6c 6c 72 61 63 6b

// Output:
// skillrack

// Explanation:
// Here the given string is 73 6b 69 6c 6c 72 61 63 6b.
// After converting the hex codes to characters, the string becomes skillrack.

// Example Input/Output 2:
// Input:
// 48 65 6c 6c 6f 20 50 65 74 65 72

// Output:
// Hello Peter




#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* hexCodeToString(char *hexCode)
{
    char *word=malloc(sizeof(char)*1001);
    int index=0;
    char *ptr=strtok(hexCode," ");
    while(ptr!=NULL){
        sscanf(ptr,"%x",&word[index++]);
        ptr=strtok(NULL," ");
    }
    word[index]='\0';
    return word;
}
int main()
{
    char hexCode[1001];
    scanf("%[^\n]", hexCode);
    char *str = hexCodeToString(hexCode);
    if(str == hexCode)
    {
        printf("New string is not formed\n");
    }
    if(str[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", str);
}

