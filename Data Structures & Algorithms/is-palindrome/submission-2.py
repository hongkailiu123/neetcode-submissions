class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        cleaned_length = len(cleaned)
        forward_i = 0
        backward_i = cleaned_length - 1

        while forward_i < backward_i:
            if cleaned[forward_i] != cleaned[backward_i]:
                print(cleaned[forward_i])
                print(cleaned[backward_i])
                return False
            forward_i += 1
            backward_i -= 1


        return True  

        