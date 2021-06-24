year = int(input("Type a year to check leap year: "))
if(year % 4 ==0):
    if(year % 100 ==0):
        if(year % 400 == 0):
            print(f"{year} Leap Year")
        else:
            print(f"{year} Not a leap year")
    else:
        print(f"{year} a leap year")
else:
    print(f"{year} Not a leap year")