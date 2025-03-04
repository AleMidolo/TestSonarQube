def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    
    # Convert each params set to out style
    out_params_list = []
    for params in many_params:
        # Format single params set
        _, out_params = self.format(sql, params)
        out_params_list.append(out_params)
        
    # Format SQL once using first params set
    try:
        first_params = next(iter(many_params))
    except StopIteration:
        first_params = {}
        
    out_sql, _ = self.format(sql, first_params)
    
    return out_sql, out_params_list