class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = s = r =0
        j = len(height)-1
        while i < j:
            s = min(height[i],height[j])*abs(i-j)
            r = max(r,s)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return r


            
            
             


    
                    

                
