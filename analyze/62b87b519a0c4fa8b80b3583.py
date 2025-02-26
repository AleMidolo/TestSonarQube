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
        return self.scale_value  # Assuming scale_value is an attribute of the class

    if not isinstance(other, (int, float)):
        raise ValueError("El valor de 'other' debe ser un número.")

    if self.scale_value is None or self.scale_value == 0:
        raise LenaValueError("La escala es desconocida o igual a cero.")

    # Assuming we have a method to adjust the scale
    self.adjust_scale(other)