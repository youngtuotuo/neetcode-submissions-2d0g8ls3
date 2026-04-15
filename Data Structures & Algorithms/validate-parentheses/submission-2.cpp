class Solution {
public:
    bool isValid(string s) {
        char stack[1000] = {0};
        int stack_idx = -1;
        int i = 0;
        while (s[i] != '\0') {
            char c = s[i];
            if (c == '{' || c == '[' || c == '(') {
                stack[++stack_idx] = c;
            } else if (c == '}' || c == ']' || c == ')') {
                if (stack_idx < 0) return 0;
                char prev = stack[stack_idx];
                if ((c == ')' && prev != '(') ||
                    (c == ']' && prev != '[') ||
                    (c == '}' && prev != '{')) {
                    return 0;
                }
                stack_idx--;
            }
            i++;
        }
        return (stack_idx == -1);
    }
};
