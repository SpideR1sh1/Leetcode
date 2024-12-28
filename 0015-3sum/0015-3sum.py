class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return res