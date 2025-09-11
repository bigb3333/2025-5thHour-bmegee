#1. Import the "random" library
import random
#2. print "Hello World!"
print ('hello world')
#3. Create three different variables that each randomly generate an integer between 1 and 10
big1=random.randint(1,10)
big2=random.randint(1,10)
big3=random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print (big1,big2,big3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
sand = big1+2
sand2 = big2-4
sand3 = big3*1.5
#6. Print each result from #5 on the same line.
print (sand,sand2,sand3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
fit =[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
fit.sort()
print (fit)
#9. Add together the highest three numbers in the list from #7 and print the result.
you = fit[1]+fit[2]+fit[3]
print (you)
#10. Create a list with 5 names of other students in this class and print the list.
guy=['aiden','bryson','iven','dylen','jude']
print (guy)
#11. Shuffle the list in #10 and print the list again.
random.shuffle (guy)
print (guy)
#12. Print a random choice from the list of names from #10.
print(random.choice(guy))
print(random.choice(guy))
print(random.choice(guy))