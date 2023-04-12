class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = [x for x in path.split('/') if x]
        stack = []
        for x in temp:
            if x!='.' and x!='..' :
                stack.append(f"/{x}")
            elif x =='..' and stack:
                stack.pop()
        string = "".join(stack)
        if not string.startswith('/'):
            return f"/{string}"
        return string
