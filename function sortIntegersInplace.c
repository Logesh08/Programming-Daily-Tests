// function sortIntegersInplace
// The function/method sortIntegersInplace accepts an argument str. The string str contains words and integers.

// The function/method sortIntegersInplace must sort the integers in the string str among their positions. Then the function must return the revised string as a new string.

// Your task is to implement the function sortIntegersInplace so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// skillrack 50 20 code 105 how are 40 you 30

// Output:
// skillrack 20 30 code 40 how are 50 you 105

// Explanation:
// The integers in the given string are 50, 20, 105, 40 and 30.
// After sorting the integers in their positions, the string becomes
// skillrack 20 30 code 40 how are 50 you 105

// Example Input/Output 2:
// Input:
// 135 cat 9841 dog rat 12 987 cow

// Output:
// 12 cat 135 dog rat 987 9841 cow




#include<stdlib.h>
#include<stdio.h>
#include<string.h>

char* sortIntegersInplace(char *str)
{
    char real[99999];
    strcpy(real,str);
    char *token = strtok(str," ");
    int ind=0,i,j;
    int arr[99999];
    while(token!=NULL){
        char ch = token[0];
        if(ch>='0'&&ch<='9'){
            arr[ind++] = atoi(token);
        }
        token = strtok(NULL," ");
    }
    for(i=0;i<ind;i++){
        for(j=i+1;j<ind;j++){
            if(arr[i]>arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    i=0;
    char *ans = malloc(999999);
    char *words = strtok(real," ");
    while(words!=NULL){
        char ch = words[0];
        if(ch>='0'&&ch<='9'){
            sprintf(ans,"%s%d ",ans,arr[i++]);
        }else{
            sprintf(ans,"%s%s ",ans,words);
        }
        words = strtok(NULL," ");
    }
    return ans;
}

int main()
{
    char str[101];
    scanf("%[^\n\r]", str);
    char *result = sortIntegersInplace(str);
    if(result == NULL || result == str)
    {
        printf("New string is not formed\n");
    }
    if(result[0] == '\0' || result[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", result);
    return 0;
}