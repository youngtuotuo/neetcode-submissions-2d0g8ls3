class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        out = [1 for _ in range(size)]
        for i in range(size):
            for n, m in zip(nums[i+1:], nums[:size-1-i]):
                out[i] *= n
                out[size-1-i] *= m

        return out