class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            char_count = [0 for _ in range(26)]
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            key = '*'.join(map(str, char_count))
            g = group.get(key, [])
            g.append(s)
            group[key] = g

        return list(group.values())