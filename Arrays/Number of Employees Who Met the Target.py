class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c = int(0)
        for i in hours:
            if i >= target:
                c += 1 
        return c