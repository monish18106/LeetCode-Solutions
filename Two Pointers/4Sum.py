class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        t = target
        nums.sort()
        ans = []
        i = 0
        while i < n:
            j = i+1
            while j < n:
                l = j+1
                r = n-1
                g = t- nums[i] - nums[j]
                while l < r:
                    if nums[l]+nums[r] == g:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        while l+1 < n and nums[l+1] == nums[l]:
                            l += 1 
                        l +=1
                        r -= 1
                    elif nums[l]+nums[r] > g:
                        r -= 1
                    else:
                        l += 1
                while j+1 < n and nums[j+1] == nums[j]:
                    j += 1
                j += 1
            while i+1 < n and nums[i+1] == nums[i]:
                i += 1
            i+= 1
        return ans

        