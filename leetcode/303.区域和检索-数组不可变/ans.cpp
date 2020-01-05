class NumArray {
public:
    int *arr;
    NumArray(vector<int>& nums) {
        int length = nums.size();
        if(length > 0) {
            arr = new int[length];
            arr[0] = nums[0];
            for (int i = 1; i < length; i++) {
                arr[i] = arr[i - 1] + nums[i]; 
            }
        }
    }
    int sumRange(int i, int j) {
        if(i == 0) {
            return arr[j];
        }
        return arr[j] - arr[i - 1];        
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
