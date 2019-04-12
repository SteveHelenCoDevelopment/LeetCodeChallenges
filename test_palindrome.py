# Test file for calling imported library functions

from longestPalindrome import Solution


def main():
    y = Solution()
    x = y.longestPalindrome('jjghefiooifellabbxb')
    print(x)

if __name__=="__main__":
    main()     