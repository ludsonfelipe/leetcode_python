class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s = [True for l in s if s.count(l)==t.count(l)]
            if len(s)==len(t):
                return True
            else:
                return False