// function everyTwoDigitsToInteger
// The function/method everyTwoDigitsToInteger accepts an argument N representing an integer value.

// The function/method everyTwoDigitsToInteger must form integer values based on the following condition.
// - For every two digits D1 and D2 in the integer N, the program must form a new integer by using the digits from D1 to D2.
// Then the function must return an integer representing the sum of the resulting integers.

// Your task is to implement the function everyTwoDigitsToInteger so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 2514

// Output:
// 57900

// Explanation:
// Here N = 2514.
// 1st integer: 2345 (2 to 5).
// 2nd integer: 54321 (5 to 1).
// 3rd integer: 1234 (1 to 4).
// 2345 + 54321 + 1234 = 57900.

// Example Input/Output 2:
// Input:
// 90109

// Output:
// 10000000010

// Explanation:
// Here N = 90109.
// 1st integer: 9876543210 (9 to 0).
// 2nd integer: 01 -> 1 (0 to 1).
// 3rd integer: 10 (1 to 0).
// 4th integer: 0123456789 -> 123456789 (0 to 9).
// 9876543210 + 1 + 10 + 123456789 = 10000000010.







// as int
#include <stdio.h>
#include <stdlib.h>
long long int everyTwoDigitsToInteger(int N)
{
    long long int ans=0, pre=N%10;
    N/=10;
    while(N){
        long long int val=0, curr=N%10;
        N/=10;
        if(curr<pre){
            for(int i=curr; i<=pre; i++){
                val=val*10+i;
            }
        }else{
            for(int i=curr; i>=pre; i--){
                val = val*10+i;
            }
        }
        ans+=val;
        pre=curr;
    }
    return ans;
}
int main()
{
    int N;
    scanf("%d", &N);
    printf("%lld", everyTwoDigitsToInteger(N));
    return 0;
}









// as string
#include <stdio.h>
#include <stdlib.h>
long long int everyTwoDigitsToInteger(int N)
{
    long long int resultNum=0;
    char num[1001];
    sprintf(num,"%d",N);
    for(int ctr=0;ctr<strlen(num)-1;ctr++)
    {
        int num1=num[ctr]-'0',num2=num[ctr+1]-'0';
        long long int currNum=0;
        int inc=(num1<num2)?1:-1;
        while(num1!=num2)
        {
            currNum=currNum*10+num1;
            num1+=inc;
        }
        currNum=currNum*10+num1;
        resultNum+=currNum;
    }
    return resultNum;
}
int main()
{
    int N;
    scanf("%d", &N);
    printf("%lld", everyTwoDigitsToInteger(N));
    return 0;
}