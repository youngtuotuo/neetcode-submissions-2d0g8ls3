class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            c = count.get(num, 0)
            count[num] = c + 1
        freq = []
        for num, c in count.items():
            freq.append((c, num))

        freq = sorted(freq, key=lambda x: x[0], reverse=True)

        return [f[1] for f in freq[:k]]