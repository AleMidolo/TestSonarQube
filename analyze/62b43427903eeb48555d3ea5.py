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
        for param_name, value in params.items():
            # Reemplazar parámetro de estilo "in" por estilo "out"
            if isinstance(param_name, str):
                old_param = f":{param_name}"
                new_param = "?" if self.out_style == "qmark" else "%s"
                out_sql = out_sql.replace(old_param, new_param)
                
                # Agregar parámetro al conjunto de salida
                if self.out_style == "qmark":
                    out_params.append(value)
                else:
                    out_params[param_name] = value
                    
    # Procesar parámetros ordinales            
    else:
        for value in params:
            # Reemplazar parámetro de estilo "in" por estilo "out"
            old_param = "?"
            new_param = "?" if self.out_style == "qmark" else "%s"
            out_sql = out_sql.replace(old_param, new_param, 1)
            
            # Agregar parámetro al conjunto de salida
            if self.out_style == "qmark":
                out_params.append(value)
            else:
                out_params[param_index] = value
                param_index += 1
                
    # Convertir sql de vuelta a bytes si era bytes originalmente
    if is_bytes:
        out_sql = out_sql.encode()
        
    return out_sql, out_params