// Rising Sequence - Minimum Addition
// The program must accept N integers and an integer K as the input. The program must convert the given sequence of N integers into a rising sequence (i.e., a sequence of integers in strictly increasing order) by adding K to one or more elements, any number of times. The program must print the minimum number of times the value K to be added to the sequence to make the rising sequence as the output.

// Boundary Condition(s):
// 2 <= N <= 1000
// 1 <= Each integer value, K <= 10^6

// Input Format:
// The first line contains N.
// The second line contains N integers separated by a space.
// The third line contains K.

// Output Format:
// The first line contains an integer representing the minimum number of times the value K to be added to the sequence to make the rising sequence.

// Example Input/Output 1:
// Input:
// 4
// 2 6 6 5
// 2

// Output:
// 3

// Explanation:
// Here K = 2.
// The rising sequence can be formed as 2, 6, 8 and 9 by adding the value K thrice.
// 3rd integer -> 6 + 2 = 8 (2 is added once)
// 4th integer -> 5 + 2 + 2 = 9 (2 is added twice)
// Hence 3 is printed as the output.

// Example Input/Output 2:
// Input:
// 4
// 1 2 3 4
// 1

// Output:
// 0

// Example Input/Output 3:
// Input:
// 5
// 1 100 2 5 5
// 3

// Output:
// 100


#include<stdio.h>
#include<stdlib.h>

int main()
{
    int x,i,j,y,c=0;
    int a[1005];
    scanf("%d",&x);
    for(i=0;i<x;i++)
    scanf("%d",&a[i]);
    scanf("%d ",&y);
    for(i=01;i<x;i++)
    {
        while(a[i]<=a[i-1])
        {
            a[i]+=y;
            c++;
        }
    }
    printf("%d",c);

}
