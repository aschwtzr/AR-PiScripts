from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

O = [0, 0, 0]  # Off  
X = [255, 255, 255]  # White


blank = [
         O, O, O, O, O, O, O, O,
         O, O, O, O, O, O, O, O,
         O, O, O, O, O, O, O, O,
         O, O, O, O, O, O, O, O,
         O, O, O, O, O, O, O, O,
         O, O, O, O, O, O, O, O,
         O, O, O, O, O, O, O, O,
         O, O, O, O, O, O, O, O,
         ]

def showHouse():
    house = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, X, O, O, O, O, X, O,
    O, X, X, X, X, X, X, O,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, X, X, X, O, O
    ]

    sense.set_pixels(house)

def showHeart():
    r = [0,0,0]

    counter = 0
    while counter < 30:
        if counter%2 == 0:
            red = 255
        else:
            red = 0
        r = [red,0,0]
        counter+=1
        sleep(.5)
        heart = [
             O, O, X, O, O, X, O, O,
             O, X, r, X, X, r, X, O,
             X, r, r, r, r, r, r, X,
             X, r, r, r, r, r, r, X,
             X, r, r, r, r, r, r, X,
             O, X, r, r, r, r, X, O,
             O, O, X, r, r, X, O, O,
             O, O, O, X, X, O, O, O,
             ]
        
        sense.set_pixels(heart)
        print(counter/2)

    sense.set_pixels(heart)

