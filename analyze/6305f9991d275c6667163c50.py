def set_cut_chars(self, before: bytes, after: bytes) -> None:
    """
    Set the bytes used to delimit slice points.

    Args:
        before: Split file before these delimiters.
        after: Split file after these delimiters.
    """
    self.before_delimiter = before
    self.after_delimiter = after