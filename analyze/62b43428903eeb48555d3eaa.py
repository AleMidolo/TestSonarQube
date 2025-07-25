def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    formatted_sql = sql
    formatted_params = []

    for params in many_params:
        if isinstance(params, dict):
            # Convert dict to list of values in the order of the keys
            formatted_params.append(list(params.values()))
        elif isinstance(params, (list, tuple)):
            # If it's already a sequence, just append it
            formatted_params.append(params)
        else:
            raise TypeError("params must be a Mapping or Sequence")

    return formatted_sql, formatted_params