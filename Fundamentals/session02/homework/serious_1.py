height = int(input("Height(cm): "))
weight = int(input("Weight(kg): "))

BMI = weight/((height/100)**2)

if BMI < 16:
    print(BMI, 'Severely underweight')
elif BMI < 18.5:
    print(BMI, 'Underweight')
elif BMI < 25:
    print(BMI, 'Normal')
elif BMI < 30:
    print(BMI, 'Overweight')
else:
    print(BMI, 'Obese')
