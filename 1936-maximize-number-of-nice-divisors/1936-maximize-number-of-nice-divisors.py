class Solution:
    def maxNiceDivisors(self, X: int) -> int:
        return X if X <= 3 else (
            pow(3, X // 3, 10**9+7) if X % 3 == 0 else (
                (pow(3, (X-4) // 3, 10**9+7) * 4) % (10**9+7) if X % 3 == 1 else 
                (2 * pow(3, X // 3, 10**9+7)) % (10**9+7)
            )
        )