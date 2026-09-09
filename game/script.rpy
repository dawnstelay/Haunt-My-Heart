# CHARACTERS
define p = Character("Pheobe")
define f = Character("Felix")
define m = Character("Milo")
define l = Character("Luka")
define unknown = Character("???")
define yn = Character("[name]")


# VARIABLES
default felixAffinity = 0
default miloAffinity = 0
default lukaAffinity = 0
default exorcismPoints = 0

# BACKGROUNDS

# SPRITES

# The game starts here.

label splashscreen:
    
    return 

label start:

    $ name = renpy.input("what would you like to be called?")
    $ name = name.strip()
    if name == "":
        $ name = "Eve"

label prologue: 

    scene bg room

    yn "test"



label day1:

label day2:



    if ((felixAffinity > miloAffinity) and (felixAffinity >lukaAffinity)):
        jump fday3
    
    if ((lukaAffinity > felixAffinity) and (lukaAffinity > miloAffinity)):
        jump lday3

    if ((miloAffinity > lukaAffinity) and (miloAffinity > felixAffinity)):
        jump mday3


    if (lukaAffinity == felixAffinity == miloAffinity):
        jump commonRoute
    return
