class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for s1 in s:
            freq[s1] = freq.get(s1, 0) + 1

        for t1 in t:
            if not t1 in freq or freq[t1] == 0:
                return False
            freq[t1] -= 1
        return True
                
        