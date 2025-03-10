def on(self, hook):
    """
    Funzione decorator per aggiungere un nuovo gestore al registro.

    Argomenti:
    - `hook` (HookType): Attributo del hook per il quale registrare il gestore.

    Restituisce:
    - `callable`: Decorator per registrare i listener per il hook specificato.
    """
    def decorator(func):
        if not hasattr(self, '_handlers'):
            self._handlers = {}
        if hook not in self._handlers:
            self._handlers[hook] = []
        self._handlers[hook].append(func)
        return func
    return decorator