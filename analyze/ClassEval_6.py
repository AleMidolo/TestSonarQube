class AvgPartition:
    def __init__(self, lst, limit):
        self.lst = lst
        self.limit = limit

    def setNum(self):
        return self.calculate_size_and_remainder()

    def calculate_size_and_remainder(self):
        size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return size, remainder

    def get(self, index):
        size, remainder = self.setNum()
        start = self.calculate_start_index(index, size, remainder)
        end = self.calculate_end_index(index, start, size, remainder)
        return self.lst[start:end]

    def calculate_start_index(self, index, size, remainder):
        return index * size + min(index, remainder)

    def calculate_end_index(self, index, start, size, remainder):
        end = start + size
        if index + 1 <= remainder:
            end += 1
        return end