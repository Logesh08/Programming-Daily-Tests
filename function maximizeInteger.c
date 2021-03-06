// function maximizeInteger
// The function/method maximizeInteger accepts four arguments - M, arr1, N and arr2. The integer M represents the size of the integer array arr1. The integer N represents the size of the integer array arr2. Both arrays contain only digits. The digits in the array arr1 represents an integer value X.

// The function/method maximizeInteger must maximize the value of X by replacing its digits with the digits in the array arr2.

// Your task is to implement the function maximizeInteger so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 5
// 1 0 3 5 6
// 3
// 1 9 7

// Output:
// 9 7 3 5 6

// Explanation:
// The value of M is 5 and the given 5 integers are 1, 0, 3, 5 and 6.
// The value of N is 3 and the given 3 integers are 1, 9 and 7.
// After replacing the digit 1 in the arr1 with the digit 9 from arr2, the array becomes 9 0 3 5 6.
// After replacing the digit 0 in the arr1 with the digit 7 from arr2, the array becomes 9 7 3 5 6.

// Example Input/Output 2:
// Input:
// 6
// 8 9 1 2 6 2
// 4
// 4 4 4 4

// Output:
// 8 9 4 4 6 4








#include <stdio.h>
#include <stdlib.h>
void maximizeInteger(int M, int arr1[M], int N, int arr2[N])
{
    int i,j;
    for(i=0;i<N;i++){
        for(j=i+1;j<N;j++){
            if(arr2[i]<arr2[j]){
                int t = arr2[j];
                arr2[j] = arr2[i];
                arr2[i] = t;
            }
        }
    }
    int ind = 0;
    for(i=0;i<M;i++){
        if(arr1[i]<arr2[ind]){
            arr1[i] = arr2[ind++];
            if(ind==N) break;
        }
    }
}
int main()
{
    int M, N;
    scanf("%d", &M);
    int arr1[M];
    for(int index = 0; index < M; index++)
    {
        scanf("%d", &arr1[index]);
    }
    scanf("%d", &N);
    int arr2[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr2[index]);
    }
    maximizeInteger(M, arr1, N, arr2);
    for(int index = 0; index < M; index++)
    {
        printf("%d ", arr1[index]);
    }
    return 0;
}