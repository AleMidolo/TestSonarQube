def scale(self, other=None):
    """
    Obtiene o establece la escala del gráfico.

    Si *other* es ``None``, devuelve la escala de este gráfico.

    Si se proporciona un valor numérico en *other*, se reajusta la escala a ese valor.  
    Si el gráfico tiene una escala desconocida o igual a cero,  
    intentar reajustar la escala generará una excepción :exc:`~.LenaValueError`.

    Para obtener resultados significativos, se utilizan los campos del gráfico.  
    Solo se reajusta la última coordenada.  
    Por ejemplo, si el gráfico tiene coordenadas *x* e *y*,  
    entonces se reajustará *y*, y para un gráfico tridimensional  
    se reajustará *z*.  
    Todos los errores se reajustan junto con su coordenada.
    """
    if other is None:
        return self._scale  # Assuming _scale is an attribute that holds the current scale

    if not isinstance(other, (int, float)):
        raise ValueError("El valor de 'other' debe ser un número.")

    if self._scale is None or self._scale == 0:
        raise LenaValueError("La escala es desconocida o igual a cero.")

    # Assuming the scale is a list or similar structure where the last element is the one to adjust
    self._scale[-1] = other
    # Adjust errors accordingly if they are stored in a similar structure
    if hasattr(self, '_errors'):
        self._errors[-1] = self._calculate_error(other)  # Placeholder for error calculation logic

    return self._scale