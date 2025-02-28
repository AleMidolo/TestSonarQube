def add_rendition(self, lang, file_path):
    """
    将类中由 `filepath()` 调用的文件路径分配给类中 `_renditions` 的 "lang"。

    {
        "original": "artigo02.pdf",
        "en": "artigo02-en.pdf",
    }
    """
    if not hasattr(self, '_renditions'):
        self._renditions = {}
    self._renditions[lang] = file_path