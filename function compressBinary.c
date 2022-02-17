// function compressBinary
// The function/method compressBinary accepts an argument N representing an integer value.

// The function/method compressBinary must compress the binary representation of N by replacing the consecutive 1s and 0s with their sum. Then the program must return an integer representing the result of the binary compression.

// Your task is to implement the function compressBinary so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Boundary Condition(s):
// 1 <= N <= 10^5

// Example Input/Output 1:
// Input:
// 120

// Output:
// 40

// Explanation:
// The binary representation of 120 is 1111000.
// After compressing the binary representation of 120, the binary representation becomes 40.
// 1111000 -> (1+1+1+1)(0+0+0) -> 40
// Hence 40 is printed as the output.

// Example Input/Output 2:
// Input:
// 2506

// Output:
// 10301010

// Explanation:
// The binary representation of 2506 is 100111001010.
// After compressing the binary representation of 2506, the binary representation becomes 10301010.
// 100111001010 -> (1)(0+0)(1+1+1)(0+0)(1)(0)(1)(0) -> 10301010
// Hence 10301010 is printed as the output.






#include <stdio.h>
#include <stdlib.h>
long long int compressBinary(int N)
{
    int binary[101],binInd=0;
    while(N>0){
        binary[binInd++]=N%2;
        N/=2;
    }
    char *num=malloc(1001);
    char numStr[101];
    int curr=binary[binInd-1];
    for(int index=binInd-2;index>=0;index--){
        if(binary[index]==binary[index+1]){
            curr+=binary[index];
        }
        else{
            sprintf(numStr,"%d",curr);
            strcat(num,numStr);
            curr=binary[index];
        }
    }
    sprintf(numStr,"%d",curr);
    strcat(num,numStr);
    return atol(num);
}
int main()
{
    int N;
    scanf("%d", &N);
    printf("%lld", compressBinary(N));
    return 0;
}