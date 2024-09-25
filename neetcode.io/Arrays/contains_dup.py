# https://leetcode.com/problems/contains-duplicate/description/



class Solution:
    def containsDuplicate(self, nums) -> bool:
        uni = set()
        for i in nums:
            if i in uni:
                return True
            else:
                uni.add(i)
        return False

import unittest

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_duplicate_true(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))

    def test_contains_duplicate_false(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(self.solution.containsDuplicate([]))

    def test_single_element(self):
        self.assertFalse(self.solution.containsDuplicate([1]))

    def test_multiple_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([1, 1, 1, 1]))

if __name__ == '__main__':
    unittest.main()



