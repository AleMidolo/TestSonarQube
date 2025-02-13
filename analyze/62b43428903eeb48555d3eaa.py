def formatmany(
                self,
                sql: AnyStr,
                many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
        ) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    out_params = []
    if isinstance(sql, bytes):
        sql = sql.decode('utf-8')
    
    for params in many_params:
        if isinstance(params, dict):
            out_param = {f'out_{key}': value for key, value in params.items()}
        elif isinstance(params, (list, tuple)):
            out_param = [f'out_{i}' for i in params]
        else:
            raise TypeError("params must be a dict or a sequence")
        
        out_params.append(out_param)
    
    formatted_sql = sql.replace("?", "out_param_placeholder")
    
    return formatted_sql, out_params