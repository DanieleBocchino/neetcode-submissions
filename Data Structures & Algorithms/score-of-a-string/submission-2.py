class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(1, len(s)):
            this_val = ord(s[i])
            prev_val = ord(s[i - 1])
            sum += abs(this_val - prev_val)
        return sum
