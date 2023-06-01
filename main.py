from datetime import datetime, date

def calculate_age(year_of_birth):
    year_of_birth = datetime.strptime(year_of_birth, "%Y")
    today = date.today()
    return today.year - year_of_birth.year - ((today.month, today.day) < (year_of_birth.month, year_of_birth.day))


recipient_name = input("enter a recipient name: ")
print(recipient_name)

year_of_birth = input("enter year of birth: ")
print(year_of_birth)

message = input("enter a message: ")
print(message)

sender_name = input("enter sender name: ")
print(sender_name)

age = calculate_age(year_of_birth)

final_message = f"""
{recipient_name}, let's celebrate your {age} years of awesomeness!
Wishing you a day filled with joy and laughter as you turn {age}!

{message}

With love and best wishes,
{sender_name}
"""

print(final_message)
