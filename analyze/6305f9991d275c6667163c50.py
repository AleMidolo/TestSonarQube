def set_cut_chars(self, before: bytes, after: bytes) -> None:
    """
    Imposta i byte utilizzati per delimitare i punti di taglio.

    Argomenti:
        before: Divide il file prima di questi delimitatori.
        after: Divide il file dopo questi delimitatori.
    """
    self.before_cut = before
    self.after_cut = after