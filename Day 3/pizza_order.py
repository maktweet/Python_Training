size = input("Piza size- 'S', 'M', 'L' : ")
add_p = input("Want to add pepperoni, 'Y', 'N' : ")
extra_cheese = input("Want to add extra Cheese, 'Y', 'N' : ")

bill = 0

if size == 'S':
    bill =15
    if add_p == 'Y':
        bill +=2
    if extra_cheese == 'Y':
        bill += 1

elif size == 'M':
    bill = 20
    if add_p == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
else:  
    bill = 25
    if add_p == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
print(f"You Total Final bill is: ${bill}")

