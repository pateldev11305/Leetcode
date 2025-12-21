class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        top=len(stack)-1
        for i in s:
            if not stack:
                stack.append(i)
                top+=1
            elif i==stack[top]:
                stack.pop()
                top-=1
            else:
                stack.append(i)
                top+=1
        return "".join(stack)


