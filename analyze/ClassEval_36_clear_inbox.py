def clear_inbox(self, size):
    """
    Limpia la bandeja de entrada eliminando los correos electrónicos más antiguos hasta que la bandeja de entrada tenga suficiente espacio para acomodar el tamaño dado.
    :param size: El tamaño del correo electrónico, float.
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
    >>> receiver.clear_inbox(30)
    >>> receiver.inbox
    [{'size': 15}]

    """
    # Calcular el espacio actual ocupado en la bandeja de entrada
    current_size = sum(email['size'] for email in self.inbox)
    
    # Calcular el espacio disponible
    available_space = self.capacity - current_size
    
    # Si ya hay suficiente espacio, no hacer nada
    if available_space >= size:
        return
    
    # Calcular cuánto espacio necesitamos liberar
    space_needed = size - available_space
    
    # Eliminar correos desde el principio (los más antiguos) hasta liberar suficiente espacio
    freed_space = 0
    index = 0
    
    while freed_space < space_needed and index < len(self.inbox):
        freed_space += self.inbox[index]['size']
        index += 1
    
    # Eliminar los correos más antiguos
    self.inbox = self.inbox[index:]