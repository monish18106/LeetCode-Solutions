class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c = 0
        n = len(arr)
        for i in range(k):
            c += arr[i]
        d = 0
        if c//k >= threshold:
            d += 1
        mx = 0
        mx = max(d,mx)
        for i in range(k,n):
            c -= arr[i-k]
            c += arr[i]
            if c//k >= threshold:
                d += 1  
            mx = max(d,mx)
        return mx 
        