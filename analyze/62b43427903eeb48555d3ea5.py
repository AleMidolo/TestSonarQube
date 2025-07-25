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
    formatted_sql = sql
    out_params = {} if isinstance(params, dict) else []
    param_index = 0
    
    # Procesar parámetros nombrados
    if isinstance(params, dict):
        for param_name, value in params.items():
            # Reemplazar parámetro de estilo "in" por estilo "out"
            old_param = f":{param_name}" if self.in_style == "named" else f"${param_name}"
            new_param = f"?" if self.out_style == "qmark" else f"%s"
            formatted_sql = formatted_sql.replace(old_param, new_param)
            
            # Agregar parámetro al conjunto de salida
            if self.out_style == "named":
                out_params[f"p{param_index}"] = value
            else:
                out_params[param_index] = value
            param_index += 1
            
    # Procesar parámetros ordinales        
    else:
        for i, value in enumerate(params):
            # Reemplazar parámetro de estilo "in" por estilo "out"
            old_param = f"${i+1}" if self.in_style == "numeric" else "?"
            new_param = f"?" if self.out_style == "qmark" else f"%s"
            formatted_sql = formatted_sql.replace(old_param, new_param)
            
            # Agregar parámetro al conjunto de salida
            if self.out_style == "named":
                out_params[f"p{i}"] = value
            else:
                out_params.append(value)
                
    # Convertir sql de vuelta a bytes si era bytes originalmente
    if is_bytes:
        formatted_sql = formatted_sql.encode()
        
    return formatted_sql, out_params