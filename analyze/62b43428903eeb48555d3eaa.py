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
            out_param = {}
            for key, value in params.items():
                out_param[key] = value
                formatted_sql = formatted_sql.replace(f":{key}", f"%({key})s")
            out_params.append(out_param)
    else:
        # Convert to ordinal parameters
        formatted_sql = sql
        out_params = []
        for params in many_params:
            out_param = list(params)
            for index in range(len(params)):
                formatted_sql = formatted_sql.replace(f"?{index + 1}", f"%s")
            out_params.append(out_param)

    return formatted_sql, out_params