def set_cut_chars(self, before: bytes, after: bytes) -> None:
    """
    Establece los bytes utilizados para delimitar los puntos de corte.

    Argumentos:
        before: Divide el archivo antes de estos delimitadores.
        after: Divide el archivo después de estos delimitadores.
    """
    self.before_cut = before
    self.after_cut = after