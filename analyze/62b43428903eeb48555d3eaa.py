def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Convert each params in many_params using the converter
    converted_params = [self._converter.convert_many(sql, params) for params in many_params]
    
    # If no params, return original sql and empty list
    if not converted_params:
        return sql, []
        
    # Get the first converted sql and params
    converted_sql = converted_params[0][0]
    
    # Extract just the params from each conversion
    params_list = [conv[1] for conv in converted_params]
    
    return converted_sql, params_list