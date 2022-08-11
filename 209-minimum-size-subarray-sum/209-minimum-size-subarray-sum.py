class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0;
        currSum = 0
        minDist = math.inf
        for r in range(0, len(nums)):
            currSum += nums[r]
            
            while (currSum >= target):
                minDist = min(minDist, r - l + 1)
                currSum -= nums[l]
                l += 1
        if minDist == math.inf:
            return 0
        
        return minDist
    