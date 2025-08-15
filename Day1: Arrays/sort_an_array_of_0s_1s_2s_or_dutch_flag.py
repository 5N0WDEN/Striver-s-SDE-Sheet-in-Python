class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        k = 0
        while k <= j and k < len(nums):
            if nums[k] == 0:
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                i += 1
                k += 1
            elif nums[k] == 1:
                k += 1
            elif nums[k] == 2:
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                j -= 1
        return nums
