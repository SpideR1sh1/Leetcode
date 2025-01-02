class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Time: n/2 => O(N)
        # Space: O(1)

        def isPalindrome(s, l, r): # general palindrome case
            while (l < r):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # here we can remove atmost one character and check where is it a palindrome - so as s[l] and s[r] are not same, we need to skip 
                # CASE 1: either s[l] to do so we need to pass args as l+1, r, 
                # CASE 2: or s[r] to do so we need to pass args as l, r-1
                return isPalindrome(s, l + 1, r) or isPalindrome(s, l, r - 1)
            l += 1
            r -= 1

        return True