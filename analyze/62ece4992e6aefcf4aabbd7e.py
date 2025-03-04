def _resolve_string(matcher):
    # Extraer nombre y valor predeterminado del matcher
    parts = matcher.group(1).split(':')
    var_name = parts[0]
    default = parts[1] if len(parts) > 1 else None
    
    # Obtener valor del entorno
    value = os.environ.get(var_name)
    
    # Si no hay valor y no hay default, error
    if value is None and default is None:
        raise ValueError(f"Environment variable '{var_name}' is not defined and no default value was provided")
        
    # Retornar valor del entorno o default
    return value if value is not None else default