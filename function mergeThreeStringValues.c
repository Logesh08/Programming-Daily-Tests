// function mergeThreeStringValues
// The function/method mergeThreeStringValues accepts three arguments str1, str2 and str3 representing three string values. All three string values represent the same string but each character is repeated a certain number of times.

// The function/method mergeThreeStringValues must merge the given three string values without any shuffle in the order of their occurrence. Then the function must return the merged string.

// Your task is to implement the function mergeThreeStringValues so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// kkkiiiiiiwwwiii
// kkiiiwwwwwiii
// kkkkiiwwiiiiii

// Output:
// kkkkkkkkkiiiiiiiiiiiwwwwwwwwwwiiiiiiiiiiii

// Explanation:
// str1 -> kkkiiiiiiwwwiii
// str2 -> kkiiiwwwwwiii
// str3 -> kkkkiiwwiiiiii
// kkk kk kkkk -> kkkkkkkkk
// iiiiii iii ii -> iiiiiiiiiii
// www wwwww ww -> wwwwwwwwww
// iii iii iiiiii -> iiiiiiiiiiii
// Hence the output is
// kkkkkkkkkiiiiiiiiiiiwwwwwwwwwwiiiiiiiiiiii

// Example Input/Output 2:
// Input:
// mmaango
// mannggo
// mangooo

// Output:
// mmmmaaaannnnggggooooo





#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* mergeThreeStringValues(char *str1, char *str2, char *str3)
{
    char *merge = malloc(9999999);
    int i,j=0,k=0,ind=0;
    merge[ind++]=str1[0];
    for(i=1;i<strlen(str1);i++){
        if(str1[i]!=str1[i-1] || i == strlen(str1)-1){
            merge[ind++] = str2[j++];
            int bf =0;
            for(;j<strlen(str2);j++){
                if(str2[j]!=str2[j-1] || j ==strlen(str2)-1){
                    merge[ind++] = str3[k++];
                    for(;k<strlen(str3);k++){
                        if(str3[k]!=str3[k-1]){
                            bf=1;
                            break;
                        }
                        merge[ind++] = str3[k];
                    }
                }
                if(bf) break;
                merge[ind++] = str2[j];
            }
        }
        merge[ind++]=str1[i];
    }
    for(;k<strlen(str3);k++) merge[ind++] = str3[k];
    return merge;
}
int main()
{
    char str1[1001], str2[1001], str3[1001];
    scanf("%s\n%s\n%s", str1, str2, str3);
    char *str = mergeThreeStringValues(str1, str2, str3);
    if(str == NULL || str == str1 || str == str2 || str == str3)
    {
        printf("String is not formed\n");
    }
    if(str[0] == ' ' || str[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", str);
    return 0;
}