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
        new_sql = sql
        
        # Replace each named parameter with positional parameter
        for key, value in params.items():
            param_name = f'${counter}'
            if isinstance(sql, str):
                new_sql = new_sql.replace(f':{key}', param_name)
                new_sql = new_sql.replace(f'%({key})s', param_name)
            else: # bytes
                new_sql = new_sql.replace(f':{key}'.encode(), param_name.encode())
                new_sql = new_sql.replace(f'%({key})s'.encode(), param_name.encode())
            new_params[counter] = value
            counter += 1
            
        return new_sql, new_params
        
    # Convert positional parameters style 
    else:
        new_params = {}
        new_sql = sql
        
        # Replace each ? or %s with $n style parameter
        for i, value in enumerate(params, 1):
            param_name = f'${i}'
            if isinstance(sql, str):
                new_sql = new_sql.replace('?', param_name, 1)
                new_sql = new_sql.replace('%s', param_name, 1)
            else: # bytes
                new_sql = new_sql.replace(b'?', param_name.encode(), 1)
                new_sql = new_sql.replace(b'%s', param_name.encode(), 1)
            new_params[i] = value
            
        return new_sql, new_params