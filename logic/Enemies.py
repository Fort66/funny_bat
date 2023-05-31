import pygame
import math
from . import GameObject, Player
from random import randint



# прописываем класс еды, на основе которого будем создавать объекты
class Enemies(GameObject):

    def __init__(self, 
                 speed: float,
                 chaos_position_x_a: int, chaos_position_x_b: int, # диапазон стартовых позиций X. 
                 chaos_position_y_a: int, chaos_position_y_b: int, # диапазон стартовых позиций Y. 
                 attack_distance_x: int, # позиция принятия решения об атаке
                 fly_enemy: bool, # признак летающего врага
                 random_attack_range: int, # диапазон случайных атак от 0 до заданного. целое число. если выпадает середина, то атака
                 damage_points: int, # урон от атаки
                 height_jump: int, # высота прыжка для наземного врага
                 recreation_x: int, # Граница пересоздания. 
                 spriteSheetName: str, state: str) -> None:
        
        self._speed = speed
        self._recreation_x = recreation_x
        self.__genPosX = lambda: randint(chaos_position_x_a, chaos_position_x_b)
        posX = self.__genPosX()
        self.__genPosY = lambda: randint(chaos_position_y_a, chaos_position_y_b)
        posY = self.__genPosY()
        self._attack_distance_x = attack_distance_x
        self._fly_enemy = fly_enemy
        self._random_attack_range = random_attack_range
        self.__decision_attack = lambda: randint(1, random_attack_range)
        self._begin_attack = False
        self.damage_points = damage_points
        self.living_hero = 0
        self.__living_hero = lambda: - self.damage_points
        self.fact_collide = False
        self.height_jump = height_jump
        self.is_jump = False
        self._spriteSheetName = spriteSheetName
        self._state = state
        self.new_position_x = 0
        self.new_position_y = 0
        self.old_spriteSheetName = None
        
        super().__init__(posX, posY, spriteSheetName, state)

    def update(self, heroX, heroY, collide):

        self.heroX, self.heroY = heroX, heroY
        if (self.heroX + self._attack_distance_x <= self._positionX <= self.heroX + self._attack_distance_x + self._speed):
            attack = self.__decision_attack()
            if attack == self._random_attack_range // 2:
                self.widthX = abs(self._positionX - self.heroX)
                self.heightY = abs(self._positionY - self.heroY)
                self._begin_attack = True


        # двигаемся в точку к герою
        if self._begin_attack:
            
            if (not self._fly_enemy) and (not self.is_jump):
                self.new_position_x = self._positionX - self._attack_distance_x * 2
                self.new_position_y = self._positionY

                if self._positionY - self.height_jump < self.heroY:
                    self.point_heroX = self.heroX
                    self.point_heroY = self.heroY
                    self.is_jump = True
                    
                else:
                    self.is_jump = False
                    self._begin_attack = False

            if (self._fly_enemy) or (not self._fly_enemy and self.is_jump):
                if (self._fly_enemy):
                    if self._positionX > self.heroX:
                        self.attack(self.widthX, self.heightY, self.heroX, self.heroY, self._positionX,     self._positionY)
                    else:
                        self._begin_attack = False

                if (not self._fly_enemy):
                    if self._positionX > self.point_heroX:
                        self.attack(self.widthX, self.heightY, self.point_heroX, self.point_heroY, self._positionX, self._positionY)
                    
            if self.is_jump:
                if (self._positionX > self.new_position_x) and (self._positionX < self.point_heroX) and (self._positionY < self.new_position_y):
                    self.attack(self.widthX, self.heightY, self.new_position_x, self.new_position_y, self._positionX, self._positionY)

            if (self._positionX <= self.new_position_x) and (self._positionY <= self.new_position_y):
                self.is_jump = False
                self._begin_attack = False


        if self._begin_attack == False:
            self._positionX -= self._speed
            
        # если достигли края, пересоздаём
        if self._positionX < self._recreation_x:
            self._positionX = self.__genPosX()
            self._positionY = self.__genPosY()

        # передаем данные по collide для подсчета очков. Поскольку враги, в отличие от насекомых не 
        # исчезают, вводим доппроверу, флаг fact._collide, чтобы сопрокосновение срабатывало один 
        # раз и больше не считало очки, пока квадрат врага в квадрате героя
        if collide and self.fact_collide == False:
            self.living_hero = self.__living_hero()
            self.fact_collide = True
        else:
            self.living_hero = 0

        if not collide:
            self.fact_collide = False
        return self.living_hero

    def attack(self, width_x, height_y, heroX, heroY, positionX, positionY):
        self.widthX, self.heightY = width_x, height_y
        self.heroX, self.heroY = heroX, heroY
        self._positionX, self._positionY = positionX, positionY
        if (self.widthX > self.heightY):
            self._positionX -= self._speed * 2
            if self.heroY > self._positionY:
                self._positionY += self._speed * self.heightY /self. widthX * 2
            else:
                 self._positionY -= self._speed * self.heightY /self. widthX * 2
        else:
            self._positionX -= self._speed * self.widthX / self.heightY * 2
            if self.heroY > self._positionY:
                self._positionY += self._speed * 2
            else:
                self._positionY -= self._speed * 2