class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # 如果L小于1，直接返回不存在
        # 否则会返回1（code_s的初始化值是0 L也是0 后续的编码就都是0了）
        # 虽然输出1并不影响最后的结果 S_org[1, 1] 但总觉得怪怪的
        if L < 1:
            return -1
        # 依次截取S中L个元素
        # 先计算第一个元素和aL
        code_s = 0
        for i in range(L):
            code_s = (code_s * a + S[i]) % modules
        set_s = {code_s}
        aL = a ** L % modules
        # 由第一个元素和aL依次计算其他长为L的序列编码
        for start in range(1, n - L + 1):
            code_s = (code_s * a - S[start - 1] * aL + S[start + L - 1]) % modules
            if code_s in set_s:
                return start
            set_s.add(code_s)
        return -1

    def longestDupSubstring(self, S_org: str) -> str:
        S = [ord(s) - ord('a') for s in S_org]
        n = len(S)
        # 注意：为了使单个元素的数组也能进入while循环，right初始为n，而不是n-1
        # 即left指向子串第一个坐标处，right指向子串最后一个坐标后一位
        # 子串长度为right-left，不用再+1
        left, right = 0, n
        while right - left > 0:  # 长度>0的时候进入循环
            L = (right + left) // 2  # 计算L(序列长度为偶数时L指向中间连个数字的后一个)))
            # print('left L right:', left, L, right)
            # 判断S中有没有长度为L的重复子串
            # 如果有
            if self.is_duplicate(L, S, n) != -1:
                left = L + 1
            else:
                right = L
        # 计算最后的结果
        # 由达到要求时候的跳出时候的left和right计算L
        L = left - 1
        start = self.is_duplicate(L, S, n)
        return S_org[start: start + L] if start != -1 else ""