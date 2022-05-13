// function countWordsOnlyAlphabets
// The function/method countWordsOnlyAlphabets accepts an argument str representing a string value. The string contains multiple words.

// The function/method countWordsOnlyAlphabets must remove the punctuation marks (comma, dot, question mark and exclamation mark). The function must return an integer representing the count of words containing only alphabets in the string. Hyphens join two words into one and hence it must be counted as a single word.

// Your task is to implement the function countWordsOnlyAlphabets so that the program runs successfully.

// IMPORTANT: Do not implement the main() function as it is already defined.

// Boundary Condition(s):
// 1 <= Length of the string <= 1000

// Example Input/Output 1:
// Input:
// How many bangles are in a half-dozen? 11?

// Output:
// 7

// Explanation:
// The 7 words are given below.
// How
// many
// bangles
// are
// in
// a
// half-dozen

// Example Input/Output 2:
// Input:
// Ten Apples, Five Oranges, 100 Grapes, Twenty-Five mangoes and 75bananas.

// Output:
// 8

// Explanation:
// The 8 words are given below.
// Ten
// Apples
// Five
// Oranges
// Grapes
// Twenty-Five
// mangoes
// and












#include <stdio.h>
#include <stdlib.h>

int countWordsOnlyAlphabets(char *str)
{
    int i=0;
    int count = 0, flag = 1;
    while(str[i]!='\0'){
        if(str[i]==' '){
            if(flag) count+=1;
            flag = 1;
        }else if(isdigit(str[i])){
            flag =0;
        }
        i++;
    }
    if(flag) count+=1;
    printf("foo bar");
    return count;
}   

int main()
{
    char str[1001];
    scanf("%[^\n]", str);
    printf("%d", countWordsOnlyAlphabets(str));
    return 0;
}