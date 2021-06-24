
height= float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kg: \n"))
bmi = round(weight / height**2)

1
if(bmi <18.5):
    print(f"{bmi}" + " " + "You are underweight")
elif bmi<25:
    print(f"{bmi}" + " " + "You are Normal Weight")
elif bmi<30:
    print(f"{bmi}" + " " + "You are Over Weight")
elif bmi<35:
    print(f"{bmi}" + " " + "You are Over Obese")
else:
    print(f"{bmi}" + " " + "You are Over Clinically obese")
    
    


