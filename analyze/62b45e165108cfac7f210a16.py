def validate_as_prior_version(self, prior):
    """
    Check that prior is a valid prior version of the current inventory object.

    The input variable prior is also expected to be an InventoryValidator object
    and both self and prior inventories are assumed to have been checked for
    internal consistency.
    """
    # Check that prior is an InventoryValidator object
    if not isinstance(prior, type(self)):
        raise TypeError("Prior must be an InventoryValidator object")

    # Check that prior timestamp is before current timestamp
    if prior.timestamp >= self.timestamp:
        raise ValueError("Prior inventory must have earlier timestamp")

    # Check that all items in prior exist in current inventory
    for item_id in prior.inventory:
        if item_id not in self.inventory:
            raise ValueError(f"Item {item_id} from prior inventory missing in current")

    # Check that quantities only increase
    for item_id, prior_qty in prior.inventory.items():
        current_qty = self.inventory[item_id]
        if current_qty < prior_qty:
            raise ValueError(f"Quantity decreased for item {item_id}")

    return True