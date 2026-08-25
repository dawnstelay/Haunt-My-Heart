# CHARACTERS
define p = Character("Pheobe")
define f = Character("Felix")
define m = Character("Milo")
define l = Character("Luka")
define unknown = Character("???")
define yn = Character("[name]")


# VARIABLES
$ felixAffinity = 0
$ miloAffinity = 0
$ lukaAffinity = 0
$ exorcismPoints = 0

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

    yn "here's some text brochacho"

    show eileen happy

    yn "yo who is that???"




    return
