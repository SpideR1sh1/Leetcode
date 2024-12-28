class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n):
            l = i+1
            r = n-1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l+= 1
                    r-= 1
                elif sum < 0:
                    l+= 1
                elif sum > 0:
                    r-= 1
        return list(res)