def set_cut_chars(self, before: bytes, after: bytes) -> None:
    """
    Imposta i byte utilizzati per delimitare i punti di taglio.

    Argomenti:
        before: Divide il file prima di questi delimitatori.
        after: Divide il file dopo questi delimitatori.
    """
    self.cut_before = before
    self.cut_after = after