 def removeDuplicates(self, nums: List[int]) -> int:
      dict_keys = dict.fromkeys(nums)
      nums[:] = list(dict_keys.keys())
