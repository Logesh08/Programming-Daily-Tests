// File - Replace Comma with Space
// The function/method replaceCommaWithSpace accepts an argument fileName representing the name of a text file. The given text file is always present in the same folder where the program executes and it contains comma-separated integer values in each line.

// The function/method replaceCommaWithSpace must modify the content of the given file by replacing each comma with a space.

// Your task is to implement the function replaceCommaWithSpace so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// numbers.txt

// Output:
// numbers.txt:
// 15 20 90 5465 345
// 15500 15
// 1 2 3 4 5 6 7 8 9 10 100 1000

// Explanation:
// Here numbers.txt is present in the same folder where the program executes and the file contains the following values.
// 15,20,90,5465,345
// 15500,15
// 1,2,3,4,5,6,7,8,9,10,100,1000

// Example Input/Output 2:
// Input:
// integers.txt

// Output:
// integers.txt:
// 36 73 12 58 19 58 29
// 66 67 28
// 75 77 67 6 94
// 49
// 49 40 12 39 28 7

// Explanation:
// Here integers.txt is present in the same folder where the program executes and the file contains the following values.
// 36,73,12,58,19,58,29
// 66,67,28
// 75,77,67,6,94
// 49
// 49,40,12,39,28,7









#include <stdio.h>
#include <stdlib.h>
void replaceCommaWithSpace(char *fileName)
{
    FILE * fp = fopen(fileName,"r");
    char out[10000];
    int ind = 0;char ch;
    while((ch=fgetc(fp))!=EOF){
        if(ch==',')ch = ' ';
        out[ind++] = ch;
    }
    out[ind] = 0;
    fclose(fp);
    fp = fopen(fileName,"w");
    fprintf(fp,"%s",out);
    fclose(fp);
}
void printFileContent(char *fileName)
{
    FILE *fp = fopen(fileName, "r");
    char ch;
    while((ch = fgetc(fp)) != EOF)
    {
        printf("%c", ch);
    }
    fclose(fp);
}

int main()
{
    char fileName[51];
    scanf("%s", fileName);
    replaceCommaWithSpace(fileName);
    printf("%s:\n", fileName);
    printFileContent(fileName);
    return 0;
}