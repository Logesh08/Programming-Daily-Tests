// # function concatBinary
// # The function/method concatBinary accepts two arguments num1 and num2 representing two integer values. The integer num2 contains only 1s and 0s denoting the binary representation of an integer X.

// # The function/method concatBinary must concatenate the binary representation of num1 and X. Then the function must return an integer representing the decimal equivalent of the concatenated the binary representation.

// # Your task is to implement the function concatBinary so that the program runs successfully.

// # IMPORTANT: Do not write the main() function as it is already defined.

// # Example Input/Output 1:
// # Input:
// # 5 110

// # Output:
// # 46

// # Explanation:
// # Here num1 = 5 and num2 = 110.
// # The binary representation of 5 is 101.
// # The concatenation of 101 and 110 is 101110.
// # The decimal equivalent of 101110 is 46.

// # Example Input/Output 2:
// # Input:
// # 425 10011

// # Output:
// # 13619

// # Explanation:
// # Here num1 = 425 and num2 = 10011.
// # The binary representation of 425 is 110101001.
// # The concatenation of 110101001 and 10011 is 11010100110011.
// # The decimal equivalent of 11010100110011 is 13619.





#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int concatBinary(int num1, int num2)
{
    int a[100001];
    int i =0 ;
    for(;num1>0;i++){
        a[i]=num1%2;
        num1/=2;
    }
    for(;num2>0;i++){
        a[i]=num2%2;
        num2/=2;
    }
    int number =0;
    for(int x=0;x<i;x++){
        number += pow(2,x);
    }
    return number;
}

int main()
{
    int num1, num2;
    scanf("%d%d", &num1, &num2);
    printf("%d", concatBinary(num1, num2));
    return 0;
}