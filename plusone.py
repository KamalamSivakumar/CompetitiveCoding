def plusOne(self, digits: List[int]) -> List[int]:
      num_string = ''.join([str(x) for x in digits])
      temp_num_string = str(int(num_string) + 1)
      final_digits = [int(x) for x in temp_num_string]
      return final_digits
