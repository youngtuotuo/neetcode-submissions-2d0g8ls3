class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        out = [1 for _ in range(size)]
        for i in range(size):
            for n in nums[i+1:]:
                out[i] *= n
            for n in nums[:size - 1 - i]:
                out[size-1-i] *= n

        return out