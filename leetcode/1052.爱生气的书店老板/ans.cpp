class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int X) {
        int res = 0;
        // 计算不生气的总收益
        for (int i = 0; i < customers.size(); i++) {
            res += customers[i] * (1 - grumpy[i]);
        }
        int max_add = 0;
        // 计算滑动窗口内均不生气(1->0)会增加的收益
        for (int i = 0; i < X; i++) {
            max_add += customers[i] * grumpy[i];
        }
        int last = max_add;
        for(int i=X; i<customers.size(); i++){
            int right = customers[i] * grumpy[i];
            int left = customers[i-X] * grumpy[i-X];
            last = right - left + last;
            max_add = max(max_add, last);
        }
        return res + max_add;

    }
};