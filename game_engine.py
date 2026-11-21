import constants as const
import math
from bot import Bot
import pygame
from pygame import Vector2

class GameEngine:
    def __init__(self) -> None:
        self.bots = []
        self.bots.append(Bot(color=pygame.Color("orange"),
                             pos=const.CENTER + Vector2(200, 200),
                             angle=math.pi / 2))

    def step(self):
        for bot in self.bots:
            new_pos = bot.pos + (bot.direction * const.MOVE_SPEED)
            max_distance = (const.DISPLAY_SIZE - const.BOT_SIZE) / 2
            bot.pos = new_pos
            # print(max_distance)
            # print(new_pos.distance_to(Vector2(const.CENTER)))
            if new_pos.distance_to(const.CENTER) > max_distance:
                center_to_player = bot.pos - const.CENTER
                center_to_player.scale_to_length(max_distance)
                bot.pos = center_to_player + const.CENTER

            future_pos = bot.pos + bot.direction * const.MOVE_SPEED * 2
            if future_pos.distance_to(const.CENTER) > max_distance:
                bot.turn(const.TURN_SPEED)

