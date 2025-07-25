def validate_choices_args(self, args):  
    """
    Verifica si el valor de los argumentos de elección es una de las opciones disponibles.  

    :param args: Los argumentos recibidos.  
    """
    available_choices = self.get_available_choices()  # Método que devuelve las opciones disponibles
    for arg in args:
        if arg not in available_choices:
            raise ValueError(f"El argumento '{arg}' no es una opción válida.")