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
        return self._scale
    elif isinstance(other, (int, float)):
        if self._scale == 0 or self._scale is None:
            raise LenaValueError("No se puede reajustar la escala de un gráfico con escala desconocida o igual a cero.")
        else:
            # Reajustar la última coordenada
            if hasattr(self, 'z'):
                self.z *= other / self._scale
            elif hasattr(self, 'y'):
                self.y *= other / self._scale
            elif hasattr(self, 'x'):
                self.x *= other / self._scale
            # Reajustar errores si existen
            if hasattr(self, 'z_err'):
                self.z_err *= other / self._scale
            elif hasattr(self, 'y_err'):
                self.y_err *= other / self._scale
            elif hasattr(self, 'x_err'):
                self.x_err *= other / self._scale
            self._scale = other
    else:
        raise TypeError("El valor de escala debe ser un número o None.")