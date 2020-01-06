#include <iostream>
#include <string>
using namespace std;

int main(){
    string s1;
    string s2 = "c plus plus";
    string s3 = s2;
    string s4 (5, 's');

    string s = "http://c.biancheng.net";
    int len = s.length();  // 返回真实长度
    cout<<len<<endl;

    string path = "D:\\demo.txt";
    const char *path1 = path.c_str();  // 返回 C 风格的字符串
    cout << path << endl;
    cout << path1 <<endl;

    return 0;
}