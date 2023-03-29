#First solution

def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):
            for p in range(i + 1, len(nums)):
                if nums[i] + nums[p] == target:
                    return [i, p]    
        return []



#Second solution

def twoSum(self, nums: List[int], target: int) -> List[int]:
    #store the values and their indexes inside dict
    bruh = {}
    # iterate over each item in nums and place it 
    for key, val in enumerate(nums):
        diff = target - val
        if diff in bruh:
            return [bruh[diff], key]
        bruh[n] = key
    return