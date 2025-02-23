def format(
                self,
                sql: AnyStr,
                params: Union[Dict[Union[str, int], Any], Sequence[Any]],
        ) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    将 SQL 使用 `self._converter.convert` 方法进行转换

    将 SQL 查询从 in-style 参数转换为 out-style 参数。

    *sql*（类型：`str` 或 `bytes`）是 SQL 查询语句。

    *params*（类型：`~collections.abc.Mapping` 或 `~collections.abc.Sequence`）包含一组 in-style 参数。它将每个参数（类型：`str` 或 `int`）映射到对应的值。如果 `SQLParams.in_style` 是命名参数样式，那么 *params* 必须是一个 `~collections.abc.Mapping` 类型。如果 `SQLParams.in_style` 是序号参数样式，那么 **params** 必须是一个 `~collections.abc.Sequence` 类型。

    返回一个包含以下内容的元组（`tuple`）：

      - 格式化后的 SQL 查询（类型：`str` 或 `bytes`）。

      - 转换后的 out-style 参数集合（类型：`dict` 或 `list`）。
    """
    # Assuming self._converter.convert is defined and works as expected
    if isinstance(params, dict):
        # Named parameters
        out_params = {key: self._converter.convert(value) for key, value in params.items()}
        formatted_sql = sql.format(**out_params)
    elif isinstance(params, (list, tuple)):
        # Positional parameters
        out_params = [self._converter.convert(value) for value in params]
        formatted_sql = sql.format(*out_params)
    else:
        raise TypeError("params must be a dictionary or a sequence")

    return formatted_sql, out_params