def fill(self, coord, weight=1):
    """
    Riempie l'istogramma alla posizione *coord* con il peso specificato *weight*.
    """
    if coord in self.histogram:
        self.histogram[coord] += weight
    else:
        self.histogram[coord] = weight