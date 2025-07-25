def formatmany(
    self,
    sql: AnyStr,
    many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Convert each params set to out-style
    out_params = []
    for params in many_params:
        # Format SQL and convert params for first iteration only
        if not out_params:
            sql, _ = self.format(sql, params)
        # Convert params to out-style
        if isinstance(params, Mapping):
            # Named parameters
            out_param_dict = {}
            for key, value in params.items():
                out_key = self._convert_param_name(key)
                out_param_dict[out_key] = value
            out_params.append(out_param_dict)
        else:
            # Ordinal parameters 
            out_params.append(list(params))
            
    return sql, out_params