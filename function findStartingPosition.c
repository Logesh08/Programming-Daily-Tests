// function findStartingPosition
// The function/method findStartingPosition accepts four arguments R, C, matrix and str. The integers R and C represent the size of the character matrix. The given matrix contains the string str in any of its columns(i.e., the string str occurs exactly in one column in forward or reverse order).

// The function/method findStartingPosition must return an array of size 2 representing the position of the first character of the string in the matrix.

// Note: The first character and the last character of the given string are always distinct.

// Your task is to implement the function findStartingPosition so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 4 5
// a b c d e
// f l o i c
// k o o n o
// c c l d e
// cool

// Output:
// 1 3

// Explanation:
// The string "cool" occurs in the 3rd column of the matrix(starting from the 1st row).
// Hence the output is
// 1 3

// Example Input/Output 2:
// Input:
// 4 5
// a a g d e
// f o y k y
// o v d o b
// f s c l r
// bye

// Output:
// 3 5





#include <stdio.h>
#include <stdlib.h>

int* findStartingPosition(int R, int C, char *matrix, char *str)
{
    int *ret= (int*)malloc(sizeof(int)*2);
    int len =strlen(str);
    char mat[R][C];
    int x=0;
    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++){
            mat[i][j]=matrix[x++];
        }
    }
    for(int i=0; i<C; i++){
        for(int j=0; j<R; j++){
            int ind=0;
            for(int k=j; k<R; k++){
                if(mat[k][i]==str[ind]){
                    ind++;
                } else{
                    break;
                }
                if(ind==len){
                    ret[0]=j+1,ret[1]=i+1;
                    return ret;
                }
            }
            ind=0;
            for(int k=j; k>=0; k--){
                if(mat[k][i]==str[ind]){
                    ind++;
                }else{
                    break;
                }
                if(ind==len){
                    ret[0]=j+1;ret[1]=i+1;
                    return ret;
                }
            }
        }
    }
    return ret;
} // End of findStartingPosition function

int main()
{
    int R, C;
    scanf("%d%d", &R, &C);
    char matrix[R][C], str[C+1];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf(" %c", &matrix[row][col]);
        }
    }
    scanf("%s", str);
    int *pos = findStartingPosition(R, C, matrix, str);
    if(pos == NULL)
    {
        printf("Array is not formed\n");
    }
    printf("%d %d", pos[0], pos[1]);
    return 0;
} // End of main function