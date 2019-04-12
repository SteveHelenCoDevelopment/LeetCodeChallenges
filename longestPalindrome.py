class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = {}
        maxl = 0
        lens = len(s)
        if lens<=1:
            return s
        for ix in range(lens):
            # first consider odd length palindromes search pivoting about cp-1, cp
            lp = rp = ix
            tmpmax = -1 # temporary maximum
            while (s[lp] == s[rp]) and (lp>=0):
                tmpmax +=2
                lp -= 1 # left pointer
                rp += 1 # right pointer
                if (rp == lens or lp<0): break

            maxl = max(tmpmax,maxl)
            if maxl not in cache:
                cache[maxl] = s[lp+1:rp]

            # now consider even length palindromes search pivoting about cp-1, cp
            lp,rp = ix-1,ix
            tmpmax = 0 # temporary maximum
            while (s[lp] == s[rp]) and (lp>=0):
                tmpmax +=2
                lp -= 1 # left pointer
                rp += 1 # right pointer
                if (rp == lens or lp<0): break

            maxl = max(tmpmax,maxl)
            if maxl not in cache:
                cache[maxl] = s[lp+1:rp]

        return cache[maxl]