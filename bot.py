import pygame
from pygame.typing import ColorLike
from pygame.math import Vector2
import constants as const
import math

class Bot:
    def __init__(self, color: ColorLike = pygame.Color("black"), 
                 pos: Vector2 = Vector2(const.DISPLAY_SIZE / 2, const.DISPLAY_SIZE / 2), 
                 angle: float = math.pi / 2) -> None:
        self.color = color
        self.color = pygame.Color(color)
        self.territory_color = self.color.lerp(pygame.Color(0, 0, 0), 0.3)
        self.trail_color = self.color.lerp(pygame.Color(255, 255, 255), 0.3)
        
        self.start_pos = pos
        self.pos = pos
        self.angle = angle
        self.direction = Vector2(math.cos(self.angle), -1 * math.sin(self.angle))

    def turn(self, d_angle) -> None:
        self.angle += d_angle
        self.direction = Vector2(math.cos(self.angle), -1 * math.sin(self.angle))
    