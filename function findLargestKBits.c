// function findLargestKBits
// The function/method findLargestKBits accepts two arguments str and K. The string str contains only 0s and 1s. K represents an integer value.

// The function/method findLargestKBits must an integer representing the largest possible integer that can be formed using exactly K consecutive bits in the given string.

// Note: The value of K is always less than or equal to the length of the given string.

// Your task is to implement the function findLargestKBits so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Boundary Condition(s):
// 1 <= Length of the string <= 1000
// 1 <= K <= 31

// Example Input/Output 1:
// Input:
// 001001101100
// 4

// Output:
// 13

// Explanation:
// Here K = 4.
// All possible ways are given below.
// 0010 -> 2
// 0100 -> 4
// 1001 -> 9
// 0011 -> 3
// 0110 -> 6
// 1101 -> 13
// 1011 -> 11
// 0110 -> 6
// 1100 -> 12
// The largest possible integer using 4 consecutive bits is 13.

// Example Input/Output 2:
// Input:
// 1100111011
// 3

// Output:
// 7



//method 1
#include <stdio.h>
#include <stdlib.h>
int findLargestKBits(char *str, int K)
{
    int i,j,len=strlen(str),ans=0;
    for(i=0;i<=len-K;i++){
        char num[K+1]; 
        for(j=i;j<i+K;j++)
            num[j-i] = str[j];
        num[K] = '\0';
        int con = (int)strtol(num,NULL,2);
        ans = (ans>con)?ans:con;
    } 
    return ans;        

}
int main()
{
    char str[1001];
    int K;
    scanf("%s\n%d", str, &K);
    printf("%d", findLargestKBits(str, K));
    return 0;
}


//method 2
#include <stdio.h>
#include <stdlib.h>
int findLargestKBits(char *str, int K)
{
    int num=-100001;
    for(int index=0;index<=strlen(str)-K;index++){
        int currNum=0;
        for(int subInd=index;subInd<index+K;subInd++){
            currNum=currNum*2+(str[subInd]-'0');
        }
        if(currNum>num){
            num=currNum;
        }
    }
    return num;
}
int main()
{
    char str[1001];
    int K;
    scanf("%s\n%d", str, &K);
    printf("%d", findLargestKBits(str, K));
    return 0;
}