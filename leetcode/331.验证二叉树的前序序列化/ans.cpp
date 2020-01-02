class Solution {
public:
    bool isValidSerialization(string preorder) {
        if (preorder.size() == 0) return false;
        istringstream is(preorder);
        string str = "";
        vector<string> v;
        while (getline(is, str, ',')) v.push_back(str);
        int cnt = 0;
        for (int i = 0; i < v.size() - 1; i++) {
            if (v[i] == "#") {
                if (!cnt) return false;
                cnt --;
            } else {
                cnt ++;
            }
        }
        return cnt == 0 && v.back() == "#";
    }
};
