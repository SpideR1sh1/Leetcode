class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                add = nums[i] + nums[l] + nums[r]
                if add == 0:
                    res.append([nums[i], nums[l], nums[r]]) 
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif add < 0:
                    l += 1
                else:
                    r -= 1
        return res 
