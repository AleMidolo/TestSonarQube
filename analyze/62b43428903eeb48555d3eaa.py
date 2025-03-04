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
        # Replace :param or %(param)s with ? or $n based on out_style
        param_names = first_param.keys()
        converted_sql = sql
        
        for name in param_names:
            if isinstance(sql, str):
                pattern = f":{name}|%\({name}\)s"
                if self.out_style == '?':
                    converted_sql = re.sub(pattern, '?', converted_sql)
                else:
                    # For $n style
                    param_num = list(param_names).index(name) + 1
                    converted_sql = re.sub(pattern, f'${param_num}', converted_sql)
                    
        # Convert parameters to list format if needed
        if self.out_style == '?':
            converted_params = [list(p.values()) for p in params_list]
        else:
            converted_params = params_list
            
    else:
        # For ordinal parameters
        # Replace ? with $n if needed
        if self.out_style == '?':
            converted_sql = sql
            converted_params = params_list
        else:
            # Convert ? to $1, $2 etc
            param_count = len(first_param)
            converted_sql = sql
            if isinstance(sql, str):
                for i in range(param_count):
                    converted_sql = converted_sql.replace('?', f'${i+1}', 1)
            converted_params = params_list
            
    return converted_sql, converted_params