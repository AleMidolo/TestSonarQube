def _update_context(self, context):
    """
    更新 *context*，使其包含此图的属性。

    *context.error* 会附加错误的索引。
    例如，对于一个具有字段 "E, t, error_E_low" 的图，其子上下文可能为：
    {"error": {"x_low": {"index": 2}}}
    请注意，错误名称被称为 "x"、"y" 和 "z"（这对应于前三个坐标，如果它们存在的话），这使得绘图更加简化。
    现有的值不会从 *context.value* 及其子上下文中移除。

    此方法在图的“销毁”过程中被调用（例如，在 :class:`.ToCSV` 中）。
    这里的“销毁”是指在流程中将图转换为另一种结构（如文本）。
    在此过程中，图对象实际上并未被真正销毁。
    """
    if not hasattr(context, 'error'):
        context.error = {}

    # 假设 self.fields 是图的字段列表
    for i, field in enumerate(self.fields):
        if field.startswith('error_'):
            # 提取错误类型，例如 "x_low" 或 "y_high"
            error_type = field[len('error_'):]
            axis = error_type.split('_')[0]  # 提取 "x", "y", 或 "z"
            error_key = f"{axis}_{error_type.split('_')[1]}"  # 例如 "x_low"
            
            # 更新 context.error
            if axis not in context.error:
                context.error[axis] = {}
            context.error[axis][error_key] = {"index": i}