// function swapDigitsSameSum
// The function/method swapDigitsSameSum accepts two arguments ptr1 and ptr2 representing the addresses of two integer values X and Y. The number of digits in X and Y are always not equal.

// The function/method swapDigitsSameSum must modify the given two integer values based on the following condition.
// - The function must remove the first D digits from the largest integer and prepend them to the smallest integer between the given two integers, where D is the absolute difference between the number of digits in X and Y.

// Please fill in the missing lines of code in the function swapDigitsSameSum so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 254 6573

// Output:
// 6254 573

// Explanation:
// The largest integer is 6573 and the smallest integer is 254.
// The number of digits in 6573 is 4.
// The number of digits in 254 is 3.
// After modifying the two integers based on the given conditions, the two integers become 6254 and 573.

// Example Input/Output 2:
// Input:
// 5056 23

// Output:
// 56 5023

// Example Input/Output 3:
// Input:
// 5000 654

// Output:
// 0 5654





// Method 1
#include <stdio.h>
#include <stdlib.h>
void swapDigitsSameSum(int *ptr1, int *ptr2)
{
    long int x=*ptr1,y=*ptr2,a=10;
    while(x>a && y>a){
        a*=10;
    }long int p=x/a,q=x%a,u=y/a,t=y%a;
    *ptr1=u*a+q;
    *ptr2=p*a+t;
}
int main()
{
    int X, Y;
    scanf("%d%d", &X, &Y);
    swapDigitsSameSum(&X, &Y);
    printf("%d %d", X, Y);
    return 0;
} // End of main function





//Method 2
#include <stdio.h>
#include <stdlib.h>
void swapDigitsSameSum(int *ptr1, int *ptr2)
{ 
    char a[15],b[15],t[15]; 
    sprintf(a,"%d",*ptr1); 
    sprintf(b,"%d",*ptr2); 
    int x=abs(strlen(a)-strlen(b)); 
    if(*ptr2>*ptr1) 
    {  
        strcpy(t,b); 
        t[x]='\0'; 
        strcat(t,a); 
        sprintf(b,"%s",b+x); 
        *ptr1=atoi(t); 
        *ptr2=atoi(b);
    }  
    else 
    {  
        strcpy(t,a); 
        t[x]='\0'; 
        strcat(t,b); 
        sprintf(a,"%s",a+x);
        *ptr1=atoi(a);   
        *ptr2=atoi(t);
    }

} // End of swapDigitsSameSum function
int main()
{
    int X, Y;
    scanf("%d%d", &X, &Y);
    swapDigitsSameSum(&X, &Y);
    printf("%d %d", X, Y);
    return 0;
} // End of main function