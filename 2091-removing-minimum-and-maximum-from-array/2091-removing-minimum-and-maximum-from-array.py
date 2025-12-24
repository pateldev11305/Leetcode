class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        min_index = 0
        max_index = 0

        # Find indices of min and max elements
        for i in range(n):
            if nums[i] > nums[max_index]:
                max_index = i
            if nums[i] < nums[min_index]:
                min_index = i

        # Calculate deletions from different sides
        delete_from_front = max(max_index, min_index) + 1
        delete_from_back = n - min(max_index, min_index)
        delete_from_both_side = (min(max_index, min_index) + 1) + (n - max(max_index, min_index))

        # Return minimum of all options
        return min(delete_from_both_side, delete_from_front, delete_from_back)