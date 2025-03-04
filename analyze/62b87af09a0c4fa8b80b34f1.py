def fill(self, coord, weight=1):
    """
    Llena el histograma en *coord* con el *weight* dado.

    Las coordenadas fuera de los límites del histograma son ignoradas.
    """
    # Verificar que las coordenadas estén dentro de los límites
    for i, c in enumerate(coord):
        if c < 0 or c >= self.bins[i]:
            return
            
    # Convertir coordenadas multidimensionales a índice lineal
    index = 0
    stride = 1
    for i, c in enumerate(reversed(coord)):
        index += c * stride
        stride *= self.bins[len(self.bins)-i-1]
        
    # Incrementar el bin correspondiente con el peso dado
    self.data[index] += weight