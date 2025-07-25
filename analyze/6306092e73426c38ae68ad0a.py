def validate_choices_args(self, args):
    """
    Verifica si el valor de los argumentos de elección es una de las opciones disponibles.

    :param args: Los argumentos recibidos.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("No se han definido opciones de elección en la clase.")

    for key, value in args.items():
        if key in self.choices:
            if value not in self.choices[key]:
                raise ValueError(f"El valor '{value}' para el argumento '{key}' no es una opción válida. Opciones válidas: {self.choices[key]}")