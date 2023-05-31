from logic import SpritesList, Player, Food, NPCFabric

# Загрузка спрайтов в лист спрайтов

sprites = SpritesList()

# Загрузка спрайтов игрока

sprites.loadSprite("Player", "right", "./images/hero/mouse_right.gif")
sprites.loadSprite("Player", "left", "./images/hero/mouse_left.gif")
# sprites.loadSprite("Player", "block", "./images/hero/mouse_block.gif")
sprites.loadSprite("Player", "crying_left", "./images/hero/mouse_crying_left.gif")
sprites.loadSprite("Player", "crying_right", "./images/hero/mouse_crying_right.gif")
sprites.loadSprite("Player", "hunger_right", "./images/hero/mouse_hunger_right.gif")
sprites.loadSprite("Player", "hunger_left", "./images/hero/mouse_hunger_left.gif")
sprites.loadSprite("Player", "injury_right", "./images/hero/mouse_injury_right.gif")
sprites.loadSprite("Player", "injury_left", "./images/hero/mouse_injury_left.gif")


# Создание объекта игрока

SPEED_X = 12 # скорость игрока по X
SPEED_Y = 12 # скорость игрока по Y

player = Player(10, 10, 150, 600) # помещаем игрока по координатам 10, 10

# Загружаем спрайты насекомых
sprites.loadSprite("Dragon", "default", "./images/meals/dragon.gif")
sprites.loadSprite("Mosquito", "default", "./images/meals/mosquito.gif")
sprites.loadSprite("Ladybug", "default", "./images/meals/ladybug.gif")
sprites.loadSprite("Butt2", "default", "./images/meals/_butt2.gif")
sprites.loadSprite("Butt1", "default", "./images/meals/_butt1.gif")

# загружаем спрайты врагов
sprites.loadSprite("Raven", "default", "./images/enemies/_raven.gif")
sprites.loadSprite("Falcon", "default", "./images/enemies/falcon1.gif")
sprites.loadSprite("Bird", "default", "./images/enemies/_bird1.gif")
sprites.loadSprite("Cat", "walking", "./images/enemies/cat.gif")
sprites.loadSprite("Cat", "jumping", "./images/enemies/cat_jump.gif")


# Создаем фабрику для NPC (неигровых персонажей). Этот класс сможет создавать NPC
# И массово контролировать их поведение.

npcs = NPCFabric(sprites)

# Создаем массово стрекоз
npcs.addFood(speed=10,
             chaos_ticks_a=50,
             chaos_ticks_b=250,
             chaos_angle_a=120,
             chaos_angle_b=240,
             chaos_position_x_a=1950,
             chaos_position_x_b=2500,
             chaos_position_y_a=20,
             chaos_position_y_b=700,
             spriteSheetName="Dragon",
             state="default",
             recovery_points = 1,
             recreation_x = -300,
             count=3)

# Москиты
npcs.addFood(speed=7,
             chaos_ticks_a=50,
             chaos_ticks_b=250,
             chaos_angle_a=120,
             chaos_angle_b=240,
             chaos_position_x_a=1950,
             chaos_position_x_b=2500,
             chaos_position_y_a=20,
             chaos_position_y_b=700,
             spriteSheetName="Mosquito",
             state="default",
             recovery_points = 1,
             recreation_x = -300,
             count=4)

# Б. коровки
npcs.addFood(speed=15,
             chaos_ticks_a=50,
             chaos_ticks_b=250,
             chaos_angle_a=120,
             chaos_angle_b=240,
             chaos_position_x_a=1950,
             chaos_position_x_b=2500,
             chaos_position_y_a=20,
             chaos_position_y_b=700,
             spriteSheetName="Ladybug",
             state="default",
             recovery_points = 1,
             recreation_x = -300,
             count=2)

# Бабочки
npcs.addFood(speed=6,
             chaos_ticks_a=50,
             chaos_ticks_b=250,
             chaos_angle_a=120,
             chaos_angle_b=240,
             chaos_position_x_a=1950,
             chaos_position_x_b=2500,
             chaos_position_y_a=20,
             chaos_position_y_b=700,
             spriteSheetName="Butt2",
             state="default",
             recovery_points = 1,
             recreation_x = -300,
             count=3)

# Бабочки
npcs.addFood(speed=4,
             chaos_ticks_a=50,
             chaos_ticks_b=250,
             chaos_angle_a=120,
             chaos_angle_b=240,
             chaos_position_x_a=1950,
             chaos_position_x_b=2500,
             chaos_position_y_a=20,
             chaos_position_y_b=700,
             spriteSheetName="Butt1",
             state="default",
             recovery_points = 1,
             recreation_x = -300,
             count=2)


# Ворон
npcs.addEnemies(speed=8,
             chaos_position_x_a=1950,
             chaos_position_x_b=3000,
             chaos_position_y_a=10,
             chaos_position_y_b=500,
             attack_distance_x=300,
             fly_enemy=True,
             random_attack_range = 5,
             spriteSheetName="Raven",
             state="default",
             damage_points = 10,
             height_jump = 0,
             recreation_x = -300,
             count=2)

npcs.addEnemies(speed=10,
             chaos_position_x_a=1950,
             chaos_position_x_b=3000,
             chaos_position_y_a=10,
             chaos_position_y_b=500,
             attack_distance_x=300,
             fly_enemy=True,
             random_attack_range = 5,
             spriteSheetName="Falcon",
             state="default",
             damage_points = 10,
             height_jump = 0,
             recreation_x = -300,
             count=2)

npcs.addEnemies(speed=10,
             chaos_position_x_a=1950,
             chaos_position_x_b=3000,
             chaos_position_y_a=10,
             chaos_position_y_b=500,
             attack_distance_x=300,
             fly_enemy=True,
             random_attack_range = 5,
             spriteSheetName="Bird",
             state="default",
             damage_points = 10,
             height_jump = 0,
             recreation_x = -300,
             count=2)

npcs.addEnemies(speed=6,
             chaos_position_x_a=1950,
             chaos_position_x_b=3000,
             chaos_position_y_a=650,
             chaos_position_y_b=650,
             attack_distance_x=300,
             fly_enemy=False,
             random_attack_range = 5,
             spriteSheetName="Cat",
             state="walking",
             damage_points = 15,
             height_jump = 300,
             recreation_x = -300,
             count=1)