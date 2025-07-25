def fill(self, coord, weight=1):
    """
    Riempie l'istogramma alla posizione *coord* con il peso specificato *weight*.
    """
    # Verifica che coord sia una tupla/lista di coordinate valide
    if not isinstance(coord, (tuple, list)):
        raise TypeError("Le coordinate devono essere specificate come tupla o lista")
        
    # Verifica che la dimensione delle coordinate corrisponda alla dimensionalità dell'istogramma
    if len(coord) != len(self.bins):
        raise ValueError(f"Numero di coordinate ({len(coord)}) non corrisponde alla dimensionalità dell'istogramma ({len(self.bins)})")
    
    # Verifica che le coordinate siano all'interno dei limiti dell'istogramma
    for i, x in enumerate(coord):
        if x < self.bins[i][0] or x >= self.bins[i][-1]:
            raise ValueError(f"Coordinata {x} fuori dai limiti dell'asse {i}")
    
    # Trova gli indici dei bin corrispondenti alle coordinate
    indices = []
    for i, x in enumerate(coord):
        # Trova l'indice del bin usando ricerca binaria
        idx = next(j for j in range(len(self.bins[i])-1) if self.bins[i][j] <= x < self.bins[i][j+1])
        indices.append(idx)
    
    # Incrementa il contenuto del bin con il peso specificato
    self.contents[tuple(indices)] += weight