// function validateDate
// The function/method validateDate accepts an argument dateStr representing a string value which contains a date in the format "DD-MM-YYYY".

// The function/method validateDate must return 1 if the given date is valid. Else the function must return 0.

// Your task is to implement the function validateDate so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 26-08-2021

// Output:
// 1

// Example Input/Output 2:
// Input:
// 09-15-2010

// Output:
// 0

// Explanation:
// Invalid month 15.

// Example Input/Output 3:
// Input:
// 39-12-2100

// Output:
// 0

// Explanation:
// Invalid date 39 in December.

// Example Input/Output 4:
// Input:
// 29-02-2021

// Output:
// 0

// Explanation:
// Invalid date 29 in February (2021 is not a leap year).


















#include <stdio.h>
#include <stdlib.h>
           

#include<string.h>
int validateDate(char *dateStr)
{
    int year, month, dat;
    sscanf(dateStr,"%d-%d-%d",&dat,&month,&year);
    if(!(month>0 && month <=12))
        return 0;
    int arr[] = {31,0,31,30,31,30,31,31,30,31,30,31};
    if(month != 2){
        int get = arr[month-1];
        if(dat>0 && dat<=get){
            return 1;
        }
        else return 0;
    }
    else{
    
    if(year % 400 == 0) {
          if(dat>0 && dat <=29){
              return 1;
          }else{
              return 0;
          }
    }
       // not a leap year if divisible by 100
       // but not divisible by 400
       else if (year % 100 == 0) {
          if(dat>0 && dat <=28) return 1;
          else return 0;
       }
       // leap year if not divisible by 100
       // but divisible by 4
       else if (year % 4 == 0) {
          if(dat>0 && dat <=29){
              return 1;
          }else{
              return 0;
          }
       }
       // all other years are not leap years
       else {
          if(dat>0 && dat <=28) return 1;
          else return 0;
       }}
}

int main()
{
    char dateStr[11];
    scanf("%s", dateStr);
    printf("%d", validateDate(dateStr));
    return 0;
}