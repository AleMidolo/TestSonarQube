def set_cut_chars(self, before: bytes, after: bytes) -> None:
    """
    设置用于分隔切片点的字节。

    参数:
      before: 在这些分隔符之前分割文件。
      after: 在这些分隔符之后分割文件。
    """
    self.before_cut = before
    self.after_cut = after