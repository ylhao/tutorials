class Solution {
public:
    string strWithout3a3b(int A, int B) {
        // 交换 A,B 和 a,b 的定义，保证 A,a 对应的是多的那个
        string str = "";
        char a = 'a';
        char b = 'b';
        // 最多输出两个相同的就插入一下另一个字符
        if (A < B) {
            swap(A, B);
            swap(a, b);
        }
        while (A > 0 || B > 0) {
            if (A > 0) {
                str.push_back(a);
                A --;
            }
            if (A > B) {
                str.push_back(a);
                A --;
            }
            if (B > 0) {
                str.push_back(b);
                B --;
            }
        }
        return str;
    }
};