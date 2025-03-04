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
            raise ValueError(f"Cantidad actual de {product_id} es menor que en versión previa")

    # Verificar que los IDs de productos sean consistentes
    if not set(prior.products.keys()).issubset(set(self.products.keys())):
        raise ValueError("Los productos del inventario previo deben existir en el actual")

    # Si pasa todas las validaciones, retornar True
    return True