class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l = 0
        r = len(tokens)-1
        s = 0
        mx = 0
        tokens.sort()
        if len(tokens) == 1 and power < tokens[0]:
            return 0
        elif len(tokens) == 1:
            return 1
        else:
            while l <= r:
                if l == 0 and power < tokens[l]:
                    return 0
                if power >= tokens[l]:
                    power -= tokens[l]
                    s += 1
                    l += 1
                else:
                    if s > 0:
                        s -= 1
                        power += tokens[r]
                        r -= 1
                mx = max(s,mx)
        return mx
