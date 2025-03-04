def validate_as_prior_version(self, prior):
    # Verificar que prior sea una instancia de InventoryValidator
    if not isinstance(prior, type(self)):
        raise TypeError("El inventario previo debe ser del mismo tipo")

    # Verificar que la fecha del prior sea anterior
    if prior.date >= self.date:
        raise ValueError("El inventario previo debe tener una fecha anterior")

    # Verificar que los productos existentes en prior existan en self
    # con cantidades mayores o iguales
    for product_id, prior_qty in prior.quantities.items():
        if product_id not in self.quantities:
            raise ValueError(f"Producto {product_id} falta en el inventario actual")
        if self.quantities[product_id] < prior_qty:
            raise ValueError(f"Cantidad del producto {product_id} es menor que en el inventario previo")

    # Verificar que los precios sean consistentes
    for product_id, prior_price in prior.prices.items():
        if product_id in self.prices and self.prices[product_id] != prior_price:
            raise ValueError(f"Precio inconsistente para producto {product_id}")

    return True