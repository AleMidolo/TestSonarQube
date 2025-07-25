def parse(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    """
    Convierte la cadena de fecha/hora en un objeto de la clase :class:`datetime.datetime`.
    
    Args:
        timestr: Cualquier fecha/hora en formato string que utilice los formatos compatibles.
        default: El objeto datetime predeterminado. Si este es un objeto datetime y no es None, 
                los elementos especificados en timestr reemplazan los elementos en el objeto predeterminado.
        ignoretz: Si True, ignora zonas horarias y devuelve datetime sin info de zona horaria.
        tzinfos: Diccionario o función para mapear nombres de zonas horarias a objetos tzinfo.
        **kwargs: Argumentos adicionales pasados a _parse().
        
    Returns:
        datetime.datetime o tupla (datetime, tokens) si fuzzy_with_tokens=True
        
    Raises:
        ParserError: Para formatos inválidos o desconocidos
        TypeError: Para entradas que no sean strings
        OverflowError: Si la fecha excede el máximo entero C
    """
    
    if not isinstance(timestr, str):
        raise TypeError("Parser must be called with string argument")
        
    # Preprocesar la cadena de entrada
    timestr = timestr.strip()
    
    # Usar el parser interno
    res, tokens = self._parse(timestr, **kwargs)
    
    if res is None:
        raise ParserError("Unknown string format")
        
    # Aplicar el default si existe
    if default is not None:
        for attr in ["year", "month", "day", "hour", "minute", 
                    "second", "microsecond"]:
            value = getattr(res, attr)
            if value is None:
                setattr(res, attr, getattr(default, attr))
                
    # Manejar zona horaria
    if not ignoretz:
        if res.tzinfo is None and tzinfos is not None:
            # Intentar obtener tzinfo del diccionario/función tzinfos
            if isinstance(tzinfos, dict):
                if res.tzname in tzinfos:
                    tzinfo = tzinfos[res.tzname]
                    if isinstance(tzinfo, int):
                        from datetime import timedelta
                        tzinfo = self.tzoffset(res.tzname, timedelta(seconds=tzinfo))
                    res = res.replace(tzinfo=tzinfo)
            else:
                # tzinfos es una función
                try:
                    res = res.replace(tzinfo=tzinfos(res.tzname, res.tzoffset))
                except:
                    pass
    else:
        res = res.replace(tzinfo=None)
        
    # Devolver resultado
    if kwargs.get('fuzzy_with_tokens', False):
        return res, tokens
    else:
        return res