class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n = len(nums2)-1
        for i in range(len(nums1)-1,-1,-1):
            if n < 0:
                break
            nums1[i] = nums2[n]
            n -= 1
        nums1.sort()
        
        


        