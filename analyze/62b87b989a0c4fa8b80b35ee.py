def reset(self):
    """
    Restablece el histograma.

    El contexto actual se restablece a un diccionario vacío.
    Los contenedores (bins) se reinicializan con el *initial_value*
    o con *make_bins()* (dependiendo de la inicialización).
    """
    self.context = {}
    if hasattr(self, 'initial_value'):
        self.bins = {key: self.initial_value for key in self.bins.keys()}
    else:
        self.bins = self.make_bins()