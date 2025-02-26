def fill(self, coord, weight=1):
    """
    Llena el histograma en *coord* con el *weight* dado.

    Las coordenadas fuera de los límites del histograma son ignoradas.
    """
    if 0 <= coord[0] < self.width and 0 <= coord[1] < self.height:
        self.histogram[coord[0]][coord[1]] += weight