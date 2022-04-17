// function findAllDigits
// The function/method findAllDigits accepts two arguments SIZE and arr. The integer SIZE represents the size of the integer array arr.

// The function/method findAllDigits must find the presence of all the digits (0-9) from left to right in the given array. The function must return the integer from the array when all of the digits (0-9) have been discovered. If all the digits are not present in the given array, then the function must return -1.

// Your task is to implement the function findAllDigits so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 10
// 5175 458 292 5057 6401 4376 2280 6137 8798 9083

// Output:
// 4376

// Explanation:
// 1st integer: 5, 1 and 7 are found.
// 2nd integer: 4 and 8 are found new.
// 3rd integer: 2 and 9 are found new.
// 4th integer: 0 is found new.
// 5th integer: 6 is found new.
// 6th integer: 3 is found new. (Now all the digits have been discovered)
// Hence the 6th integer 4376 is printed as the output.

// Example Input/Output 2:
// Input:
// 4
// 12354 67821 1524 21359

// Output:
// -1














#include <stdio.h>
#include <stdlib.h>
int findAllDigits(int SIZE, int arr[])
{
    int dig[10]={0};
    for(int i =0 ;i<SIZE;i++){
        int n = arr[i];
        while(n>0){
            dig[n%10] = 1;
            n /= 10;
        }
        int flag = 1;
        for(int j =0;j<10;j++){
            if(dig[j]==0) {
                flag = 0;
                break;
            }
        }
        if(flag){
            return arr[i];
        }
    }
    return -1;
}
int main()
{
    int N;
    scanf("%d",&N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    printf("%d", findAllDigits(N, arr));
    return 0;
}