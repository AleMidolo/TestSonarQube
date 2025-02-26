def set_cut_chars(self, before: bytes, after: bytes) -> None:
    """
    Set the bytes used to delimit slice points.

    Args:
        before: Split file before these delimiters.
        after: Split file after these delimiters.
    """
    self.before_cut_chars = before
    self.after_cut_chars = after