class Solution:
    def isPalindrome(self, s: str) -> bool:

        str = ""

        for letter in s:
            if letter.isalnum():
                str += letter.lower()

        return str == str[::-1]
