#Name:
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:
height=int(input("enter your height here in inches: "))
weight =int(input("enter your weight here in pounds: "))
bmi = weight/(height**2)
print(bmi)
if bmi < 18.5:
    print("you are underweight")
elif bmi >= 18.5 and bmi <= 25:
    print("you are normal")
elif bmi >= 25 and bmi <= 30:
    print("you are overweight")
else:
    print("you are obese")