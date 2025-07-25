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
    # Convert the SQL query using the converter
    formatted_sql = self._converter.convert(sql)
    
    # Convert the params to out-style
    if isinstance(params, dict):
        # If params is a dictionary, convert it to out-style dictionary
        out_params = {k: self._converter.convert_value(v) for k, v in params.items()}
    else:
        # If params is a sequence, convert it to out-style list
        out_params = [self._converter.convert_value(v) for v in params]
    
    return formatted_sql, out_params