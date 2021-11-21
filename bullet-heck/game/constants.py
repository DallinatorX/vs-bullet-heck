import os
import random

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BRICK0 = os.path.join(os.getcwd(), "./batter/assets/brick-0.png")
IMAGE_BRICK1 = os.path.join(os.getcwd(), "./batter/assets/brick-1.png")
IMAGE_BRICK2 = os.path.join(os.getcwd(), "./batter/assets/brick-2.png")
IMAGE_BRICK3 = os.path.join(os.getcwd(), "./batter/assets/brick-3.png")
IMAGE_BRICK4 = os.path.join(os.getcwd(), "./batter/assets/brick-4.png")
IMAGE_BRICK5 = os.path.join(os.getcwd(), "./batter/assets/brick-5.png")
IMAGE_BRICK6 = os.path.join(os.getcwd(), "./batter/assets/brick-6.png")
IMAGE_BRICK = [IMAGE_BRICK0,IMAGE_BRICK1,IMAGE_BRICK2,IMAGE_BRICK3,IMAGE_BRICK4,IMAGE_BRICK5,IMAGE_BRICK6]


IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

PADDLE_SPEED = 15

PADDLE_WIDTH = 96
PADDLE_HEIGHT = 24

BALL_WIDTH = 24
BALL_HEIGHT = 24

BRICK_COUNT_COLLUMS = 10
BRICK_COUNT_ROWS = 10

