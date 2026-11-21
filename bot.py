import pygame
from pygame.typing import ColorLike
from pygame.math import Vector2
import constants
import math

class Bot:
    def __init__(self, color: ColorLike = pygame.Color("black"), 
                 pos: Vector2 = Vector2(constants.DISPLAY_SIZE / 2, constants.DISPLAY_SIZE / 2), 
                 angle: float = math.pi / 2) -> None:
        self.color = color
        self.pos = pos
        self.angle = angle
        self.size = constants.DISPLAY_SIZE / 20