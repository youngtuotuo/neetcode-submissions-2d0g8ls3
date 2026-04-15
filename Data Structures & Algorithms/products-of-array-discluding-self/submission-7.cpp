class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> output(nums.size(), 1);
        for (int i = 0; i < nums.size(); i++) 
        {
            for (int j = i+1; j < nums.size(); j++)
            {
                output[i] *= nums[j];
            }

            for (int j = nums.size() - i - 2; j >= 0; j--)
            {
                output[nums.size() - 1 - i] *= nums[j];
            }
        }
        return output;

    }
};
