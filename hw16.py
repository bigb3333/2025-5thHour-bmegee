#Name:
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def average(a,b,c):
    total = a + b + c
    avg=total/3
    print("The average is: ", avg)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animals_list(*animals):
    print(animals[2])
#4. Create a def function that loops from 1 to the number put in the argument.
def loop(r):
    for i in range (1,r+1):
       print(i)
#5. Call all  the functions created in 1 - 4 with relevant arguments.
hello_world()
average(1,2,3)
animals_list("dog", "cat", "fish","bird","mole")
loop(3)
#6. Create a variable x that has the value of 2. Print x
x=2
#7. Create a def function that multiplies the value of 2 by a random number between 1 and 5.
def multiplie():
    global x
    x *= 2
    print(x)
    x = x * random.randint(1,5)
    print(x)
#8. Print the new value of x.
multiplie()
print(x)