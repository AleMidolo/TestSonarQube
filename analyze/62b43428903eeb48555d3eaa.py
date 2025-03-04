def formatmany(
    self,
    sql: AnyStr,
    many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    
    # Convert params to list for processing
    params_list = list(many_params)
    
    if not params_list:
        return sql, []
        
    # Get first param to determine type
    first_param = params_list[0]
    
    # Check if named parameters (dict) or ordinal parameters (sequence)
    is_named = isinstance(first_param, dict)
    
    # Initialize output params list
    out_params = []
    
    # Process each parameter set
    for params in params_list:
        if is_named:
            # For named parameters
            if not isinstance(params, dict):
                raise TypeError("All parameters must be dictionaries for named style")
                
            # Convert parameter names to output style
            out_param = {}
            for key, value in params.items():
                if isinstance(key, int):
                    # Convert int keys to string
                    out_param[str(key)] = value
                else:
                    out_param[key] = value
            out_params.append(out_param)
            
        else:
            # For ordinal parameters
            if not isinstance(params, (list, tuple)):
                raise TypeError("All parameters must be sequences for ordinal style")
                
            # Convert to list and append
            out_params.append(list(params))
            
    # Convert parameter style in SQL if needed
    if isinstance(sql, str):
        # Handle string SQL
        if is_named:
            # Convert named parameters from :name to %(name)s style
            sql = self._convert_named_params(sql)
        else:
            # Convert ordinal parameters from ? to %s style 
            sql = sql.replace('?', '%s')
    else:
        # Handle bytes SQL
        if is_named:
            sql = self._convert_named_params(sql.decode()).encode()
        else:
            sql = sql.replace(b'?', b'%s')
            
    return sql, out_params

def _convert_named_params(self, sql: str) -> str:
    """Helper method to convert :name style parameters to %(name)s style"""
    import re
    return re.sub(r':([a-zA-Z_][a-zA-Z0-9_]*)', r'%(\1)s', sql)