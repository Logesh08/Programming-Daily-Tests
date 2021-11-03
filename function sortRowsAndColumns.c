// function sortRowsAndColumns
// The function/method sortRowsAndColumns accepts three arguments R, C and matrix. The first two arguments R and C represent the size of an integer matrix. The third argument matrix represents a pointer to the R*C integer matrix.

// The function/method sortRowsAndColumns must sort the integers in each row. Then the function must sort the integers in each column of the given matrix.

// Your task is to implement the function sortRowsAndColumns so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 4 5
// 96 66 74 60 18
// 42 12 96 62 15
// 68 29 64 92 24
// 60 44 37 61 53

// Output:
// 12 15 42 60 61
// 18 29 53 62 92
// 24 44 64 68 96
// 37 60 66 74 96

// Explanation:
// After sorting the integers in each row of the matrix, the matrix becomes
// 18 60 66 74 96
// 12 15 42 62 96
// 24 29 64 68 92
// 37 44 53 60 61

// After sorting the integers in each column of the revised matrix, the matrix becomes
// 12 15 42 60 61
// 18 29 53 62 92
// 24 44 64 68 96
// 37 60 66 74 96

// Example Input/Output 2:
// Input:
// 5 5
// 79 26 81 79 75
// 91 88 54 36 45
// 25 83 73 47 46
// 56 21 25 12 50
// 47 22 52 74 69

// Output:
// 12 21 25 50 56
// 22 45 47 69 74
// 25 46 52 73 81
// 26 47 54 79 83
// 36 75 79 88 91






#include <stdio.h>
#include <stdlib.h>

void sortRowsAndColumns(int R, int C, int *matrix)
{
    for(int row = 0, len = 0; row < R; row ++, len += C) {
        sort(C, matrix + len);
    }

    for(int col = 0; col < C; col ++) {
        for(int row = 0; row < R; row ++) {
            for(int row2 = row + 1; row2 < R; row2 ++) {
                if(matrix[row * C + col] > matrix[row2 * C + col]) {
                    swap(&matrix[row * C + col], &matrix[row2 * C + col]);
                }
            }
        }
    }
} // End of sortRowsAndColumns function

void swap(int *num1, int *num2) {
    int temp = *num1;
    *num1 = *num2;
    *num2 = temp;
}

void sort(int C, int *arr) {
    
    int ind1 = 1, ind2, key;
    
    while(ind1 < C) {
        key = arr[ind1];
        ind2 = ind1 - 1;
        
        while(ind2 >= 0 && arr[ind2] > key) {
            arr[ind2 + 1] = arr[ind2];
            ind2 --;
        }
        
        arr[ind2 + 1] = key;
        
        ind1 ++;
    }
    
}
int main()
{
    int R, C;
    scanf("%d %d", &R, &C);
    int matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix[row][col]);
        }
    }
    sortRowsAndColumns(R, C, matrix);
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            printf("%d ",  matrix[row][col]);
        }
        printf("\n");
    }
    return 0;
} // End of main function