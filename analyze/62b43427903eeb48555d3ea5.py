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
    # 检查参数类型是否匹配样式
    if self.in_style.is_named():
        if not isinstance(params, Mapping):
            raise TypeError("Named parameter style requires mapping params")
    else:
        if not isinstance(params, Sequence) or isinstance(params, (str, bytes)):
            raise TypeError("Positional parameter style requires sequence params")

    # 转换参数
    converted_params = {}
    if isinstance(params, Mapping):
        # 命名参数样式
        for key, value in params.items():
            converted_params[key] = self._converter.convert(value)
    else:
        # 序号参数样式
        converted_params = [self._converter.convert(value) for value in params]

    # 根据输出样式格式化SQL
    if self.out_style.is_named():
        # 如果输入是序号样式但输出需要命名样式
        if isinstance(converted_params, list):
            named_params = {f"p{i}": val for i, val in enumerate(converted_params)}
            formatted_sql = self._convert_positional_to_named(sql, len(converted_params))
            converted_params = named_params
        else:
            formatted_sql = sql
    else:
        # 如果输入是命名样式但输出需要序号样式
        if isinstance(converted_params, dict):
            param_list = []
            formatted_sql = self._convert_named_to_positional(sql, converted_params, param_list)
            converted_params = param_list
        else:
            formatted_sql = sql

    return formatted_sql, converted_params