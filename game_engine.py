import constants
import math
from bot import Bot
import pygame
from pygame import Vector2

class GameEngine:
    def __init__(self) -> None:
        self.bots = []
        self.bots.append(Bot(color=pygame.Color("orange"),
                             pos=constants.CENTER + Vector2(200, 200),
                             angle=math.pi / 2))

    def step(self):
        for bot in self.bots:
            dx = math.cos(bot.angle) * constants.SPEED
            dy = -1 * math.sin(bot.angle) * constants.SPEED
            new_pos = bot.pos + Vector2(dx, dy)
            max_distance = (constants.DISPLAY_SIZE - constants.BOT_SIZE) / 2
            bot.pos = new_pos
            # print(max_distance)
            # print(new_pos.distance_to(Vector2(constants.CENTER)))
            if new_pos.distance_to(Vector2(constants.CENTER)) > max_distance:
                center_to_player = bot.pos - constants.CENTER
                center_to_player.scale_to_length(max_distance)
                bot.pos = center_to_player + constants.CENTER