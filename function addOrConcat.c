// function addOrConcat
// The function/method addOrConcat accepts an argument str representing a string value that contains the integers and words separated by a plus symbol (+).

// The function/method addOrConcat must perform the following operations on the given string.
// - If two or more integers are separated by a plus symbol (+), then those integers must be replaced with their sum.
// - If two or more words are separated by a plus symbol (+), then those words must be combined into a single word.
// Finally, the function must return the resulting string as the output.
// Note:
// - Each integer value will be from 1 to 10^6.
// - Each word contains only alphabets.

// Your task is to implement the function addOrConcat so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 5+10+rats+cats+25+monkeys+50+100+donkeys

// Output:
// 15+ratscats+25+monkeys+150+donkeys

// Explanation:
// Here the given string is 5+10+rats+cats+25+monkeys+50+100+donkeys.
// After performing the addition and concatenation operations, the resulting string becomes 15+ratscats+25+monkeys+150+donkeys.

// Example Input/Output 2:
// Input:
// a+b+c+d+1+2+3+4+5+alphabets+numbers

// Output:
// abcd+15+alphabetsnumbers





#include <stdio.h>
#include <stdlib.h>


#include <string.h>
char* addOrConcat(char *str)
{
    char *token = strtok(str,"+");
    char *ret = malloc(99999);
    char *prv = malloc(99999);
    int sum=0, sumSet = 0,cat=0;
    while(token!=NULL){
        if(token[0]>='0'&&token[0]<='9'){
            sum+=atoi(token);
            sumSet = 1;
            if(cat){
                cat=0;
                sprintf(ret,"%s+",ret);
            }
        }else{
            if(sumSet){
                sprintf(ret,"%s%d+",ret,sum);
                sumSet=sum=0;
            }
            sprintf(ret,"%s%s",ret,token);
            cat = 1;
        }
        strcpy(prv,token);
        token = strtok(NULL,"+");
        
    }
    if(sumSet)sprintf(ret,"%s%d+",ret,sum);
    return ret;
}


int main()
{
    char str[1001];
    scanf("%s", str);
    char *result = addOrConcat(str);
    if(result == NULL || result == str)
    {
        printf("String is not formed\n");
    }
    if(result[0] == ' ' || result[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", result);
    return 0;
}
