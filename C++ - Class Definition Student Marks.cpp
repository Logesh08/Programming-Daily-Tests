// C++ - Class Definition Student Marks
// Fill in the missing lines of code to define the class Student so that the program accepts the input value for marks and prints twice the input value as the output.





#include <iostream>
using namespace std;
class Student
{
    public:
    int marks =0;
    Student(int m){
        marks = m;
    }
    int getMarks()
    {
        return marks;
    }
};
int main()
{
    int input;
    cin >> input;
    Student stud {input} ;
    cout << stud.getMarks()*2 ;
    return 0;
}