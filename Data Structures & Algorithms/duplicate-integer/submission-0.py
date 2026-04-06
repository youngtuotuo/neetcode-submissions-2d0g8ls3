class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for index, num in enumerate(nums):
            c = count.get(num, 0)
            if c > 0:
                return True
            count[num] = c + 1
        return False