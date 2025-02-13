from dateutil.relativedelta import relativedelta

def normalized(self):
    total_hours = int(self.hours) + int(self.days * 24) + int(self.months * 30 * 24) + int(self.years * 365 * 24)
    total_days = int(self.days) + int(self.months * 30) + int(self.years * 365)
    return relativedelta(days=total_days, hours=total_hours)