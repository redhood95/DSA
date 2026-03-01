# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] +=1
            else:
                s_map[s[i]] = 1

            if t[i] in t_map:
                t_map[t[i]] +=1
            else:
                t_map[t[i]] = 1
        return s_map == t_map
    
    def isAnagram_single_map(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        return all(v == 0 for v in count.values())
            
