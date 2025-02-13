def fill(self, coord, weight=1):
    if not (0 <= coord[0] < self.width and 0 <= coord[1] < self.height):
        return
    self.histogram[coord] += weight