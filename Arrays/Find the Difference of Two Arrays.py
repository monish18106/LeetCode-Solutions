class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = []
        b = []
        for i in nums1:
            if i in nums2:
                pass
            else:
                a.append(i)
        for i in nums2:
            if i in nums1:
                pass
            else:
                b.append(i)
        c = [list(set(a)),list(set(b))]
        return c
