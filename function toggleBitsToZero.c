// function toggleBitsToZero
// The function/method toggleBitsToZero accepts two arguments - SIZE and arr. The integer size represents the size of the integer array arr.

// The function/method toggleBitsToZero must modify the integers in the array arr based on the following condition.
// - For each integer X in the array arr, the function must convert the bits to 0 that occur in the odd positions from LSB.
// Finally, the function must return an integer representing the sum of the N revised integers.

// Your task is to implement to function toggleBitsToZero so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 4
// 15 10 12 18

// Output:
// 30

// Explanation:
// 15 -> 1111 -> 1010 -> 10.
// 10 -> 1010 -> 1010 -> 10.
// 12 -> 1100 -> 1000 -> 8.
// 18 -> 10010 -> 00010 -> 2.
// 10 + 10 + 8 + 2 = 30.

// Example Input/Output 2:
// Input:
// 5
// 240 48 409 85 42

// Output:
// 370

// Explanation:
// 240 -> 11110000 -> 10100000 -> 160.
// 48 -> 110000 -> 100000 -> 32.
// 409 -> 110011001 -> 010001000 -> 136.
// 85 -> 1010101 -> 0000000 -> 0.
// 42 -> 101010 -> 101010 -> 42.
// 160 + 32 + 136 + 0 + 42 = 370.





#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int toggleBitsToZero(int SIZE, int *arr)
{
    int sum = 0;
    for(int i=0;i<SIZE;i++){
        char tmp[101]={'\0'};
        int ind=0;
        while(arr[i]>0){
            if(arr[i]%2==0)
                tmp[ind++]='0';
            else
                tmp[ind++]='1';
            arr[i]/=2;
                
        }
        int t=0;
        while(tmp[t]!='\0'){
            if(t%2==0) tmp[t]='0';
            t++;
        }
        int n=0;
        for(int j=0;j<ind;j++){
            int r;
            if(tmp[j]=='0') r=0;
            else r=1;
            n+= r* pow(2,j);
        }
        sum+=n;
    }
    return sum;
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
    printf("%d", toggleBitsToZero(N, arr));
    return 0;
}