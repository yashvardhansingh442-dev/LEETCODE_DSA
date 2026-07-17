class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # extra spaces khud handle karta hai
        return " ".join(reversed(words))