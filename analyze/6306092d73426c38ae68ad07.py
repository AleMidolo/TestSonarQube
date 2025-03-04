def validar_argumentos_requeridos(self, args):
    """
    Verifica si se han proporcionado todos los argumentos requeridos.
    """
    argumentos_requeridos = [arg for arg in self.argumentos if arg.requerido]
    
    for arg_requerido in argumentos_requeridos:
        if arg_requerido.nombre not in args:
            raise ValueError(f"Falta el argumento requerido: {arg_requerido.nombre}")
        
        if args[arg_requerido.nombre] is None:
            raise ValueError(f"El argumento {arg_requerido.nombre} no puede ser None")
            
    return True