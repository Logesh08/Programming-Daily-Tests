// Zip Arrays
// The program accepts three array elements with the size of the arrays as A, B and C as the input. The program must print "Two Arrays Zip:" followed by the integers that occur in the same positions in the first two arrays in separate lines. Then the program must print "Three Arrays Zip:" followed by the integers that occur in the same positions in the three arrays in separate lines.

// Your task is implement the function zipArrays so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 5 5 5
// 1 2 3 4 5
// 6 7 8 9 10
// 10 20 30 40 50

// Output:
// Two Arrays Zip:
// 1 6
// 2 7
// 3 8
// 4 9
// 5 10
// Three Arrays Zip:
// 1 6 10
// 2 7 20
// 3 8 30
// 4 9 40
// 5 10 50

// Explanation:
// The integers that occur in the same positions in the first two arrays are given below.
// 1 6
// 2 7
// 3 8
// 4 9
// 5 10
// The integers that occur in the same positions in the three arrays are given below.
// 1 6 10
// 2 7 20
// 3 8 30
// 4 9 40
// 5 10 50

// Example Input/Output 2:
// Input:
// 7 10 6
// 54 15 58 39 70 44 78
// 48 74 40 87 39 84 12 27 55 41
// 15 56 86 11 59 34

// Output:
// Two Arrays Zip:
// 54 48
// 15 74
// 58 40
// 39 87
// 70 39
// 44 84
// 78 12
// Three Arrays Zip:
// 54 48 15
// 15 74 56
// 58 40 86
// 39 87 11
// 70 39 59
// 44 84 34










#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
void zipArrays(int count, ...)
{
    va_list args;
    va_start(args,count);
    int min=999999,x;
    for(int i=0;i<count;i++){
        if(i%2==0){
            x = va_arg(args,int);
            min = x < min? x: min;
        }
        else{
            int *p = va_arg(args,int *);
            for(int j=0;j<x;j++){
                printf("%d ",p[j]);
                
            }
        }
        
    }
    printf("\n");
}
int main()
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    int arr1[A], arr2[B], arr3[C];
    for(int index = 0; index < A; index++){
        scanf("%d", &arr1[index]);
    }
    for(int index = 0; index < B; index++){
        scanf("%d", &arr2[index]);
    }
    for(int index = 0; index < C; index++){
        scanf("%d", &arr3[index]);
    }
    printf("Two Arrays Zip:\n");
    zipArrays(4, A, arr1, B, arr2);
    printf("Three Arrays Zip:\n");
    zipArrays(6, A, arr1, B, arr2, C, arr3);
    return 0;
}