class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        if not slen: return ""
        for sublen in range(slen):
            for x in range(sublen+1):
                tmps = s[sublen-x:slen-x]
                if tmps==tmps[::-1]:
                    return (s[sublen-x:slen-x])
        # the routine will eventually return as an single char is a palindrome      
