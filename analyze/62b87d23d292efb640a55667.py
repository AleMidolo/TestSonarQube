def register_vcs_handler(vcs, method):  # decorador
    """Crear un decorador para marcar un método como el manejador de un VCS.
    
    Args:
        vcs: Sistema de control de versiones
        method: Método a decorar
        
    Returns:
        Función decoradora
    """
    def decorate(f):
        # Almacena el manejador VCS en el atributo _vcs_handler del método
        f._vcs_handler = (vcs, method)
        return f
    return decorate