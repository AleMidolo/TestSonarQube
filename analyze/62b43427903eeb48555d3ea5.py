def format(
    self,
    sql: AnyStr,
    params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    
    # Handle empty params case
    if not params:
        return sql, params
        
    # Convert named parameters style
    if isinstance(params, dict):
        formatted_sql = sql
        formatted_params = {}
        param_count = 0
        
        # Replace named parameters with positional parameters
        for param_name, param_value in params.items():
            param_placeholder = f'%({param_name})s' if isinstance(sql, str) else b'%(' + str(param_name).encode() + b')s'
            out_placeholder = '%s' if isinstance(sql, str) else b'%s'
            formatted_sql = formatted_sql.replace(param_placeholder, out_placeholder)
            formatted_params[param_count] = param_value
            param_count += 1
            
        return formatted_sql, formatted_params
        
    # Convert positional parameters style 
    else:
        formatted_sql = sql
        formatted_params = list(params)
        
        # Replace %s with ? for positional parameters if needed
        if isinstance(sql, str):
            formatted_sql = formatted_sql.replace('%s', '?')
        else:
            formatted_sql = formatted_sql.replace(b'%s', b'?')
            
        return formatted_sql, formatted_params