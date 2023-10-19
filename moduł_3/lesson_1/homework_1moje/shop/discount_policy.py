
def default_policy(total_price):
    return total_price

def loyal_customer(total_price):
    return total_price * 0.95

def holiday_season(total_price):
    if total_price > 100:
        return total_price - 20
    return total_price