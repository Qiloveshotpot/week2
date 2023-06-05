recipient_name = input("who is going to receive this message? ")
sender_name = input("who is sending the message? ")
year_of_birth = int(input("recipient's year of birth? "))
current_year = int(input("current year? "))
age = current_year - year_of_birth
personalized_message = input("give your birthday wishes here: ")

print()
print("Hi", recipient_name, ", let's celebrate your", age, "years of awesomeness!")
print("Wishing you a day filled with joy and laughter as you turn", age, "!")
print()
print(personalized_message)
print()
print("With love and best wishes,")
print(sender_name)





















