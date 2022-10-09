class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occ = 0
        index = 1
        for i in range(len(nums)):
            if nums[i] != val:
                nums[occ] = nums[i]
                occ += 1
        return occ
                    
                    