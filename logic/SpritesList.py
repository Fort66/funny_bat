import gif_pygame
from collections import defaultdict # этот словарь лучше обычных, так как создает нужные записи при обращении

class SpritesList(object):
    
    def __init__(self) -> None:
        self.__list = defaultdict(defaultdict) # представим список спрайтов как словарь словарей

    # Этот метод загружает спрайт для конкретного спрайтлиста и помещает под конкретным состоянием.
    # Таким образом спрайтлист cat сможет хранить состояния walking и jumping, между которыми сможет
    # Переключаться
    def loadSprite(self, spriteSheetName: str, state: str, address: str):
        self.__list[spriteSheetName][state] = gif_pygame.load(address)

    # Возвращает конкретный спрайт по названиям спрайтлиста и состояния
    def getSprite(self, spriteSheetName: str, state: str) -> gif_pygame.PygameGIF:
        return self.__list[spriteSheetName][state]
