class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0 for _ in range(26)]
        for c in s:
            char_count[ord(c) - ord('a')] +=1
        for c in t:
            char_count[ord(c) - ord('a')] -=1
        for count in char_count:
            if count != 0:
                return False
        return True