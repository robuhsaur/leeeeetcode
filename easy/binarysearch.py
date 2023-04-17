class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize low as 0 instead of 1 to handle edge case of single item list
		low = 0
        high = len(nums) - 1 
        mid = 0
				
		# low <= high to handle low and high being the same number (single item list)
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target: 
                high = mid - 1
        return -1