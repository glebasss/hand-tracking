import cv2
import mediapipe as mp
import time
from game import *

game = SoccerGame()
cap = cv2.VideoCapture(2)
game.play_game_ball(cap)
