#include <cstring>
#define TABLE_SIZE 262144
#define MASK (TABLE_SIZE - 1)

static int table[TABLE_SIZE];
static bool used[TABLE_SIZE];

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    memset(used, 0, sizeof(used));
    for (int i = 0; i < nums.size(); i++) {
        unsigned int idx = (nums[i] * 2654435769) & MASK;
        while (used[idx]) {
            if (table[idx] == nums[i]) return true;
            idx = (idx+1) & MASK;
        }
        table[idx] = nums[i];
        used[idx] = true;
    }
    return false;
    }
};