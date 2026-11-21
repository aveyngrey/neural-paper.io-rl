import constants
import math
from bot import Bot
import pygame
from pygame import Vector2

class GameEngine:
    def __init__(self) -> None:
        self.bots = []
        self.bots.append(Bot(color=pygame.Color("orange"),
                             pos=constants.CENTER + Vector2(50, 50),
                             angle=math.pi))

    def step(self):
        for bot in self.bots:
            dx = math.cos(bot.angle) * constants.SPEED
            dy = math.sin(bot.angple) * constants.SPEED
            bot.self.pos += Vector2(dx, dy)