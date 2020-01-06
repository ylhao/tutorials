#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1 = "s1abc";
    string s2 = "s2abc";
    char *s3 = "s3abc";
    char s4[] = "s4abc";
    char ch = '@';

    string s5 = s1 + s2;
    string s6 = s1 + s3;
    string s7 = s1 + s4;
    string s8 = s1 + ch;

    cout << s5 << endl;
    cout << s6 << endl;
    cout << s7 << endl;
    cout << s8 << endl;

    return 0;
}