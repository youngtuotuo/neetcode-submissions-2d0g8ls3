class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += f";{len(s)};{s}"
        return out
        
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        # ";5;Hello;5;World"
        while i < len(s):
            j = i+1
            while s[j] != ";":
                j+=1
            print(i, j)
            num = int(s[i+1:j])
            out.append(s[j+1:j+num+1])
            i = j+num+1
        return out