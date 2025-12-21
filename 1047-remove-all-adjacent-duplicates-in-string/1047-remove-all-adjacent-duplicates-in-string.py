class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in s:
            top=len(stack)-1
            if not stack:
                stack.append(i)
            elif i==stack[top]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)


