import  random


# Define Color
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

# Define Window
WIDTH = 1920
HEIGHT = 1080

# Define FPS
FPS = 60

def getRandomColor():
    return (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))