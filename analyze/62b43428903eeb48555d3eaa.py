def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    
    # Convert each params in many_params using the converter
    converted_params = []
    for params in many_params:
        converted = self._converter.convert_many(sql, params)
        converted_params.append(converted[1])
        
        # Use the SQL from first conversion since it will be the same for all
        if len(converted_params) == 1:
            converted_sql = converted[0]
            
    return converted_sql, converted_params