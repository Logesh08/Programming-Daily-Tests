// function getMatrixEdge
// The function/method getMatrixEdge accepts four arguments - R, C, matrix and E. The integers R and C represent the size of the integer matrix. The character E represents one of the four edges of the matrix (T, R, B or L).

// The function/method getMatrixEdge must return an array of integers containing all the integers in the given edge of the matrix based on the following conditions.
// - Top Edge: The order of integers must be from left to right.
// - Right Edge: The order of integers must be from top to bottom.
// - Bottom Edge: The order of integers must be from right to left.
// - Left Edge: The order of integers must be from bottom to top.

// Your task is to implement the function getMatrixEdge so that it passes all the test cases.

// The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
// typedef struct BoundedArray
// {
//     int SIZE;
//     int *arr;
// } boundedArray;

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 6 5
// 53 91 24 31 17
// 11 76 70 25 75
// 99 74 66 87 50
// 29 15 64 71 42
// 67 13 47 23 20
// 49 48 86 36 84
// T

// Output:
// 53 91 24 31 17

// Example Input/Output 2:
// Input:
// 6 5
// 53 91 24 31 17
// 11 76 70 25 75
// 99 74 66 87 50
// 29 15 64 71 42
// 67 13 47 23 20
// 49 48 86 36 84
// R

// Output:
// 17 75 50 42 20 84

// Example Input/Output 3:
// Input:
// 6 5
// 53 91 24 31 17
// 11 76 70 25 75
// 99 74 66 87 50
// 29 15 64 71 42
// 67 13 47 23 20
// 49 48 86 36 84
// B

// Output:
// 84 36 86 48 49

// Example Input/Output 4:
// Input:
// 6 5
// 53 91 24 31 17
// 11 76 70 25 75
// 99 74 66 87 50
// 29 15 64 71 42
// 67 13 47 23 20
// 49 48 86 36 84
// L

// Output:
// 49 67 29 99 11 53


#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;


boundedArray* getMatrixEdge(int R, int C, int matrix[R][C], char E)
{
    boundedArray *bArr = malloc(sizeof(int)*R*C +2);
    bArr->arr=malloc(sizeof(int)*R*C);
    int index=0,i=0;
    if(E=='T'){
        for(i=0;i<C;i++){
            bArr->arr[index++]=matrix[0][i];
        }
    }else if(E=='R'){
        for(i=0;i<R;i++){
            bArr->arr[index++]=matrix[i][C-1];
        }
    }else if(E=='B'){
        for(i=C-1;i>=0;i--){
            bArr->arr[index++]=matrix[R-1][i];
        }
    }else if(E=='L'){
        for(i=R-1;i>=0;i--){
            bArr->arr[index++]=matrix[i][0];
        }
    }
    bArr->SIZE=index;
    return bArr;
}


int main()
{
    int R, C;
    char E;
    scanf("%d %d", &R, &C);
    int matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix[row][col]);
        }
    }
    scanf(" %c", &E);
    boundedArray *bArr = getMatrixEdge(R, C, matrix, E);
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}
