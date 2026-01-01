def send(self, info):
    """
        Enviar información que contiene dirección y contenido
        :param info: dict, diccionario de información que contiene dirección y contenido
        :return: si se envió con éxito, no devuelve nada; de lo contrario, devuelve una cadena que indica un mensaje de error
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
    if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
        return "Error: Invalid info format. Must be a dict with 'addr' and 'content' keys."
    self.send_struct = {'addr': info['addr'], 'content': info['content']}