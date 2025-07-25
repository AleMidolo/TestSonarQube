def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    
    # Convert each params set to out style
    out_params = []
    for params in many_params:
        # Format SQL and convert params for first iteration only
        if not out_params:
            sql, _ = self.format(sql, params)
            
        # Convert params to out style without reformatting SQL
        converted_params = self._convert_params(params)
        out_params.append(converted_params)
            
    return sql, out_params