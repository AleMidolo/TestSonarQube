class AvgPartition:
    def __init__(self, lst, limit):
        self.lst = lst
        self.limit = limit

    def setNum(self):
        size = self.calculateSize()
        remainder = self.calculateRemainder()
        return size, remainder

    def calculateSize(self):
        return len(self.lst) // self.limit

    def calculateRemainder(self):
        return len(self.lst) % self.limit

    def get(self, index):
        size, remainder = self.setNum()
        start = self.calculateStart(index, size, remainder)
        end = self.calculateEnd(index, size, remainder)
        return self.lst[start:end]

    def calculateStart(self, index, size, remainder):
        return index * size + min(index, remainder)

    def calculateEnd(self, index, size, remainder):
        end = (index * size) + min(index, remainder) + size
        if index + 1 <= remainder:
            end += 1
        return end