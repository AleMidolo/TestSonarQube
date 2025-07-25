def add_asset(self, basename, file_path):
    """
    将类中由 `filepath()` 调用的文件路径分配给类中 `_assets` 的 `basename`。
    "{
      "artigo02-gf03.tiff": "/path/artigo02-gf03.tiff",
      "artigo02-gf03.jpg": "/path/artigo02-gf03.jpg",
      "artigo02-gf03.png": "/path/artigo02-gf03.png",
    }
    """
    if not hasattr(self, '_assets'):
        self._assets = {}
    self._assets[basename] = file_path