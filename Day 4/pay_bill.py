import random


string_name = input("Enter your name one by one with separated comma : ")
names = string_name.strip()
names = names.split(",")
random_person =  random.randint(0,len(names)-1)
print(len(names))
if random_person==0:
    print(names[0])
elif random_person==1:
    print(names[1])
else:
    print(names[2])
