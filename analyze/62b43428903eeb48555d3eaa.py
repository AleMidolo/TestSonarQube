def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]:
    """
    将 SQL 使用 `self._converter.convert_many` 转换

    将 SQL 查询从 in-style 参数转换为 out-style 参数。

    *sql*（类型：`str` 或 `bytes`）是 SQL 查询语句。

    *many_params*（类型：`~collections.abc.Iterable`）包含每组 in-style 参数（*params*）。

      - *params*（类型：`~collections.abc.Mapping` 或  `~collections.abc.Sequence`）包含一组 in-style 参数。它将每个参数（类型：`str` 或 `int`）映射到对应的值。如果 `SQLParams.in_style` 是命名参数样式，那么 *params* 必须是一个 `~collections.abc.Mapping` 类型。如果 `SQLParams.in_style` 是序号参数样式，那么 **params** 必须是一个 `~collections.abc.Sequence` 类型。

    返回一个包含以下内容的元组（`tuple`）：

      - 格式化后的 SQL 查询（类型：`str` 或 `bytes`）。

      - 一个包含每组转换后的 out-style 参数（类型：`dict` 或 `list`）的列表。
    """
    formatted_sql = sql
    formatted_params = []

    for params in many_params:
        converted_sql, converted_params = self._converter.convert_many(sql, params)
        formatted_sql = converted_sql
        formatted_params.append(converted_params)

    return formatted_sql, formatted_params