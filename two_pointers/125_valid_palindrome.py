class Solution:
  def isPalindrome(self, s: str) -> bool:
    alpha_and_symbols = list(s)
    alpha = [char.lower() for char in alpha_and_symbols if char.isalnum()]
    n = len(alpha)
    a = 0
    b = n-1
    while a < b:
      if alpha[a] != alpha[b]:
        return False 
      else:
        a += 1
        b -= 1
    return True
        
        
        
# ======================================================== #
# ======================================================== #
# ======================================================== #
        
""" 125. Valid Palindrome
Easy
Topics
Companies

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

 """