import pygame
from . import Food, Enemies, SpritesList, Player
# from config import win #для отладки положения и размеров квадратов 
from config import start_living_hero, current_living, win_width, win_height, orientation

# Этот класс фабрику неигровых персонажей

class NPCFabric(object):
    def __init__(self, spriteList: SpritesList) -> None:
        self._food = list() # список еды
        self._enemies = list() # список врагов
        self._sprites = spriteList # список спрайтов для отрисовки
        self.points_game = start_living_hero
        self.current_living = current_living
        self.orientation = orientation
    # заполняет список еды едой с конкретными параметрами
    def addFood(self, 
                 speed: float, 
                 chaos_ticks_a: int, chaos_ticks_b: int,
                 chaos_angle_a: int, chaos_angle_b: int,
                 chaos_position_x_a: int, chaos_position_x_b: int,
                 chaos_position_y_a: int, chaos_position_y_b: int,
                 recovery_points: int, recreation_x: int, 
                 spriteSheetName: str, state: str, count: int):
        for _ in range(count):
            self._food.append(Food(
                speed, 
                chaos_ticks_a, chaos_ticks_b, 
                chaos_angle_a, chaos_angle_b,
                chaos_position_x_a, chaos_position_x_b,
                chaos_position_y_a, chaos_position_y_b,
                recovery_points, recreation_x,
                spriteSheetName, state))

    # список врагов врагами с конкретными параметрами
    def addEnemies(self,
                 speed: float, 
                 chaos_position_x_a: int, chaos_position_x_b: int,
                 chaos_position_y_a: int, chaos_position_y_b: int,
                 attack_distance_x: int, fly_enemy: bool,
                 random_attack_range: int,
                 damage_points: int, height_jump: int, recreation_x: int, 
                 spriteSheetName: str, state: str, count: int):
        for _ in range(count):
            self._enemies.append(Enemies(
                speed, 
                chaos_position_x_a, chaos_position_x_b,
                chaos_position_y_a, chaos_position_y_b,
                attack_distance_x, fly_enemy, random_attack_range,
                damage_points, height_jump, recreation_x,
                spriteSheetName, state))

    # массовая функция обновления положения персонажей неигровых. Для еды и врагов передаются
    # результаты проверки столкновения с игроком.
    def update(self, player: Player):

        # игрок
        player_rect = self.defining_rectangle(player)
        self.inflate_rectangle(player, player_rect, 2, 2)
        
        player_rect[0] =  self.position_rectX(player, player.getPositionX(), 4)
        player_rect[1] = self.position_rectY(player, player.getPositionY(), 4)
        player.setState(self.player_state(self.points_game, self.orientation))

        #для отладки размеров и положения квадратов
        # pygame.draw.rect(win, (0, 0, 255), player_rect, 2)   

        #еда
        for food in self._food:
            food_rect = self.defining_rectangle(food)
            food_rect[0] += food.getPositionX()
            food_rect[1] += food.getPositionY()

            #для квадратов
            # pygame.draw.rect(win, (0, 0, 255), food_rect, 2)  
            
            collide = food.update(player_rect.colliderect(food_rect))
            if collide != 0:
                self.points_game += collide


        #враги
        for enemies in self._enemies:
            enemies_rect = self.defining_rectangle(enemies)
            self.inflate_rectangle(enemies, enemies_rect, 2, 2)
                
            if not enemies._fly_enemy:
                enemies_rect.move_ip((- enemies_rect.x, enemies_rect.y))

                if enemies.is_jump:
                    enemies.setState("jumping")
                    enemies_rect.move_ip((enemies_rect.x, - enemies_rect.y))
                else:
                    enemies.setState("walking")

            enemies_rect[0] += enemies.getPositionX()
            enemies_rect[1] += enemies.getPositionY()

            #для отладки квадратов
            # pygame.draw.rect(win, (0, 0, 255), enemies_rect, 2)  
            
            collide = enemies.update(player.getPositionX(), player.getPositionY(), player_rect.colliderect(enemies_rect))
            
            if collide != 0:
                self.points_game += collide
            
    # массовая отрисовка
    def draw(self, context):
        for food in self._food:
            self._sprites.getSprite(*food.getSprite()).render(context, food.getPosition())
        for enemies in self._enemies:
            self._sprites.getSprite(*enemies.getSprite()).render(context, enemies.getPosition())


        # считаем очки
        self.scoring_points(context)





    def defining_rectangle(self, objects):
        return self._sprites.getSprite(*objects.getSprite()).get_rect()

    def inflate_rectangle(self, objects, objects_rect, decrease_width: int, decrease_height: int):
        pygame.Rect.inflate_ip(objects_rect, - self._sprites.getSprite(*objects.getSprite()).get_width() // decrease_width, - self._sprites.getSprite(*objects.getSprite()).get_height() // decrease_height)

    def position_rectX(self, objects, objects_position_x: int, decreasX: int):
        return objects_position_x + self._sprites.getSprite(*objects.getSprite()).get_width() // decreasX

    def position_rectY(self, objects, objects_position_y: int, decreasY: int):
        return objects_position_y + self._sprites.getSprite(*objects.getSprite()).get_height() // decreasY

    def scoring_points(self, context):
        
        if self.points_game >= start_living_hero:
            self.points_game = start_living_hero

        if self.points_game <= 0:
            self.points_game = 0

        current_living = self.points_game

        
        living_hero_label = pygame.font.Font('./fonts/Roboto/Roboto-Black.ttf', 30)
        view_label = living_hero_label.render(
            'Уровень жизни: ' + str(self.points_game), True, (255, 255, 255))
        context.blit(view_label, (win_width - win_width + 10, win_height - 50))

    def player_state(self, current_living, orientation):
        self.current_living = current_living
        self.orientation = orientation

        if 75 < self.current_living <= 100:
            if self.orientation == "L":
                return "left"
            else:
                return "right"

        if 50 < self.current_living <= 75:
            if self.orientation == "L":
                return "crying_left"
            else:
                return "crying_right"

        if 0 <= self.current_living <= 50:
            if self.orientation == "L":
                return "hunger_left"
            else:
                return "hunger_right"
            