def formatmany(
                self,
                sql: AnyStr,
                many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
        ) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Initialize a list to hold the converted parameters
    out_params = []
    
    # Process each set of parameters
    for params in many_params:
        if isinstance(params, dict):
            # If params is a dictionary, convert it to a list of values
            out_params.append(list(params.values()))
        elif isinstance(params, (list, tuple)):
            # If params is a list or tuple, just append it
            out_params.append(params)
        else:
            raise ValueError("Parameters must be a dictionary or a sequence.")
    
    # Replace "in-style" parameters in the SQL query with "out-style" parameters
    formatted_sql = sql
    for i, params in enumerate(out_params):
        # Create placeholders for the parameters
        placeholders = ', '.join(['%s'] * len(params))
        formatted_sql = formatted_sql.replace(f'({placeholders})', f'({", ".join(map(str, params))})', 1)
    
    return formatted_sql, out_params