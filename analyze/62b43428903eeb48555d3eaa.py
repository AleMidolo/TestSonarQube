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
                    
        # Convert parameters to list format
        converted_params = []
        for param_dict in params_list:
            ordered_params = [param_dict[name] for name in param_names]
            if self.out_style == "qmark":
                converted_params.append(ordered_params)
            else:
                converted_params.append(dict(enumerate(ordered_params, start=1)))
                
    else:
        # For ordinal parameters
        # Replace ? or $n with new style
        converted_sql = sql
        param_count = len(first_param)
        
        if isinstance(sql, str):
            if self.out_style == "qmark":
                converted_sql = converted_sql.replace("$", "?")
            else:
                for i in range(param_count, 0, -1):
                    converted_sql = converted_sql.replace("?", f"${i}")
        else:
            # For bytes
            if self.out_style == "qmark":
                converted_sql = converted_sql.replace(b"$", b"?")
            else:
                for i in range(param_count, 0, -1):
                    converted_sql = converted_sql.replace(b"?", str(f"${i}").encode())
                    
        # Convert parameters
        if self.out_style == "qmark":
            converted_params = list(params_list)  # Keep as list
        else:
            # Convert to dict with numbered keys
            converted_params = [
                dict(enumerate(param_seq, start=1)) 
                for param_seq in params_list
            ]
            
    return converted_sql, converted_params