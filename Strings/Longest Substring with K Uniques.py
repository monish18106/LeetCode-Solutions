class Solution:
    def longestKSubstr(self, s, k):
        freq = [0] * 26
        left = 0
        distinct = 0
        ans = -1

        for right in range(len(s)):
            idx = ord(s[right]) - ord('a')

            if freq[idx] == 0:
                distinct += 1
            freq[idx] += 1

            while distinct > k:
                idx = ord(s[left]) - ord('a')
                freq[idx] -= 1

                if freq[idx] == 0:
                    distinct -= 1

                left += 1

            if distinct == k:
                ans = max(ans, right - left + 1)

        return ans