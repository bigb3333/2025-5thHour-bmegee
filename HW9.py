#Name:
#Class: 6th Hour
#Assignment: HW9

import random

#1. Print "Hello World!"
print('hello world')
#2. Create a list with three variables that each randomly generate a number between 1 and 100
big=random.randint(1,100),random.randint(1,100),random.randint(1,100)


#3. Print the list.
print(big)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if big[0]<big[1] and big[0]<big[2]:
    print("big is bigger than 2 and 3 ")
    num=big[0]
elif big[1]>big[0] and big[1]>big[2]:
    print ("2 is bigger than 3 and 1")
    num=big[1]
else:
    print ("3 is bigger than 2 and 1")
    num=big[2]

#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num%2==0:
    if num%3==0:
        print ("divisible by 3 and 2")
    else:
        print ("divisible by 2 but not 3")
else:
    if num%3==0:
        print ("divisible by 3 but not 2")
    else:
        print ("not divisible by 3 or 2 ")