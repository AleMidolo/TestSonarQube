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
    for dim, x in enumerate(coord):
        # Trova il bin corretto usando ricerca binaria
        edges = self.edges[dim]
        idx = 0
        for j in range(len(edges)-1):
            if edges[j] <= x < edges[j+1]:
                idx = j
                break
        indices.append(idx)

    # Incrementa il contenuto del bin
    self.content[tuple(indices)] += weight