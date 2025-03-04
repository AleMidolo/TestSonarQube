def fill(self, coord, weight=1):
    """
    Riempie l'istogramma alla posizione *coord* con il peso specificato *weight*.
    """
    # Verifica che coord sia una tupla di coordinate valide
    if not isinstance(coord, tuple):
        raise TypeError("Le coordinate devono essere specificate come tupla")
        
    # Verifica che le dimensioni delle coordinate corrispondano a quelle dell'istogramma
    if len(coord) != len(self.bins):
        raise ValueError("Il numero di coordinate non corrisponde alle dimensioni dell'istogramma")
    
    # Verifica che le coordinate siano all'interno dei limiti
    for i, x in enumerate(coord):
        if x < 0 or x >= len(self.bins[i]):
            raise ValueError(f"Coordinata {i} fuori dai limiti dell'istogramma")
            
    # Converte le coordinate in un indice lineare per accedere all'array dei contenuti
    idx = 0
    stride = 1
    for i in range(len(coord)-1, -1, -1):
        idx += coord[i] * stride
        stride *= len(self.bins[i])
        
    # Aggiunge il peso alla bin corrispondente
    self.contents[idx] += weight