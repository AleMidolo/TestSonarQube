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
        
    # Check that all items in prior exist in current with same or greater quantity
    for item_id, prior_quantity in prior.inventory.items():
        if item_id not in self.inventory:
            raise ValueError(f"Item {item_id} from prior inventory missing in current")
        if self.inventory[item_id] < prior_quantity:
            raise ValueError(f"Item {item_id} has decreased quantity from prior version")
            
    return True