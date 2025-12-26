class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(set(nums)) == len(nums):
            return False

        window_map = set()

        left = 0

        for right in range(len(nums)):

            if right - left > k:
                window_map.remove(nums[left]) # remove oldest element from window
                left += 1
            
            if nums[right] in window_map:
                return True

            window_map.add(nums[right]) 
        
        return False

        