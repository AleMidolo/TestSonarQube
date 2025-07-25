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
            out_param = {key: params[key] for key in params}
            out_params.append(out_param)
            # Replace named parameters in the SQL
            for key in out_param:
                formatted_sql = formatted_sql.replace(f":{key}", str(out_param[key]))
    else:
        # Convert to ordinal parameters
        formatted_sql = sql
        out_params = []
        for params in many_params:
            out_param = list(params)
            out_params.append(out_param)
            # Replace ordinal parameters in the SQL
            for index, value in enumerate(out_param):
                formatted_sql = formatted_sql.replace(f"?{index + 1}", str(value))

    return formatted_sql, out_params