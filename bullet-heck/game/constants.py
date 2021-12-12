import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

P1_SHIP_SPEED = 8
P2_SHIP_SPEED = 4
P1_BULLET_SPEED = 10

P1_BULLET_COOL_DOWN = 10
P2_MAIN_FIRE_COOL_DOWN = 25
P2_LEFT_ANGLE_FIRE_COOL_DOWN = 25
P2_RIGHT_ANGLE_FIRE_COOL_DOWN = 25
P2_CIRCLE_FIRE_COOL_DOWN = 25

P2_CIRCLE_FIRE_BULLET_COUNT = 8
P2_RIGHT_ANGLE_FIRE_BULLET_COUNT = 6
P2_LEFT_ANGLE_FIRE_BULLET_COUNT = 6


P2_BULLET_SPEED = 5
P2_HP = 5

P1_SHIP_IMAGE = os.path.join(os.getcwd(), "./bullet-heck/assets/rocket3.png")
P2_SHIP_IMAGE = os.path.join(os.getcwd(), "./bullet-heck/assets/UFO2.png")


PAUSE_MENU_MUSIC = os.path.join(os.getcwd(), "./bullet-heck/assets/Pause-Menu-Song.wav")
MAIN_MUSIC = os.path.join(os.getcwd(), "./bullet-heck/assets/Bleeping_Demo.wav")




