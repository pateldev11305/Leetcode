class Solution:
    def plusOne(self,nums:List[int])->List[int]:
        res=[]
        carry=1
        for i in range(len(nums)-1,-1,-1):
            total=nums[i]+carry
            if total==10:
                res=[0]+res
                carry=1
            else:
                res=[total]+res
                carry=0
        if carry==1:
            res=[1]+res
        return res
