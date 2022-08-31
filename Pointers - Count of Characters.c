// Pointers - Count of Characters

// The program must accept a string S and two characters CH1 and CH2 as the input. The program must print the number of characters which are present between CH1 and CH2 in the string S as the output. Fill in the missing lines of code so that the program runs successfully.
// Note: The string S contains only one occurrence of CH1 and CH2.

// Boundary Condition(s):
// 2 <= Length of S <= 100

// Input Format:
// The first line contains the string value S.
// The second line contains two characters CH1 and CH2 separated by a space.

// Output Format:
// The first line contains the number of characters present between CH1 and CH2 in the string S.

// Example Input/Output 1:
// Input:
// aq@#wed7cs
// @ c

// Output:
// 5

// Explanation:
// The 5 characters are # w e d 7 which are present between @ and c

// Example Input/Output 2:
// Input:
// akIU684@$#%763NVdsf
// V 4

// Output:
// 8









#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *a, *b;

    char str[101],x,y;
    scanf("%s\n",str);
    scanf("%c %c",&x,&y);
    int i=0,len=strlen(str);
    for(;i<len;i++){
        if(str[i]==x){
            a = &str[i];
            break;
        }
    }
    for(i=0;i<len;i++){
        if(str[i]==y){
            b = &str[i];
            break;
        }
    }
    printf("%d", abs(b - a) - 1);
    return 0;
}