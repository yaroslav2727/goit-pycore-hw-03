import datetime

def get_days_from_today(date):
    our_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.datetime.now()
    return (current_date - our_date).days