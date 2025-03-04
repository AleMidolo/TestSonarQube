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
                
            # Convert parameter style if needed
            if hasattr(self, 'in_style') and hasattr(self, 'out_style'):
                converted_params = {}
                for key, value in params.items():
                    # Convert parameter name from in_style to out_style
                    new_key = key
                    if isinstance(key, str):
                        if self.in_style == '%s':
                            new_key = f"%({key})s"
                        elif self.in_style == ':':
                            new_key = f":{key}"
                        elif self.in_style == '$':
                            new_key = f"${key}"
                    converted_params[new_key] = value
                out_params.append(converted_params)
            else:
                out_params.append(params)
                
        else:
            # For ordinal parameters
            if not isinstance(params, (list, tuple)):
                raise TypeError("All parameters must be sequences for ordinal style")
                
            # Convert to list to ensure mutability
            out_params.append(list(params))
            
    # Convert SQL if needed
    if hasattr(self, 'in_style') and hasattr(self, 'out_style'):
        if isinstance(sql, str):
            # Replace parameter style markers
            if self.in_style == '%s' and self.out_style == ':':
                sql = sql.replace('%s', ':%s')
            elif self.in_style == ':' and self.out_style == '%s':
                sql = sql.replace(':', '%')
            elif self.in_style == '$' and self.out_style == '%s':
                # Replace $1, $2, etc with %s
                import re
                sql = re.sub(r'\$\d+', '%s', sql)
                
    return sql, out_params