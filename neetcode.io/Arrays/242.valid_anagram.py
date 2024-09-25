# https://leetcode.com/problems/valid-anagram/



from collections import Counter

class Solution(object):
    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return  sorted(list(s)) == sorted(list(t))

    def isAnagram2(self, s, t):
        """
        Check if two strings are anagrams using the Counter class from the collections module.

        The Counter class is a dictionary subclass that helps count hashable objects. 
        It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

        :type s: str
        :type t: str
        :rtype: bool
        :return: True if the strings are anagrams, False otherwise
        """
        return Counter(s) == Counter(t)
    def isAnagram3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dp1, dp2  = dict(),dict()
        for i in s:
            if i in dp1:
                dp1[i] +=1
            else:
                dp1[i] = 1

        for i in t:
            if i in dp2:
                dp2[i] +=1
            else:
                dp2[i] = 1
        
        return dp1 == dp2
        

import unittest

class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isAnagram1_true(self):
        self.assertTrue(self.solution.isAnagram1("anagram", "nagaram"))

    def test_isAnagram1_false(self):
        self.assertFalse(self.solution.isAnagram1("rat", "car"))

    def test_isAnagram2_true(self):
        self.assertTrue(self.solution.isAnagram2("anagram", "nagaram"))

    def test_isAnagram2_false(self):
        self.assertFalse(self.solution.isAnagram2("rat", "car"))

    def test_isAnagram3_true(self):
        self.assertTrue(self.solution.isAnagram3("anagram", "nagaram"))

    def test_isAnagram3_false(self):
        self.assertFalse(self.solution.isAnagram3("rat", "car"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram1("", ""))
        self.assertTrue(self.solution.isAnagram2("", ""))
        self.assertTrue(self.solution.isAnagram3("", ""))

    def test_single_character(self):
        self.assertTrue(self.solution.isAnagram1("a", "a"))
        self.assertFalse(self.solution.isAnagram1("a", "b"))
        self.assertTrue(self.solution.isAnagram2("a", "a"))
        self.assertFalse(self.solution.isAnagram2("a", "b"))
        self.assertTrue(self.solution.isAnagram3("a", "a"))
        self.assertFalse(self.solution.isAnagram3("a", "b"))

if __name__ == '__main__':
    unittest.main()
