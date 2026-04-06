class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        def encode(s):
            l = [0] * 26
            for c in s:
                l[ord(c) - ord('a')] += 1
            return '#'.join(map(str, l))
        for s in strs:
            group.setdefault(encode(s), []).append(s)
        return list(group.values())