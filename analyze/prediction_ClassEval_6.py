class AvgPartition:
    def __init__(self, lst, limit):
        self.lst = lst
        self.limit = limit

    def setNum(self):
        return self.calculateSizeAndRemainder()

    def calculateSizeAndRemainder(self):
        size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return size, remainder

    def get(self, index):
        size, remainder = self.setNum()
        start = self.calculateStartIndex(index, size, remainder)
        end = self.calculateEndIndex(index, start, size, remainder)
        return self.lst[start:end]

    def calculateStartIndex(self, index, size, remainder):
        return index * size + min(index, remainder)

    def calculateEndIndex(self, index, start, size, remainder):
        end = start + size
        if index + 1 <= remainder:
            end += 1
        return end