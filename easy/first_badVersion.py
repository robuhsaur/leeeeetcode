
class Solution:
    def firstBadVersion(self, n: int) -> int:
        #isBadVersion(version) takes in an int from n and checks if its bad
        # return the lowest num version that is bad
        low = 1
        high = n
        while low < high:
            mid = round((low + high) / 2 ) 
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low