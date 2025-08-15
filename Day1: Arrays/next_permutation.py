class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        flag = False
        # Checking the maxima exists or not
        for idx in range(1, len(nums)):
            if nums[-idx] > nums[-(idx + 1)]:
                flag = True
                break
        if flag:
            # Finding the maxima from end and replacing the value
            for i in range(1, idx + 1):
                if nums[-(idx + 1)] < nums[-i]:
                    temp = nums[-i]
                    nums[-i] = nums[-(idx + 1)]
                    nums[-(idx + 1)] = temp
                    break
            # Reversing till the maxima
            for i in range(1, (idx>>1) + 1):
                temp = nums[-i]
                nums[-i] = nums[-(idx-i+1)]
                nums[-(idx-i+1)] = temp
        else:
            # Reverse it
            for i in range(1, (len(nums)>>1) + 1):
                temp = nums[-i]
                nums[-i] = nums[-(len(nums)-i+1)]
                nums[-(len(nums)-i+1)] = temp     
        return nums
