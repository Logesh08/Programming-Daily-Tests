// function alphabetsToIntegers
// The function/method alphabetsToIntegers accepts an argument str. The string str contains only alphabets(a - j) and minus symbol(-). The alphabets from a to j indicate the digits from 0 to 9 respectively. The minus symbol(-) indicates the sign of an integer.

// The function/method alphabetsToIntegers must form integers from the given alphabets and return the resulting integers as an array.

// Your task is to implement the function alphabetsToIntegers so that it passes all the test cases.

// The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
// typedef struct BoundedArray
// {
//     int SIZE;
//     int *arr;
// } boundedArray;

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// bc dff eaaj -hi

// Output:
// 12 355 4009 -78

// Explanation:
// bc -> 12
// dff -> 355
// eaaj -> 4009
// -hi -> -78

// Example Input/Output 2:
// Input:
// -aaae -gab ajai

// Output:
// -4 -601 908





#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;
#include<string.h>
boundedArray* alphabetsToIntegers(char *str)
{
    boundedArray *ptr =  malloc(10000001);
    ptr->arr = malloc(10000001);
    int i=0,len=strlen(str),ind=0;
    char *token = strtok(str," ");
    while(token){
        char temp[10];
        i=0;
        if(token[i]=='-'){
            temp[i]='-';
            i+=1;
        }
        while(token[i]!='\0'){
            int x = token[i]-97;
            // printf("%d ",x);
            sprintf(temp,"%s%d",temp,x);
            i++;
        }
        ptr->arr[ind++]=atoi(temp);
        token = strtok(NULL," ");
    }
    ptr->SIZE = ind;
    return ptr;
}
int main()
{
    char str[1001];
    scanf("%[^\n]", str);
    boundedArray *bArr = alphabetsToIntegers(str);
    if(bArr == NULL)
    {
        printf("Array is not formed\n");
    }
    if(bArr->SIZE <= 0)
    {
        printf("Invalid size for the array\n");
    }
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}