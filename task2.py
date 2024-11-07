import random

def get_numbers_ticket(min, max, quantity):
    if min < 1:
        min = 1
    if max > 1000:
        max = 1000
    if (max+1) - min < quantity:
        return []
    
    numbers = random.sample(range(min, max+1), quantity)
    sorted_numbers = sorted(numbers)
    return sorted_numbers

print(get_numbers_ticket(1, 49, 6))