from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today()
    upcoming_birthdays = []
    
    for user in users:

        day_of_birth = datetime.strptime(user['birthday'], '%Y.%m.%d')
        
        birthday = day_of_birth.replace(year=today.year)
        
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        
        days_difference = (birthday - today).days
        
        if 0 <= days_difference <= 7:

            if birthday.weekday() >= 5:  # 5 = Субота, 6 = Неділя
                birthday += timedelta(days=(7 - birthday.weekday()))
            
            congratulation_date = birthday.strftime('%Y.%m.%d')
            
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date
            })
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.11.03"},
    {"name": "Jane Smith", "birthday": "1990.11.06"}
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("List of greetings this week:", upcoming_birthdays)