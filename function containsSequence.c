// function containsSequence
// The function/method containsSequence accepts three arguments SIZE, arr and K. The integer SIZE represents the size of the integer array arr and K represents an integer value. The integers in the given array are always in sorted order(either in ascending or descending).

// The function/method containsSequence must return 1 if the given array contains all the integers from 1 to K and no other integers. Else the function must return 0.

// Your task is to implement the function containsSequence so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 5
// 1 1 2 3 3
// 3

// Output:
// 1

// Explanation:
// Here N=5, K=3 and the given 5 integers are 1, 1, 2, 3 and 3.
// The array contains all the integers from 1 to 3 and no other integers, so 1 is printed as the output.

// Example Input/Output 2:
// Input:
// 4
// 1 1 1 3
// 2

// Output:
// 0

// Example Input/Output 3:
// Input:
// 5
// 2 2 1 1 1
// 2

// Output:
// 1

// Example Input/Output 4:
// Input:
// 5
// 5 4 3 2 1
// 4

// Output:
// 0









#include <stdio.h>
#include <stdlib.h>
int containsSequence(int SIZE, int *arr, int K)
{
    for(int i=1;i<=K;i++){
        int found = 0;
        for(int j = 0;j<SIZE;j++){
            if(arr[j]>K) return 0;
            if (arr[j] == i){
                found = 1;
            }
        }
        if(!found){
            return 0;
        }
    }
    return 1;
}

int main()
{
    int N, K;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    scanf("%d", &K);
    printf("%d", containsSequence(N, arr, K));
    return 0;
}





