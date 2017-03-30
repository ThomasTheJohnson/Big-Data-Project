from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True

X = [255, 255, 0]
O = [76, 0, 153]

hi = [
O, O, O, O, O, O, O, O,
X, O, X, X, X, X, O, X,
X, O, X, O, O, X, O, X,
X, O, X, X, X, X, O, X,
X, O, O, O, X, X, O, X,
X, X, X, X, X, X, X, X,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

sense.set_pixels(hi)
#sleep(1)
#sense.clear()
#sleep(1)
#sense.set_pixels(hi)
#sleep(1)
#sense.clear()
