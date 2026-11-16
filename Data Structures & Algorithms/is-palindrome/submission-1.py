class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum())
        w = cleaned.lower()
        l = len(w)
        l_half = l//2
        for i in range(l_half):
            if w[i] == w[i+l-(2*i+1)]:
                continue
            else:
                return False
        return True