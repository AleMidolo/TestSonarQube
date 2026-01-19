def get_mode(self):
    """
    Obtener el modo de trabajo actual
    :return mode: str, modo de trabajo. solo ['heat', 'cool']
    """
    return self.mode if hasattr(self, 'mode') and self.mode in ['heat', 'cool'] else 'cool'