# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.


class Solution:

    def validPalindrome(self, s):
        
        def checkpalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1
        s = s.lower()    
        while left < right:
            if s[left] != s[right]:
                return checkpalindrome(s, left + 1, right) or checkpalindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True
    
    
if __name__ == "__main__":
    s ="abca"
    print(Solution().validPalindrome(s)) # True    