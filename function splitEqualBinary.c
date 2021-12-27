// function splitEqualBinary
// The function/method splitEqualBinary accepts an argument N representing an integer value. The number of bits in the binary representation of N is always even.

// The function/method splitEqualBinary must split the binary representation of N into two equal halves. If the two halves are same, then the function must return the sum of decimal equivalents of the two equal halves. Else the function must return the integer N as it is.

// Your task is to implement the function splitEqualBinary so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 10

// Output:
// 4

// Explanation:
// Here N = 10.
// 10 -> 1010 -> 10 == 10.
// 2 + 2 = 4.

// Example Input/Output 2:
// Input:
// 187

// Output:
// 22

// Explanation:
// Here N = 187.
// 187 -> 10111011 -> 1011 == 1011.
// 11 + 11 = 22.

// Example Input/Output 3:
// Input:
// 8

// Output:
// 8







#include <stdio.h>
#include <stdlib.h>
int splitEqualBinary(int N)
{
int t,a[10000],x=0,i,s=0;
t=N;
while(t>0)
{
    a[x++]=t%2;
    t/=2;
}
for(i=0;i<x/2;i++)
{
    if(a[i]!=a[x/2+i])
    return N;
}
for(i=0;i<x/2;i++)
{
    if(a[i]==1)
    {
        s=s+pow(2,i);
    }
}
return s+s;

}
int main()
{
    int N;
    scanf("%d", &N);
    printf("%d", splitEqualBinary(N));
    return 0;
}