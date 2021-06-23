print("Welcome to the top calculator\n")
total_bill = int(input("What was the total bill? $"))
tip_percentage = int(input("What percentage top would you like to give? 10, 12, or 15? "))
actual_tip_with_bill = (total_bill*tip_percentage)/100 + total_bill
number_of_people = int(input("How many people to split the bill? "))

each_person_get = round(actual_tip_with_bill/number_of_people,2)
# formatting string to show the 2 decmal point {:.2f}
each_person_get = "{:.2f}".format(each_person_get)
print(f"Each person should pay {each_person_get}")