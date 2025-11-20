#Name:
#Class: 5th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

x=0


player=int(input("enter the number of players"))


for h in range(1,player+1):
    vote=int(input("enter the vote 1-5"))
    while vote < 0 or vote > 5:
        print("vote must be between 1 and 5")
        vote=int(input("enter the vote 1-5"))
    else:
        x+=vote
print(x/player)