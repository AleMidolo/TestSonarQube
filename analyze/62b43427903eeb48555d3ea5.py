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
            param_placeholder = f'%({param_name})s'
            if isinstance(sql, bytes):
                param_placeholder = param_placeholder.encode()
            
            if param_placeholder in formatted_sql:
                param_count += 1
                new_placeholder = '%s' if isinstance(sql, str) else b'%s'
                formatted_sql = formatted_sql.replace(param_placeholder, new_placeholder)
                formatted_params[param_count] = param_value
                
        return formatted_sql, formatted_params
        
    # Convert positional parameters style 
    else:
        formatted_sql = sql
        formatted_params = list(params)
        
        # Replace %s with numbered parameters
        param_count = len(params)
        for i in range(param_count):
            old_placeholder = '%s' if isinstance(sql, str) else b'%s'
            new_placeholder = f'${i+1}' if isinstance(sql, str) else f'${i+1}'.encode()
            formatted_sql = formatted_sql.replace(old_placeholder, new_placeholder, 1)
            
        return formatted_sql, formatted_params