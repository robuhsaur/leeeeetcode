# sets only contain unique elements

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set_nums = set()
        for x in nums:
            if x in set_nums:
                return True
            set_nums.add(x)
        return False
    


# return False if the len(set) != len(nums)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums)) 