def myname():
    print("My name is Jared")
myname()

# Parameters and arguments

def fullname(firstname,lastname):
    print(firstname+" "+ lastname)
fullname("Jared","Kiptoo")

# Tuple as an argument

def mygame(*game):
    print(game[0])
mygame("basketball","tennis","football")

# key-value arguments
def rank(position1,position2,position3):
    print("Student in first position is "+position1)
rank(position1="Jared",position2="Ann",position3="Andrew")