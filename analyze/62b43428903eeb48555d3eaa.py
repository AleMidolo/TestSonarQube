def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    formatted_sql = sql
    formatted_params = []

    for params in many_params:
        if isinstance(params, dict):
            # Named parameters
            formatted_params.append({k: v for k, v in params.items()})
        else:
            # Ordinal parameters
            formatted_params.append([v for v in params])

    return formatted_sql, formatted_params