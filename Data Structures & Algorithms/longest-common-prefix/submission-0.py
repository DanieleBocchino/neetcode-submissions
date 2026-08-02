class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for c in strs[0]:
            prefix += c
            for s in strs:
                if s[:len(prefix)] != prefix:
                    return prefix[:-1]
        return prefix
