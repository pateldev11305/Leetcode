class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m=len(nums1)
        n=len(nums2)
        l=0
        h=m

        while l<=h:
            mid=(l+h)//2
            num1Part=mid
            num2Part=(m+n+1)//2-num1Part
            if num1Part==0:
                left1=float('-inf')
            else:
                left1=nums1[num1Part - 1]
            if num1Part==m:
                right1=float('inf')
            else:
                right1=nums1[num1Part]
            if num2Part==0:
                left2=float('-inf')
            else:
                left2=nums2[num2Part-1]

            if num2Part==n:
                right2=float('inf')
            else:
                right2=nums2[num2Part]
            if left1<=right2 and left2<=right1:
                if (m+n)%2==0:
                    left_max =max(left1, left2)
                    right_min =min(right1, right2)
                    median=(left_max+right_min)/2
                    return median
                else:
                    median= max(left1,left2)
                    return median
            if left1>right2:
                h=mid - 1
            else:
                l=mid + 1
