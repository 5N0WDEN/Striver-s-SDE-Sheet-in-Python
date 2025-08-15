class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lcs = float('-inf')
        cs = 0
        for num in nums:
            cs += num
            if num > cs:
                cs = num
            if lcs < cs:
                lcs = cs
        return lcs
