class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for c in s:
            if not len(l) and (c == ')' or c == ']' or c == '}'):
                return False

            if (c == ')' and (l[-1] == '[' or l[-1] == '{')) or \
               (c == ']' and (l[-1] == '(' or l[-1] == '{')) or \
               (c == '}' and (l[-1] == '(' or l[-1] == '[')):
               return False

            if (c == ')' and l[-1] == '(') or \
               (c == ']' and l[-1] == '[') or \
               (c == '}' and l[-1] == '{'):
               l.pop()
               continue
            l.append(c)
        return not len(l)