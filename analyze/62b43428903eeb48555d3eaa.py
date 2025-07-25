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
            sql, param_map = self._format(sql, params)
            out_params.append(param_map)
        else:
            # For subsequent iterations, just convert params using same mapping
            if isinstance(params, Mapping):
                param_map = {i: params[key] for key, i in self._param_map.items()}
            else:
                param_map = {i: params[key] for key, i in enumerate(self._param_map)}
            out_params.append(param_map)

    # Convert param maps to lists if using ordinal out style
    if self.out_style in (ParamStyle.QMARK, ParamStyle.FORMAT):
        max_param = max(max(p.keys()) for p in out_params)
        out_params = [[p.get(i) for i in range(max_param + 1)] for p in out_params]

    return sql, out_params