# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/


# Runtime: 60 ms
# Memory Usage: 13.5 MB
# Your runtime beats 66.20 % of python3 submissions.
# Your memory usage beats 10.51 % of python3 submissions.
# Reference:
# https://www.jiuzhang.com/solution/median-of-two-sorted-arrays/#tag-highlight-lang-python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n%2 == 1:
            return self.findKth(nums1, 0, nums2, 0, n//2+1)
        else:
            return 0.5*(self.findKth(nums1, 0, nums2, 0, n//2) + \
                       self.findKth(nums1, 0, nums2, 0, n//2+1))
        
    def findKth(self, nums1, idx1, nums2, idx2, k):
        if idx1 == len(nums1):
            return nums2[idx2 + k - 1]
        if idx2 == len(nums2):
            return nums1[idx1 + k - 1]
        if k == 1:
            return min(nums1[idx1], nums2[idx2])
        
        A = nums1[idx1 + k//2 - 1] if idx1 + k//2 <= len(nums1) else None
        B = nums2[idx2 + k//2 - 1] if idx2 + k//2 <= len(nums2) else None
        
        if A is None or (B is not None and A > B):
            return self.findKth(nums1, idx1, nums2, idx2 + k//2, k - k//2)
        else:
            return self.findKth(nums1, idx1 + k//2, nums2, idx2, k - k//2)



