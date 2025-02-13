def add_rendition(self, lang, file_path):
    """ {
        "originale": "artigo02.pdf",
        "en": "artigo02-en.pdf",
    }
    """
    if not hasattr(self, 'renditions'):
        self.renditions = {}
    self.renditions[lang] = file_path