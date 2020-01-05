class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        findPermute(0, nums, ans);
        return ans;
    }

    void findPermute(int cur, vector<int>& nums, vector<vector<int>>& ans) {
        if (cur == nums.size() - 1) {
            ans.push_back(nums);
            return;
        }
        for (int i = cur; i < nums.size(); i++) {
            swap(nums[cur], nums[i]);
            findPermute(cur + 1, nums, ans);
            swap(nums[cur], nums[i]);
        }
    }
};
