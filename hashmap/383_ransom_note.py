from collections import defaultdict


class Solution:

  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    chars = defaultdict(int)
    for c in magazine:
      chars[c] += 1
    for r in ransomNote:
      chars[r] -= 1
    if any(chars.values < 0):
      return False
    return True

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


""" 383. Ransom Note
Easy
Topics
Companies

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

 

Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

 """
