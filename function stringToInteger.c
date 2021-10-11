// function stringToInteger
// The function/method stringToInteger accepts an argument str representing a string value. The string contains the digits in words(only in lower case).

// The function/method stringToInteger must find the integer value from the given string and return the integer value.

// Your task is to implement the function stringToInteger so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// nineninefoursixseventwoone

// Output:
// 9946721

// Explanation:
// nine -> 9
// nine -> 9
// four -> 4
// six -> 6
// seven -> 7
// two -> 2
// one -> 1
// Hence the integer value is 9946721.

// Example Input/Output 2:
// Input:
// onefiveeightfivethreeeightzero

// Output:
// 1585380



#include<stdio.h>
#include<stdlib.h>
int stringToInteger(char *str)
{
    int ans=0, ind=0;
    char nums[10][10]={"zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}, tmp[10];
    for(int i=0; i<strlen(str); i++){
        tmp[ind++]=str[i];
        tmp[ind]='\0';
        for(int j=0; j<10; j++){
            if(strcmp(tmp, nums[j])==0){
                ans=ans*10+j;
                ind=0;
                break;
            }
        }
    }
    return ans;
}
int main()
{
    char str[51];
    scanf("%s", str);
    printf("%d", stringToInteger(str));
    return 0;
}