from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1
        
        return heapq.nlargest(k, count, key=count.get)
        


        