def format(
        self,
        sql: AnyStr,
        params: Union[Dict[Union[str, int], Any], Sequence[Any]],
) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    converted_sql = self._converter.convert(sql)
    if isinstance(params, dict):
        converted_params = {key: self._converter.convert(value) for key, value in params.items()}
    else:
        converted_params = [self._converter.convert(value) for value in params]
    return converted_sql, converted_params