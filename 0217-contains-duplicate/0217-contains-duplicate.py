class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cpy = set()
        for i in nums:

            if i in cpy:
                return True
            cpy.add(i)
        return False

        

