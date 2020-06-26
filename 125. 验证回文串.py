class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 双指针
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            while left < right and not s[left].isalnum():  # Python isalnum()方法检测字符串是否由字母和数字组成。

                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():  ##### .lower() 把字母转换成小写
                return False  ##### .upper() 把字母转换成大写
            left += 1
            right -= 1
        return True