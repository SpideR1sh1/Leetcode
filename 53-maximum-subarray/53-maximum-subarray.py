class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currArr = nums[0]
        maxArr = nums[0]
        
        for i in range(1,len(nums)):
            num = nums[i]
            
            currArr = max(num, currArr + num)
            maxArr = max(maxArr, currArr)
            
        return maxArr