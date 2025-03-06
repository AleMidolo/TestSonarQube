def fill(self, coord, weight=1):
    """
    Llena el histograma en *coord* con el *weight* dado.

    Las coordenadas fuera de los límites del histograma son ignoradas.
    """
    if 0 <= coord < len(self.histogram):
        self.histogram[coord] += weight