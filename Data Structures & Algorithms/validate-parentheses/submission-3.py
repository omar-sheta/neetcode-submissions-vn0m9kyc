class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', ']':'[', ')':'('}

        for br in s:
            if br in mapping.keys():
                # check if top of stack is closing of same type
                if stack and stack[-1] != mapping[br]:
                    return False
                elif not stack:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(br)

        return len(stack) == 0
        