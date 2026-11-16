class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum())
        w = cleaned.lower()
        l = len(w)
        l_half = l//2
        if l%2 == 0:
            #even
            for i in range(0, l_half):
                if w[l_half + i] == w[l_half - i -1]:
                    continue
                else:
                    return False
            return True
        else:
            #odd
            for i in range(1, l_half +1):
                if w[l_half + i] == w[l_half - i]:
                    continue
                else:
                    return False
            return True
