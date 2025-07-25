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
        
        for i, name in enumerate(param_names, start=1):
            if isinstance(sql, str):
                converted_sql = converted_sql.replace(f":{name}", 
                    "?" if self.out_style == "qmark" else f"${i}")
                converted_sql = converted_sql.replace(f"%({name})s",
                    "?" if self.out_style == "qmark" else f"${i}")
            else:
                # For bytes
                name_bytes = str(name).encode()
                converted_sql = converted_sql.replace(b":" + name_bytes,
                    b"?" if self.out_style == "qmark" else str(f"${i}").encode())
                converted_sql = converted_sql.replace(b"%" + name_bytes + b")s",
                    b"?" if self.out_style == "qmark" else str(f"${i}").encode())
                    
        # Convert parameters to list in correct order
        converted_params = []
        for param_dict in params_list:
            ordered_params = [param_dict[name] for name in param_names]
            if self.out_style == "numeric":
                # For numeric style, convert to dict with position numbers
                ordered_params = {i+1: val for i, val in enumerate(ordered_params)}
            converted_params.append(ordered_params)
            
    else:
        # For ordinal parameters
        # Replace ? or :1,:2 with ? or $1,$2 based on out_style 
        converted_sql = sql
        param_count = len(first_param)
        
        if isinstance(sql, str):
            for i in range(param_count):
                converted_sql = converted_sql.replace(f":{i+1}",
                    "?" if self.out_style == "qmark" else f"${i+1}")
        else:
            # For bytes
            for i in range(param_count):
                pos = str(i+1).encode()
                converted_sql = converted_sql.replace(b":" + pos,
                    b"?" if self.out_style == "qmark" else str(f"${i+1}").encode())
                    
        # Convert parameters based on out_style
        if self.out_style == "numeric":
            # Convert sequences to dicts with position numbers
            converted_params = [{i+1: val for i, val in enumerate(param_seq)} 
                              for param_seq in params_list]
        else:
            # Keep as sequences for qmark style
            converted_params = list(params_list)
            
    return converted_sql, converted_params