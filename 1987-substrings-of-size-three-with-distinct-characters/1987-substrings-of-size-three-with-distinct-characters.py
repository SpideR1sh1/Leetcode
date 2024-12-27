class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        l = 0
        seen = {}

        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = 1
            else:
                seen[s[r]] += 1
            
            if r - l == 3:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    seen.pop(s[l])
                l += 1
            if len(seen) == 3:
                count += 1
        return count