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
                converted_sql = converted_sql.replace(f':{name}', self.out_placeholder)
        elif self.in_style == 'pyformat':
            for name in param_names:
                converted_sql = converted_sql.replace(f'%({name})s', self.out_placeholder)
                
        # Convert parameters to list format
        converted_params = []
        for params in params_list:
            if self.out_style == 'qmark':
                # Convert to list maintaining order of param_names
                converted_params.append([params[name] for name in param_names])
            else:
                # Keep as dict for named out styles
                converted_params.append(params)
                
    else:
        # For ordinal parameters
        # Replace ? or %s with ? or $n based on out_style
        converted_sql = sql
        
        if self.in_style == 'qmark':
            placeholder = '?'
        elif self.in_style == 'format':
            placeholder = '%s'
            
        count = len(first_param)
        if self.out_style == 'numeric':
            # Replace with $1, $2 etc
            for i in range(count):
                converted_sql = converted_sql.replace(placeholder, f'${i+1}', 1)
        else:
            # Replace with out placeholder if different from in placeholder
            if placeholder != self.out_placeholder:
                for _ in range(count):
                    converted_sql = converted_sql.replace(placeholder, self.out_placeholder, 1)
                    
        converted_params = params_list

    return converted_sql, converted_params