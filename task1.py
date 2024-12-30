import datetime

def get_days_from_today(date):
    try:
        our_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Incorrect date format. Please use YYYY-MM-DD."
    
    current_date = datetime.datetime.now()
    return (current_date - our_date).days