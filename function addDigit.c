// function addDigit
// Please implement the function addDigit(int *arr, int SIZE, int D) so that the program executes successfully. SIZE indicates the number of elements in arr. D is the digit to be added. The new array returned must be terminated by a -1 indicating that the array has ended.

// Boundary Condition(s):
// 1 <= N <= 1000
// 1 <= D <= 9

// Input Format:
// The first line contains N.
// The second line contains N integer values separated by a space.
// The third line contains D.

// Output Format:
// The first line contains N or N+1 integer values separated by a space.

// Example Input/Output 1:
// Input:
// 5
// 1 2 3 4 4
// 1

// Output:
// 1 2 3 4 5

// Explanation:
// 12344 + 1 = 12345. The digits are separated by a space.
// Hence the array returned must have the following six elements.
// [1, 2, 3, 4, 5, -1]
// The last -1 indicates the end of the array.

// Example Input/Output 2:
// Input:
// 3
// 9 9 9
// 2

// Output:
// 1 0 0 1

// Explanation:
// The array returned must have the following five elements.
// [1, 0, 0, 1, -1]
// The last -1 indicates the end of the array.




#include <stdio.h>
#include <stdlib.h>


int* addDigit(int *arr, int SIZE, int D)
{
    int* ret = malloc(sizeof(int)*(SIZE+2));
    int i,cur=0;
    
    for(i=0;i<SIZE;i++){
        cur = cur * 10 + arr[i];
    }
    cur+=D;
    int rev=1,rem;
    while(cur!=0){
        rem=cur%10;
        rev=rev*10+rem;
        cur/=10;
    }
    i=0;
    while(rev!=0){
        ret[i]=rev%10;
        rev/=10;
        i++;
    }
    ret[i-1]=-1;
    
    return ret;
}

int main()
{
    int N, digit;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    scanf("%d", &digit);
    int *ptr = addDigit(arr, N, digit);
    int index = 0;
    while(*(ptr+index) != -1)
    {
        printf("%d ", ptr[index]);
        index++;
    }
    return 0;
}
