def on(self, hook):
    """
    Función decoradora para agregar un nuevo manejador al registro.

    Argumentos:
    hook (HookType): Atributo del hook para el cual se registrará el manejador.

    Retorna:
    callable: Decorador para registrar los listeners para el hook especificado.
    """
    def decorator(func):
        if not hasattr(self, '_hooks'):
            self._hooks = {}
        if hook not in self._hooks:
            self._hooks[hook] = []
        self._hooks[hook].append(func)
        return func
    return decorator