def formatmany(
                self,
                sql: AnyStr,
                many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
        ) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Determine the parameter style based on the SQL query
    if self.SQLParams.in_style == 'named':
        # Convert to named parameters
        formatted_sql = sql
        out_params = []
        for params in many_params:
            out_param = {f":{key}": value for key, value in params.items()}
            out_params.append(out_param)
            formatted_sql = formatted_sql.replace("?", ", ".join(out_param.keys()), 1)
    else:
        # Convert to ordinal parameters
        formatted_sql = sql
        out_params = []
        for params in many_params:
            out_param = list(params)
            out_params.append(out_param)
            formatted_sql = formatted_sql.replace("?", "?", len(out_param))
    
    return formatted_sql, out_params