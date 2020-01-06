#include <iostream>
#include <string>
using namespace std;

int main(){
    string s1, s2, s3;
    s1 = s2 = "1234567890";
    s3 = "aaa";
    char *s4 = "bbb";

    s1.insert(5, s3);
    cout<< s1 <<endl;

    s2.insert(5, s4);
    cout<< s2 <<endl;
    return 0;
}