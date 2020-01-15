class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left=0;
        int right=nums.size();
        int mid;
        vector<int> res;
        while (left < right) {  // 找左边界
            mid = left + (right - left) / 2;
            if (nums[mid] >= target)
                right = mid;
            else
                left = mid + 1;
        }
        if (left == nums.size() || nums[left] != target)
            return res={-1, -1};
        if (nums[left] == target)
            res.emplace_back(left);
        right = nums.size();
        while (left < right){    // 找右边界
            mid = left + (right - left) / 2;
            if (nums[mid] <= target) 
                left=mid + 1;
            else 
                right = mid;
        }
        if (nums[right - 1] == target)
            res.emplace_back(right - 1);
        return res;
    }
};
