def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Convert each params in many_params using the converter
    converted_params = [self._converter.convert_many(params) for params in many_params]
    
    # If no params provided, return original sql and empty list
    if not converted_params:
        return sql, []
        
    # Get the first converted params to determine type
    first_params = converted_params[0]
    
    # For named parameters (dict)
    if isinstance(first_params, dict):
        # Verify all params are dicts
        if not all(isinstance(p, dict) for p in converted_params):
            raise TypeError("All parameters must be of same type (dict)")
        return sql, converted_params
        
    # For positional parameters (sequence)
    elif isinstance(first_params, (list, tuple)):
        # Verify all params are sequences
        if not all(isinstance(p, (list, tuple)) for p in converted_params):
            raise TypeError("All parameters must be of same type (sequence)")
        return sql, converted_params
        
    else:
        raise TypeError("Parameters must be either dict or sequence type")