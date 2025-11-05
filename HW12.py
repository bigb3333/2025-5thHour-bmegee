#Name:
#Class: 5th Hour
#Assignment: HW12
import time
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i=5
while i >= 0:
    print(i)
    time.sleep(0.4)
    i -=1
else:
    print("hello world")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
l =1
while l <= 30:
    if l % 2 == 0:
        print(l)
        l+=1
    else:l+=1


#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.

#5. Create a while loop that asks for a number input until the user inputs the number 0.