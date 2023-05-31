from . import GameObject
from config import win_width, win_height

# наследуем класс игрок от класса стандартного игрового объекта
class Player(GameObject):
    
    def __init__(self, positionX: float, positionY: float, width_restriction: int, height_rectriction: int) -> None:
        super().__init__(positionX, positionY, "Player", "right")
        self._width_restriction = width_restriction
        self._height_rectriction = height_rectriction
    # движение по сторонам на некоторое расстояние
    def moveX(self, distanceX: float):
        self._positionX += distanceX
        if self._positionX <= 0:
            self._positionX = 0
        if self._positionX >= win_width - self._width_restriction:
            self._positionX = win_width - self._width_restriction

    def moveY(self, distanceY: float):
        self._positionY += distanceY
        if self._positionY <= 0:
            self._positionY = 0
        if self._positionY >= self._height_rectriction:
            self._positionY = self._height_rectriction