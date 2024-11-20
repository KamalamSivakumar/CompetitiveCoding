class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for ele in nums:
            if nums.count(ele) == 1:
                return ele
            else:
                continue
