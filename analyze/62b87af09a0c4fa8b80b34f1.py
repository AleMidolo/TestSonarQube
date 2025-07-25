def fill(self, coord, weight=1):
    """
    Riempie l'istogramma alla posizione *coord* con il peso specificato *weight*.
    """
    # Verifica che coord sia una tupla/lista con la dimensione corretta
    if not isinstance(coord, (tuple, list)) or len(coord) != self.dim:
        raise ValueError(f"coord deve essere una sequenza di {self.dim} valori")

    # Verifica che le coordinate siano all'interno dei limiti
    for i, x in enumerate(coord):
        if x < self.edges[i][0] or x >= self.edges[i][-1]:
            return  # Ignora valori fuori dai limiti

    # Trova gli indici dei bin per ogni dimensione
    indices = []
    for i, x in enumerate(coord):
        # Trova il bin corrispondente usando ricerca binaria
        idx = np.searchsorted(self.edges[i], x) - 1
        indices.append(idx)

    # Incrementa il contenuto del bin
    self.content[tuple(indices)] += weight