class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> output(nums.size(), 1);
        int i;
        for (i = 1; i < nums.size(); i++)
        {
            output[i] = output[i-1] * nums[i-1];
        }
        int postfix = 1;
        for (i = nums.size() - 1; i >= 0; i--)
        {
            output[i] *= postfix;
            postfix *= nums[i];
        }
        return output;

    }
};

/*
3 2 4 6
-------
e 3 3 3
2 e 2 2
4 4 e 4
6 6 6 e
*/
