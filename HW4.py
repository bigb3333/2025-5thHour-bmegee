#1. Print Hello World!
print('hello world')
#1. Create a list with 5 strings containing 5 different names in it.
ben=['hat','sad','big','bad','cat']
#2. Append a new name onto the Name List.
ben.append('fin')
#3. Print out the 4th name on the list.
print(ben[3])
#4. Create a list with 4 different integers in it.
tin=[1,4,6,7]
#5. Insert a new integer into the 2nd spot and print the new list.
tin.insert(1,5)
print(tin)
#6. Sort the list from lowest to highest and print the sorted list.
tin.sort()
print(tin)
#7. Add the 1st three numbers on the sorted list together and print the sum.
rat=tin[0]+tin[1]+tin[2]
print(rat)
#8. Create a list with two strings, two variables, and too boolean values.
win=['sad','dan',1,4,True,False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(win[int(input())])