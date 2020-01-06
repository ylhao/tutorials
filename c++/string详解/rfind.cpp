#include <iostream>
#include <string>
using namespace std;

int main(){
    string s1 = "first second third";
    string s2 = "second";
    int index = s1.rfind(s2,5);
    // int index = s1.rfind(s2,6);
    // int index = s1.rfind(s2,7);
    if(index < s1.length())
        cout<<"Found at index : "<< index <<endl;
    else
        cout<<"Not found"<<endl;
    return 0;
}