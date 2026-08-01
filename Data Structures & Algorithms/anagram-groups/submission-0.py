class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs: #O(n)
            key = ''.join(sorted(s)) #O(m logm)
            groups[key].append(s)
        return list(groups.values())

        

            
        