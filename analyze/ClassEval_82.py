class StockPortfolioTracker:
    def __init__(self, cash_balance):
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        existing_stock = self.find_stock(stock['name'])
        if existing_stock:
            existing_stock['quantity'] += stock['quantity']
        else:
            self.portfolio.append(stock)

    def find_stock(self, stock_name):
        for pf in self.portfolio:
            if pf['name'] == stock_name:
                return pf
        return None

    def remove_stock(self, stock):
        existing_stock = self.find_stock(stock['name'])
        if existing_stock and existing_stock['quantity'] >= stock['quantity']:
            existing_stock['quantity'] -= stock['quantity']
            if existing_stock['quantity'] == 0:
                self.portfolio.remove(existing_stock)
            return True
        return False

    def buy_stock(self, stock):
        if self.is_purchase_exceeding_cash(stock):
            return False
        self.add_stock(stock)
        self.cash_balance -= stock['price'] * stock['quantity']
        return True

    def is_purchase_exceeding_cash(self, stock):
        return stock['price'] * stock['quantity'] > self.cash_balance

    def sell_stock(self, stock):
        if not self.remove_stock(stock):
            return False
        self.cash_balance += stock['price'] * stock['quantity']
        return True

    def calculate_portfolio_value(self):
        total_value = self.cash_balance + self.calculate_stocks_value()
        return total_value

    def calculate_stocks_value(self):
        return sum(stock['price'] * stock['quantity'] for stock in self.portfolio)

    def get_portfolio_summary(self):
        summary = [{"name": stock["name"], "value": self.get_stock_value(stock)} for stock in self.portfolio]
        portfolio_value = self.calculate_portfolio_value()
        return portfolio_value, summary

    def get_stock_value(self, stock):
        return stock['price'] * stock['quantity']