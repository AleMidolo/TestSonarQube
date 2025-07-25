def formatmany(
    self,
    sql: AnyStr,
    many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    
    # Convert each params set to out style
    out_params = []
    for params in many_params:
        # Format single params set
        _, converted_params = self.format(sql, params)
        out_params.append(converted_params)
        
    # Format SQL once using first params set
    try:
        first_params = next(iter(many_params))
    except StopIteration:
        # No params, just format SQL
        formatted_sql, _ = self.format(sql, {})
    else:
        # Format with first params set
        formatted_sql, _ = self.format(sql, first_params)
        
    return formatted_sql, out_params