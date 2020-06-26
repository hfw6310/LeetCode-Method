class CQueue:

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A and not self.B:
            return -1
        if not self.B:
            while self.A:
                tmp = self.A.pop()
                self.B.append(tmp)
        return self.B.pop()