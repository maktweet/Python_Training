age = input("What is your current age: \n")
years_remaining = 90 - int(age)

days = years_remaining * 365
months = years_remaining * 12
weeks = years_remaining * 52

print(f"You have {days} days and {weeks} weeks and {months} months")
