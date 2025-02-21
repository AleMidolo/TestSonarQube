def fill(self, coord, weight=1):
    """
    Riempie l'istogramma alla posizione *coord* con il peso specificato *weight*.
    """
    if coord < 0 or coord >= len(self.histogram):
        raise IndexError("Coordinate fuori dai limiti dell'istogramma.")
    self.histogram[coord] += weight