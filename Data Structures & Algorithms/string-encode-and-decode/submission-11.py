class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += f"{len(s)};{s}"
        return out
        
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i+1
            while s[j] != ";":
                j+=1
            num = int(s[i:j])
            out.append(s[j+1:j+num+1])
            i = j+num+1
        return out