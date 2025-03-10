def reset(self):
    """
    Reimposta l'istogramma.

    Il contesto attuale viene reimpostato a un dizionario vuoto.
    I bin vengono reinizializzati con il *valore_iniziale*
    o con *make_bins()* (a seconda dell'inizializzazione).
    """
    self.context = {}
    if hasattr(self, 'valore_iniziale'):
        self.bins = [self.valore_iniziale] * len(self.bins)
    else:
        self.bins = self.make_bins()