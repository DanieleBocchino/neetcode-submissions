class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_v = count = 0

        # [1,1,0,1,1,1]

        for i in nums:
            if i == 1:
                count += 1
            else:
                if count > max_v:
                    max_v = count 
                count = 0
        if count > max_v:
            max_v = count 
            
        return max_v