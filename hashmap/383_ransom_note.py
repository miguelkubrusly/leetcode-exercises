from collections import Counter


class Solution:

  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    magazine_counts = Counter(magazine)
    ransom_counts = Counter(ransomNote)
    for char, count in ransom_counts.items():
      if magazine_counts[char] < count:
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
