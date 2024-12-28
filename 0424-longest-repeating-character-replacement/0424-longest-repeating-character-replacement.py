class Solution:
    # Sliding Window - track the maxFreq -> to calculate the number of replacements in current window
    # If replacements needed are more than k, then we shrink the window
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = defaultdict(int)
        maxFreq = 0
        for right, c in enumerate(s):
            freq[c] += 1
            if freq[c] > maxFreq:
                maxFreq = freq[c]
            if right - left + 1 - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
        return len(s) - left