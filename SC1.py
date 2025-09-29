
#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
badguys={
    'eat':{
    'name':'Bob',
    'age':18 ,
    'height':70 ,
        'damage':123
    },
    'eat2':{
    'name':'bill',
    'age':16 ,
    'height':100 ,
        'damage':1190 ,
    },
    'eat3':{
    'name':'ash',
    'age':46 ,
    'height':13 ,
        'damage':500 ,
    },
    'eat4':{
    'name':'big',
    'age':34 ,
    'height':12 ,
        'damage':543 ,
    },
    'eat5':{
    'name':'den',
    'age':98 ,
    'height':67 ,
        'damage':67676767 ,
    },
}

badguys['eat']['damage']=int(input())
print(badguys['eat'])



