# CHARACTERS
define p = Character("Pheobe")
define f = Character("Felix")
define m = Character("Milo")
define l = Character("Luka")
define unknown = Character("???")


# VARIABLES
$ felixAffinity = 0
$ miloAffinity = 0
$ lukaAffinity = 0
$ exorcismPoints = 0

# BACKGROUNDS

# SPRITES

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
