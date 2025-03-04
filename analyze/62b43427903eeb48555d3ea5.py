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
        new_params = {}
        counter = 1
        
        # Replace named parameters with positional parameters
        for key, value in params.items():
            placeholder = f'${counter}'
            if isinstance(sql, str):
                sql = sql.replace(f':{key}', placeholder)
                sql = sql.replace(f'%({key})s', placeholder)
            else:  # bytes
                sql = sql.replace(f':{key}'.encode(), placeholder.encode())
                sql = sql.replace(f'%({key})s'.encode(), placeholder.encode())
            new_params[counter] = value
            counter += 1
            
        return sql, new_params
        
    # Convert positional parameters style 
    else:
        new_params = {}
        for i, value in enumerate(params, 1):
            if isinstance(sql, str):
                sql = sql.replace('?', f'${i}', 1)
                sql = sql.replace('%s', f'${i}', 1)
            else:  # bytes
                sql = sql.replace(b'?', f'${i}'.encode(), 1)
                sql = sql.replace(b'%s', f'${i}'.encode(), 1)
            new_params[i] = value
            
        return sql, new_params