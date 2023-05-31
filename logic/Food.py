import pygame
import math
from . import GameObject, Player
from random import randint



# прописываем класс еды, на основе которого будем создавать объекты
class Food(GameObject):

    def __init__(self, 
                 speed: float,
                 chaos_ticks_a: int, chaos_ticks_b: int, # сколько времени еда должна двигаться в выбранном направлении. 
                 chaos_angle_a: int, chaos_angle_b: int, # диапазон случайных углов направления движения еды.
                 chaos_position_x_a: int, chaos_position_x_b: int, # диапазон стартовых позиций X. 
                 chaos_position_y_a: int, chaos_position_y_b: int, # диапозон стартовых позиций Y. 
                 recovery_points: int,
                 recreation_x: int, # Граница пересоздания. 
                 spriteSheetName: str, state: str) -> None:
        self._startTicks = pygame.time.get_ticks()
        self.__genTicks = lambda: randint(chaos_ticks_a, chaos_ticks_b) 
        self._endTicks = self.__genTicks() 
        self.__genAngle = lambda: randint(chaos_angle_a, chaos_angle_b)
        self._angle = self.__genAngle()
        self._speed = speed
        self._recreation_x = recreation_x
        self.__genPosX = lambda: randint(chaos_position_x_a, chaos_position_x_b)
        posX = self.__genPosX()
        self.__genPosY = lambda: randint(chaos_position_y_a, chaos_position_y_b)
        posY = self.__genPosY()
        self.recovery_points = recovery_points
        self.living_hero = 0
        self.__living_hero = lambda: + self.recovery_points
        super().__init__(posX, posY, spriteSheetName, state)

    def update(self, collide):

        # смотрим истек ли срок движения по выбранному направлению. если да то меняем угол
        ticks = pygame.time.get_ticks()
        if (ticks - self._startTicks > self._endTicks):
            self._angle = self.__genAngle()
            self._startTicks = pygame.time.get_ticks()
            self._endTicks = self.__genTicks()

        # двигаемся под выбранным углом
        self._positionX += self._speed * math.cos(self._angle * math.pi / 180)
        self._positionY += self._speed * math.sin(self._angle * math.pi / 180)

        # если достигли края или столкнулись с игроком, пересоздаём
        if self._positionX < self._recreation_x or collide:
            self._positionX = self.__genPosX()
            self._positionY = self.__genPosY()

        if collide:
           self.living_hero = self.__living_hero()
        else:
           self.living_hero = 0
        return self.living_hero
        