def get_supported_currencies(self):
        """
        返回支持的货币类型列表
        :return: list, 所有支持的货币类型
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """
        return list(self.rates.keys())