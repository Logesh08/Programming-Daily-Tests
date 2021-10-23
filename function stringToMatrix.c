// function stringToMatrix
// The function/method stringToMatrix accepts three arguments N, str1 and str2. The integer N represents the size of a character matrix to be created. The sum of lengths of both string values str1 and str2 is equal to N*N.

// The function/method stringToMatrix must return a double pointer representing the character matrix based on the following conditions.
// - The size of the character matrix must be N*N.
// - The matrix must be filled with the characters from the string values str1 and str2 alternatively (starting from the 1st row, where left to right in each row of the matrix).

// Your task is to implement the function stringToMatrix so that it passes all the test cases.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 3
// Skill
// Rack

// Output:
// S R k
// a i c
// l k l

// Explanation:
// Here N=3, so the size of the character matrix is 3*3.
// After filling the matrix with the characters from the string values "Skill" and "Rack" alternatively, the matrix becomes
// S R k
// a i c
// l k l

// Example Input/Output 2:
// Input:
// 4
// abcdefgh
// ijklmnop

// Output:
// a i b j
// c k d l
// e m f n
// g o h p



#include <stdio.h>
#include <stdlib.h>

char** stringToMatrix(int N, char *str1, char *str2)
{
    int i1=0,i2=0,f=1;
    char **mat=malloc(sizeof(char*)*N);
    for(int i=0;i<N;i++){
        char *t=malloc(sizeof(char)*N);
        mat[i]=t;
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(f){
                if(i1<strlen(str1)){
                    mat[i][j]=str1[i1];
                    i1++;
                    if(i2<strlen(str2))f=!f;
                }
            }else{
                if(i2<strlen(str2)){
                    mat[i][j]=str2[i2++];
                    if(i1<strlen(str1))f=!f;
                }
            }
        }
    }
    return mat;
} // End of stringToMatrix function

int main()
{
    int N;
    scanf("%d\n", &N);
    char str1[N*N], str2[N*N];
    scanf("%s\n%s", str1, str2);
    char **matrix = stringToMatrix(N, str1, str2);
    if(matrix == NULL)
    {
        printf("Matrix is not formed\n");
    }
    for(int row = 0; row < N; row++)
    {
        for(int col = 0; col < N; col++)
        {
            printf("%c ", matrix[row][col]);
        }
        printf("\n");
    }
    return 0;
} // End of main function