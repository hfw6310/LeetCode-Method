class Solution:
    def findNthDigit(self, n: int) -> int:
        # 首先判断target是几位数，用digits表示
        base = 9
        digits = 1
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        # 计算target的值
        idx = n % digits  # 注意由于上面的计算，n现在表示digits位数的第n个数字
        if idx == 0:
            idx = digits
        number = 1
        for i in range(1,digits):
            number *= 10
        if idx == digits:
            number += n // digits - 1
        else:
            number += n // digits
        # 找到target中对应的数字
        for i in range(idx,digits):
            number //= 10
        return number % 10