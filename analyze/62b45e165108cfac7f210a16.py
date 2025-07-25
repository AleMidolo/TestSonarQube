def validate_as_prior_version(self, prior):
    """
    检查 `prior` 是否是当前库存（inventory）对象的有效先前版本。

    输入变量 `prior` 也应是一个 `InventoryValidator` 对象，并且假定 `self` 和 `prior` 的库存对象都已经过内部一致性检查。在类中返回 `error()`。
    """
    # 检查 prior 是否为 InventoryValidator 类型
    if not isinstance(prior, type(self)):
        return self.error("Prior version must be an InventoryValidator object")

    # 检查时间戳,确保 prior 版本早于当前版本
    if prior.timestamp >= self.timestamp:
        return self.error("Prior version timestamp must be earlier than current version")

    # 检查库存变化的合理性
    for item_id, current_qty in self.inventory.items():
        prior_qty = prior.inventory.get(item_id, 0)
        
        # 数量变化不能为负
        if current_qty < 0:
            return self.error(f"Invalid negative quantity for item {item_id}")
            
        # 检查数量变化是否合理
        qty_change = current_qty - prior_qty
        if qty_change < -prior_qty:  # 减少的数量不能超过之前的库存
            return self.error(f"Invalid quantity reduction for item {item_id}")

    # 所有检查通过
    return None