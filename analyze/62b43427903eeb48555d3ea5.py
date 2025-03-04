def format(
    self,
    sql: AnyStr,
    params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Convert the SQL query to use the out-style parameters instead of
    the in-style parameters.

    *sql* (:class:`str` or :class:`bytes`) is the SQL query.

    *params* (:class:`~collections.abc.Mapping` or :class:`~collections.abc.Sequence`)
    contains the set of in-style parameters. It maps each parameter
    (:class:`str` or :class:`int`) to value. If :attr:`.SQLParams.in_style`
    is a named parameter style. then *params* must be a :class:`~collections.abc.Mapping`.
    If :attr:`.SQLParams.in_style` is an ordinal parameter style, then
    *params* must be a :class:`~collections.abc.Sequence`.

    Returns a :class:`tuple` containing:

    -       The formatted SQL query (:class:`str` or :class:`bytes`).

    -       The set of converted out-style parameters (:class:`dict` or
            :class:`list`).
    """
    # Handle bytes vs string
    is_bytes = isinstance(sql, bytes)
    if is_bytes:
        sql = sql.decode('utf-8')
        
    # Convert params to dict if sequence
    if isinstance(params, Sequence):
        params_dict = {str(i): val for i, val in enumerate(params)}
    else:
        params_dict = params

    # Initialize output params
    out_params = {} if self.out_style.is_named else []
    param_counter = 0
    
    # Process the SQL string
    result = ''
    i = 0
    while i < len(sql):
        # Look for parameter markers
        if sql[i:i+len(self.in_style.prefix)] == self.in_style.prefix:
            param_name = ''
            i += len(self.in_style.prefix)
            
            # Extract parameter name/number
            while i < len(sql) and (sql[i].isalnum() or sql[i] == '_'):
                param_name += sql[i]
                i += 1
                
            if param_name:
                # Get parameter value
                param_value = params_dict[param_name]
                
                # Add to output parameters
                if self.out_style.is_named:
                    out_param_name = f"p{param_counter}"
                    out_params[out_param_name] = param_value
                    result += self.out_style.prefix + out_param_name
                else:
                    out_params.append(param_value)
                    result += self.out_style.prefix
                    
                param_counter += 1
        else:
            result += sql[i]
            i += 1
            
    # Convert back to bytes if input was bytes
    if is_bytes:
        result = result.encode('utf-8')
        
    return result, out_params