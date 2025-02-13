def formatmany(
                self,
                sql: AnyStr,
                many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
        ) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    out_params = []
    for params in many_params:
        converted_params = self._converter.convert_many(params)
        out_params.append(converted_params)
    
    formatted_sql = self._converter.convert_sql(sql)
    
    return formatted_sql, out_params