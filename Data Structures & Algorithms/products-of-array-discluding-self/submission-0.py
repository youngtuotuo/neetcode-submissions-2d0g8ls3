class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        out = [1 for _ in range(size)]
        for i in range(size):
            for n in nums[i+1:]:
                out[i] *= n
        for i in range(size - 1, 0, -1):
            for n in nums[:i]:
                out[i] *= n
        return out

        


"""
[1,2,4,6]


e 1 1 1
2 e 2 2
4 4 e 4
6 6 6 e
"""