#include <iostream>
#include <string>
using namespace std;

int main(){
    string s1 = "first second third";
    string s2 = "first";
    // string s2 = "second";
    // string s2 = "third";
    int index = s1.find(s2,5);
    if(index < s1.length())
        cout<<"Found at index : "<< index <<endl;
    else
        cout<<"Not found"<<endl;
    return 0;
}