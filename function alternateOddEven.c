// function alternateOddEven
// The function/method alternateOddEven accepts two arguments arr and N. The integer N represents the size of the integer array arr.

// The function/method alternateOddEven must return an array where odd and even integers are placed alternatively in the same order of their occurrence. 
// The array contains an equal count of odd and even integers.
// Note: The value of N is always even.

// Your task is to implement the function alternateOddEven so that the program runs successfully.

// IMPORTANT: Do not implement the main() function as it is already defined.

// Input Format:
// The first line contains N.
// The second line contains the N integer values separated by a space.

// Output Format:
// The N integer values with odd and even integers are placed alternatively separated by a space.

// Example Input/Output 1:
// Input:
// 6
// 10 5 7 8 99 44

// Output:
// 5 10 7 8 99 44

// Explanation:
// Here N=6 and the given 6 integers are 10 5 7 8 99 44.
// After placing the odd and even integers alternatively in the same order of their occurrence, the array becomes 5 10 7 8 99 44.

// Example Input/Output 2:
// Input:
// 4
// 2 3 64 5

// Output:
// 3 2 5 64



#include <stdio.h>
#include <stdlib.h>
int* alternateOddEven(int arr[], int N)
{
    int *newArr = malloc(sizeof(int)*N);
    int i,odd[N/2],even[N/2],evenIndex=0,oddIndex=0;
    for(i=0;i<N;i++){
        if(arr[i]%2==0) even[evenIndex++]=arr[i];
        else odd[oddIndex++]=arr[i];
    }
    oddIndex=evenIndex=0;
    for(i=0;i<N;i++){
        if(i%2==0) newArr[i]=odd[oddIndex++];
        else newArr[i]=even[evenIndex++];
    }
    return newArr;
}
int main()
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", arr+index);
    }
    int *ptr = alternateOddEven(arr,N);
    for(int index = 0; index < N; index++)
    {
        printf("%d ",ptr[index]);
    }
}
