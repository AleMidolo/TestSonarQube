def validate_as_prior_version(self, prior):
    # Verificar que prior sea una instancia de InventoryValidator
    if not isinstance(prior, type(self)):
        raise TypeError("El inventario previo debe ser del mismo tipo")

    # Verificar que la fecha del prior sea anterior
    if prior.date >= self.date:
        raise ValueError("La fecha del inventario previo debe ser anterior")

    # Verificar que los productos existentes en prior existan en self
    # con cantidades mayores o iguales
    for product_id, prior_qty in prior.quantities.items():
        if product_id not in self.quantities:
            raise ValueError(f"Producto {product_id} no existe en inventario actual")
        if self.quantities[product_id] < prior_qty:
            raise ValueError(f"Cantidad de producto {product_id} es menor que en versión previa")

    # Verificar que los productos tengan los mismos atributos
    for product_id in prior.products:
        if product_id not in self.products:
            raise ValueError(f"Producto {product_id} no existe en inventario actual")
        if prior.products[product_id] != self.products[product_id]:
            raise ValueError(f"Atributos del producto {product_id} han cambiado")

    return True