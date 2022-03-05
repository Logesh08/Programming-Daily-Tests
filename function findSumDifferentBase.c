#include <stdio.h>
#include <stdlib.h>
int findSumDifferentBase(char *str)
{
    int ans=0;
    #include<string.h>
    char *tok = strtok(str, " ");
    do{
        char c=tolower(tok[0]);
        tok++;
       
        if(c=='b'){
            ans+=strtoul(tok, 0,2);
        }else if(c=='d'){
            ans+=atoi(tok);
        }else{
            int val;
            if(c=='o'){
                sscanf(tok, "%o", &val);
            }else{
                sscanf(tok, "%x", &val);
            }
            ans+=val;
        }
    }while(tok=strtok(0, " "));
    return ans;
}
int main()
{
    char str[1001];
    scanf("%[^\n]", str);
    printf("%d", findSumDifferentBase(str));
    return 0;
}