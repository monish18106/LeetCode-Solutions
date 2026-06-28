class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mindiff = 10**9
        closetsum = 0
        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n-1
            while j < k:
                currsum = nums[i]+nums[j]+nums[k]
                currdiff = abs(currsum - target)
                if currdiff < mindiff:
                    mindiff = currdiff
                    closetsum = currsum
                if currsum < target:
                    j += 1
                else:
                    k -= 1
        return closetsum
    



        