class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp=[]
        count=0
        for i in nums:
            if i==val:
                count+=1
            else:
                temp.append(i)
        nums[:]=temp
        return len(nums)