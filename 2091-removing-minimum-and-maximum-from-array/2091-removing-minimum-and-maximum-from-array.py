class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        lowest=0
        highest=0
        for i in range(len(nums)):
            if nums[i]<nums[lowest]:
                lowest=i
            if nums[i]>nums[highest]:
                highest=i

        length=len(nums)-1
        leftL=lowest-0
        rightL=length-lowest
        leftH=highest-0
        rightH=length-highest
        total = min(max(leftL,leftH)+1,max(rightL,rightH)+1,(leftL+1)+(rightH+1),(leftH+1)+(rightL+1))
        return total
