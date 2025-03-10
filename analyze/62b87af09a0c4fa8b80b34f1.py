def fill(self, coord, weight=1):
    """
    Llena el histograma en *coord* con el *weight* dado.

    Las coordenadas fuera de los límites del histograma son ignoradas.
    """
    if self.is_within_bounds(coord):
        self.histogram[coord] += weight