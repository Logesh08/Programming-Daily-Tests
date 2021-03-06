// function findDigitsBitMask
// The function/method findDigitsBitMask accepts an argument N representing an integer value.

// The function/method findDigitsBitMask must return an integer value X whose binary representation indicates the presence of digits in the given integer. The 10 digits (0 to 9) are mapped to 10 bits in the binary representation of X starting from LSB(least significant bit). The presence of the digits must be indicated by the set bits in the binary representation of X.

// Your task is to implement the function findDigitsBitMask so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 25414

// Output:
// 54

// Explanation:
// Here N = 25414.
// So the binary representation of X = 0000110110.
// 9876543210 <- All 10 digits.
// 0000110110 <- Binary Representation of X.
// Each set bit indicates the presence of corresponding digit.

// Example Input/Output 2:
// Input:
// 95500879

// Output:
// 929






#include <stdio.h>
#include <stdlib.h>
int findDigitsBitMask(long long int N) {
    
    int ans = 0;
    
    while (ans |= 1 << (N % 10), N /= 10);
    
    return ans;
    
}
int main()
{
    long long int N;
    scanf("%lld", &N);
    printf("%d", findDigitsBitMask(N));
    return 0;
}

