class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        right=n
        res=[]
        for left in range(n):
            res.append(nums[left])
            res.append(nums[right])
            right+=1
        return res