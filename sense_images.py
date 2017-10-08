from sense_hat import SenseHat
sense = SenseHat()

def showHouse():
    O = [0, 0, 0]  # Off  
    X = [255, 255, 255]  # White

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
