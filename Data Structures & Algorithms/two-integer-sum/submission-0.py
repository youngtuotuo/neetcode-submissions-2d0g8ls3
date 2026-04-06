class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2index = {}
        for index, num in enumerate(nums):
            remain = target - num
            remain_index = num2index.get(remain)
            if remain_index is not None:
                return [remain_index, index]
            num2index[num] = index
            print(num2index)