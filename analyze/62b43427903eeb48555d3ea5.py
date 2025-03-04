def format(
    self,
    sql: AnyStr,
    params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    
    # Si sql es bytes, convertir a str para procesar
    is_bytes = isinstance(sql, bytes)
    if is_bytes:
        sql = sql.decode()
        
    # Inicializar variables
    out_sql = sql
    out_params = {} if isinstance(params, dict) else []
    param_index = 0
    
    # Procesar parámetros nombrados
    if isinstance(params, dict):
        for param_name, param_value in params.items():
            # Reemplazar parámetro de estilo "in" por estilo "out"
            if isinstance(param_name, str):
                old_param = f":{param_name}"
                new_param = f"${param_index + 1}"
                out_sql = out_sql.replace(old_param, new_param)
                out_params[param_index] = param_value
                param_index += 1
                
    # Procesar parámetros ordinales 
    else:
        for i, param_value in enumerate(params):
            # Reemplazar parámetro de estilo "in" por estilo "out"
            old_param = "?"
            new_param = f"${i + 1}"
            out_sql = out_sql.replace(old_param, new_param, 1)
            out_params.append(param_value)
            
    # Convertir out_params a dict si era dict originalmente
    if isinstance(params, dict):
        out_params = dict(enumerate(out_params.values()))
            
    # Convertir sql de vuelta a bytes si era bytes originalmente
    if is_bytes:
        out_sql = out_sql.encode()
        
    return out_sql, out_params