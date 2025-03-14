# 1249. Minimum Remove to Make Valid Parentheses
# Difficulty: Medium

# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' , ')', or lowercase English letter.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Track indices to remove
        to_remove = set()
        # Stack to keep track of opening parenthesis indices
        stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:  # If we have a matching opening parenthesis
                    stack.pop()
                else:  # No matching opening parenthesis, mark for removal
                    to_remove.add(i)
        
        # Any indices remaining in stack are unmatched opening parentheses
        to_remove.update(stack)
        
        # Build the result string, skipping characters at indices in to_remove
        return ''.join(char for i, char in enumerate(s) if i not in to_remove)

            
if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    print(Solution().minRemoveToMakeValid(s)) # "lee(t(c)o)de"

    s = "a)b(c)d"
    print(Solution().minRemoveToMakeValid(s)) # "ab(c)d"

    s = "))(("
    print(Solution().minRemoveToMakeValid(s)) # ""

