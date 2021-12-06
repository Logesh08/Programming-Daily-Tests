// function splitAndConcat
// The function/method splitAndConcat accepts an argument str. The string str contains multiple words of even length.

// The function/method splitAndConcat must split each word into two equal halves. Then the program must concatenate the second half of each word and the first half of its next word. Finally, the function must return the resulting string as a new string.

// Your task is to implement the function splitAndConcat so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// four lion keyboard on strawberry

// Output:
// fo urli onkeyb oardo nstraw berry

// Explanation:
// four -> fo and ur
// lion -> li and on
// keyboard -> keyb and oard
// on -> o and n
// strawberry -> straw and berry
// After concatenating the second half of each word and the first half of its next word, the words become
// fo urli onkeyb oardo nstraw berry

// Example Input/Output 2:
// Input:
// abcdefghij ABCDEF abcd pqrstu

// Output:
// abcde fghijABC DEFab cdpqr stu












#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* splitAndConcat(char *str)
{
    char *newone = malloc(sizeof(char)*strlen(str));
    int t = 0;
    char *tok = strtok(str," ");
    while(tok){
        int Len = strlen(tok)/2;
        for(int i = 0;i<Len;i++){
            newone[t++] = tok[i];
        }
        newone[t++] = ' ';
        for(int j = Len;j<strlen(tok);j++){
            newone[t++] = tok[j];
        }
        tok = strtok(NULL," ");
    }
    newone[t] = '\0';
    return newone;

}
int main()
{
    char str[101];
    scanf("%[^\n]", str);
    char *result = splitAndConcat(str);
    if(result == str || result == NULL)
    {
        printf("String is not formed\n");
    }
    if(result[0] == '\0' || result[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", result);
    return 0;
}