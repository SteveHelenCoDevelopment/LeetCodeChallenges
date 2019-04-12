# Test file for calling imported library functions
import unittest
from longestPalindrome import Solution

class TestPalindromeSuite(unittest.TestCase):

    def test_longer(self):
        y = Solution()
        test_cases = ["aaaa","aba","abasskjhghjkz","abasskjhgghjkz"]
        responses = ["aaaa","aba","kjhghjk","kjhgghjk"]
        for i in range(len(test_cases)):
            self.assertEqual(y.longestPalindrome(test_cases[i]), responses[i])

    def test_extreme(self):
        y = Solution()
        test_cases = ["","a"," "]
        responses = ["","a"," "]
        for i in range(len(test_cases)):
            self.assertEqual(y.longestPalindrome(test_cases[i]), responses[i])

if __name__ == '__main__':
    unittest.main()
