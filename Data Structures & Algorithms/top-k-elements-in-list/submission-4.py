class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        buckets = [[] for _ in nums]
        for num, cnt in count.items():
            buckets[cnt-1].append(num)
        res = []
        for bkt in buckets[::-1]:
            for num in bkt:
                res.append(num)
                if len(res) == k:
                    return res