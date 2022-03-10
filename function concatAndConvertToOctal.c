// function concatAndConvertToOctal
// The function/method concatAndConvertToOctal accepts two arguments - SIZE and arr. The integer SIZE represents the size of the integer array arr.

// The function/method concatAndConvertToOctal must find the binary representation of each integer in the given array. Then the function must concatenate all the binary representations and print its the octal equivalent.

// Your task is to implement the function concatAndConvertToOctal so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Boundary Condition(s):
// 1 <= SIZE <= 100
// 1 <= Each integer value <= 10^6

// Example Input/Output 1:
// Input:
// 5
// 45 127 32 19 25

// Output:
// 2677701171

// Explanation:
// 45 -> 101101
// 127 -> 1111111
// 32 -> 100000
// 19 -> 10011
// 25 -> 11001
// The concatenated binary representation is given below.
// 10110111111111000001001111001
// The octal equivalent is 2677701171.

// Example Input/Output 2:
// Input:
// 4
// 9 10 4 2

// Output:
// 11522









#include <stdio.h>
#include <stdlib.h>
void concatAndConvertToOctal(int SIZE, int arr[])
{
    int k[10000],l=0;
    for(int i=SIZE-1;i>=0;i--){
        int t=arr[i];
        while(t){
            k[l++]=t%2;
            t/=2;
        }
    }
    while(l%3!=0){
        k[l++]=0;
    }
    for(int i=l-1;i>=0;i-=3){
        int d=0,c=1;
        for(int j=i-2;j<=i;j++){
            d+=(c*k[j]);
            c*=2;
        }
        printf("%d",d);
    }
}
int main()
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    concatAndConvertToOctal(N, arr);
    return 0;
}