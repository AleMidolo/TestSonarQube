def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]:
    formatted_sql = sql
    formatted_params = []

    for params in many_params:
        if isinstance(params, dict):
            # Handle named parameters
            formatted_params.append({k: v for k, v in params.items()})
        elif isinstance(params, (list, tuple)):
            # Handle ordinal parameters
            formatted_params.append([v for v in params])
        else:
            raise TypeError("Unsupported parameter type. Expected dict, list, or tuple.")

    return formatted_sql, formatted_params