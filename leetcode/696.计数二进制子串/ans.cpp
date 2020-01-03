class Solution {
public:
    int countBinarySubstrings(string s) {
        int length = s.length();
        if (length == 0) {
            return 0;
        }
        int *group = new int[length];
        int index = 0;
        group[index] = 1;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s[i] != s[i+1]) {
                group[++index] = 1;
            } else {
                group[index] ++;
            }
        }
        int res = 0;
        for (int i = 0; i < index; i++) {
            res += min(group[i], group[i+1]);
        }
        return res;
    }
};
