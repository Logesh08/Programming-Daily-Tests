// function getDateFromString
// The function/method getDateFromString accepts an argument dateStr. The string dateStr represents a date D. The day DD, the month MMM and the year YYYY in the date D can be in any order.

// The function/method getDateFromString must find the day, month and year from the given string. Then the function must return the date.

// The following structure is used to represent the Date and is already defined in the default code (Do not write this definition again in your code).
// struct Date
// {
//     int day;
//     char month[4];
//     int year;
// };
// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 02-Apr-2014

// Output:
// 2 Apr 2014

// Example Input/Output 2:
// Input:
// Aug-30-1990

// Output:
// 30 Aug 1990







#include <stdio.h>
#include <stdlib.h>

struct Date
{
    int day;
    char month[4];
    int year;
};
struct Date* getDateFromString(char *dateStr)
{
    struct Date *date=malloc(sizeof(struct Date));
    char str[101];
    int strInd=0;
    for(int index=0;index<strlen(dateStr)+1;index++){
        if(dateStr[index]=='-' || dateStr[index]=='\0'){
            str[strInd]='\0';
            if(isalpha(str[0])){
                strcpy(date->month,str);
            }
            else if(strInd<=2){
                date->day=atoi(str);
            }
            else{
                date->year=atoi(str);
            }
            str[strInd]='\0';
            strInd=0;
        }
        else{
            str[strInd++]=dateStr[index];
        }
    }
    return date;
}
int main()
{
    char dateStr[12];
    scanf("%s", dateStr);
    struct Date *date = getDateFromString(dateStr);
    if(date == NULL)
    {
        printf("Date is not formed\n");
    }
    printf("%d %s %d", date->day, date->month, date->year);
    return 0;
}