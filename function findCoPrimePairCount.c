// function findCoPrimePairCount
// Two integers x and y are coprime if the only positive integer that is a divisor of both of them is 1.

// The function/method findCoPrimePairCount accepts four arguments - M, arr1, N, arr2. The integer M represents the size of the integer array arr1. The integer N represents the size of the integer array arr2.

// The function/method findCoPrimePairCount must return the number of pairs (x, y) where x and y are co-prime numbers. The values x, y belong to the arrays arr1 and arr2 respectively.

// Your task is to implement the function findCoPrimePairCount so that it passes all the test cases.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 5
// 12 45 7 10 20
// 4
// 15 67 34 40

// Output:
// 9

// Explanation:
// The 9 co-prime pairs are given below.
// 12 67
// 45 67
// 45 34
// 7 15
// 7 67
// 7 34
// 7 40
// 10 67
// 20 67

// Example Input/Output 2:
// Input:
// 6
// 19 12 45 38 10 34
// 3
// 8 12 10

// Output:
// 4









#include <stdio.h>
#include <stdlib.h>
int findCoPrimePairCount(int M, int arr1[M], int N, int arr2[N])
{
    int count = 0,i,j,k,hcf;
    for(i=0;i<M;i++){
        for(j=0;j<N;j++){
            for(k=1;k<=arr1[i];k++){
                if(arr1[i]%k==0 && arr2[j]%k==0)
                    hcf = k;
            }
            if(hcf==1){
                count++;
            }
        }
    }
    return count;
}
int main()
{
    int M, N, X;
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
    printf("%d", findCoPrimePairCount(M, arr1, N, arr2));
    return 0;
}
