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
    
    # Convert SQL and params based on parameter style
    if is_named:
        # For named parameters
        # Replace :name or %(name)s with ? or $n based on out_style
        param_names = list(first_param.keys())
        converted_sql = sql
        
        if self.in_style in [':named', 'named']:
            for name in param_names:
                converted_sql = converted_sql.replace(f':{name}', 
                    self.out_style_placeholder(param_names.index(name)))
        elif self.in_style == 'pyformat':
            for name in param_names:
                converted_sql = converted_sql.replace(f'%({name})s',
                    self.out_style_placeholder(param_names.index(name)))
                    
        # Convert parameters to list in correct order
        converted_params = []
        for params in params_list:
            param_values = [params[name] for name in param_names]
            if self.out_style == 'named':
                # Convert back to dict for named out style
                converted_params.append(dict(zip(param_names, param_values)))
            else:
                converted_params.append(param_values)
                
    else:
        # For ordinal parameters
        # Replace %s with ? or $n based on out_style
        param_count = len(first_param)
        converted_sql = sql
        
        if self.in_style == 'format':
            for i in range(param_count):
                converted_sql = converted_sql.replace('%s',
                    self.out_style_placeholder(i), 1)
                    
        # Parameters remain as sequences
        converted_params = params_list
        if self.out_style == 'named':
            # Convert sequences to dicts for named out style
            converted_params = [
                dict(enumerate(params)) for params in params_list
            ]
            
    return converted_sql, converted_params