class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dp = dict()
        for i,val in enumerate(nums):
            if val in dp:
                return [dp[val],i]
            else:
                dp[target-val] = i


        
import unittest

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_no_solution(self):
        self.assertIsNone(self.solution.twoSum([1, 2, 3], 7))

    def test_empty_list(self):
        self.assertIsNone(self.solution.twoSum([], 0))

    def test_single_element(self):
        self.assertIsNone(self.solution.twoSum([1], 1))

if __name__ == '__main__':
    unittest.main()