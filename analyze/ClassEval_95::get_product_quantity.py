def get_product_quantity(self, product_id):
        """
        Ottieni la quantità di un prodotto specifico tramite product_id.
        :param product_id, int
        :return: se il product_id è presente nell'inventario, restituisce la quantità corrispondente,
                altrimenti restituisce False.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.get_product_quantity(1)
        3
        >>> warehouse.get_product_quantity(2)
        False
        """
        return self.inventory[product_id]['quantity'] if product_id in self.inventory else False