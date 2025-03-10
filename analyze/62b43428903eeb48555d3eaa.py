def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    formatted_sql = sql
    formatted_params = []
    
    for params in many_params:
        if isinstance(params, dict):
            # Handle named parameters
            formatted_params.append(params)
        elif isinstance(params, (list, tuple)):
            # Handle ordinal parameters
            formatted_params.append(list(params))
        else:
            raise TypeError("Parameters must be either a dictionary or a sequence.")
    
    return formatted_sql, formatted_params