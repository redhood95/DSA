# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uni = set()
        for i in nums:
            if i in uni:
                return True
            else:
                uni.add(i)
        return False
