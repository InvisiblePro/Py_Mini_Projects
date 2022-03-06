# BMI_Calculator
height = float(input("Enter your height : "))
weight = float(input("Enter your weight : "))


def BMI(h, w):
    h = h / 100
    bmi = w / h**2
    if bmi < 16:
        return "Severely Underweight, have healthy and nutrious food...", bmi
    elif bmi >= 16 and bmi <= 18.5:
        return "Underweight, Oops! you just missed...", bmi
    elif bmi >= 18.5 and bmi <= 25:
        return "Healthy, maintain this regularly...", bmi
    elif bmi >= 25 and bmi <= 30:
        return "Overweight, have some cycling daily...", bmi
    elif bmi >= 30:
        return "Severely Overweight, join diet..", bmi


quote, bmi = BMI(height, weight)

print("Your bmi is {}, you are {}".format(bmi, quote))
