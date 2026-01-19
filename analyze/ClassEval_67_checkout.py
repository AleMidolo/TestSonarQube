def checkout(self):
    """
    ऑर्डर किए गए व्यंजनों की चेकआउट करें। यदि self.selected_dishes खाली नहीं है, तो चेकआउट करने के लिए calculate_total
    विधि को कॉल करें।
    :return यदि self.selected_dishes खाली है तो Flase, अन्यथा total (calculate_total का लौटने वाला मान)।
    >>> order = Order()
    >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    >>> order.sales = {"dish1": 0.8}
    >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
    True
    >>> order.checkout()
    32.0
    """
    if not self.selected_dishes:
        return False
    else:
        return self.calculate_total()