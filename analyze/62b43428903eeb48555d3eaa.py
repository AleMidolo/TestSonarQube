def formatmany(
                self,
                sql: AnyStr,
                many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
        ) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Determine the parameter style
    if isinstance(many_params, dict):
        param_style = 'named'
    else:
        param_style = 'ordinal'

    # Prepare the formatted SQL and converted parameters
    formatted_sql = sql
    converted_params = []

    for params in many_params:
        if param_style == 'named':
            # Convert named parameters to out style
            converted_param = {key: value for key, value in params.items()}
            formatted_sql = formatted_sql.replace(':{}'.format(key), '{}'.format(value))
        else:
            # Convert ordinal parameters to out style
            converted_param = list(params)
            formatted_sql = formatted_sql.replace('?', '{}')

        converted_params.append(converted_param)

    return formatted_sql, converted_params