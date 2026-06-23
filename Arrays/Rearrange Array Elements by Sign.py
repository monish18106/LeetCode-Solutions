class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = [] 
        p = []
        for i in nums:
            if i < 0:
                n.append(i)
            else:
                p.append(i)
        a = []
        for i in range(len(nums)//2):
            a.append(p[i])
            a.append(n[i])
        return a



            


            


        
