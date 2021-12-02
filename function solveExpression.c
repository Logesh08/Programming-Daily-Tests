// function solveExpression
// The function/method solveExpression accepts an argument expression representing an expression as given below.

// val1+val2=val3 or val1*val2=val3

// In the above expression, one of the three values will be replaced with X.

// The function/method solveExpression solve the given expression and find the value of X. Then the function must return the integer value X.

// Your task is to implement the function solveExpression so that the program runs successfully.

// IMPORTANT: Do not implement the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 5+X=7

// Output:
// 2

// Explanation:
// If X = 2, then the expression becomes 5+2=7.

// Example Input/Output 2:
// Input:
// 4*5=X

// Output:
// 20

// Example Input/Output 3:
// Input:
// X+2=100

// Output:
// 98

// Example Input/Output 4:
// Input:
// X*2=100

// Output:
// 50






#include <stdio.h>
#include <stdlib.h>
int solveExpression(char *expression)
{
    int num1=0,num2=0,flag=0;
    char ch;
    for(int index=0;expression[index];index++){
        if(index>0 && isdigit(expression[index-1]) && !isdigit(expression[index])){
            flag=1;
        }
        if(isdigit(expression[index]) && flag==0){
            num1=(num1*10)+(expression[index]-'0');
        }
        else if(isdigit(expression[index]) && flag){
            num2=(num2*10)+(expression[index]-'0');
        }
        else if(expression[index]!='X' && expression[index]!='='){
            ch=expression[index];
        }
    }
    int len=strlen(expression);
    if(expression[len-2]=='=' && expression[len-1]=='X'){
        if(ch=='+'){
            return num2+num1;
        }
        else{
            return num1*num2;
        }
    }
    if(ch=='+'){
        return num2-num1;
    }
    else{
        return num2/num1;
    }
}
int main()
{
    char expression[51];
    scanf("%s", expression);
    printf("%d", solveExpression(expression));
    return 0;
}