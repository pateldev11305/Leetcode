class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m+i] = nums2[i]
        size = m + n
        for i in range(size):
            for j in range(0, size - 1):
                if nums1[j] > nums1[j+1]:
                    nums1[j], nums1[j+1] = nums1[j+1], nums1[j]

        