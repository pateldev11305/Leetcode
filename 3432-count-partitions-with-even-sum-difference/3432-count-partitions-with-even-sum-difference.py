class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        if len(nums)==1:
            return 0
        else:

            for partition in range(1,len(nums)):
                lArr,rArr=0,0

                for i in range(0,len(nums)):

                    if i<partition:
                        lArr+= nums[i]
                    else:
                        rArr+= nums[i]

                total = lArr - rArr
                if total%2 == 0:
                    count+=1
        return count