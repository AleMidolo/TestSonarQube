from dateutil.relativedelta import relativedelta

def normalized(self):
    total_days = int(self.days) + int(self.hours // 24)
    total_hours = int(self.hours) % 24
    return relativedelta(days=total_days, hours=total_hours)