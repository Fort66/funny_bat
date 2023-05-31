class GameObject(object):
    def __init__(self, positionX: float, positionY: float, spriteSheetName: str, state: str) -> None:
        self._positionX = positionX
        self._positionY = positionY
        self._spriteSheetName = spriteSheetName
        self._state = state
    
    def getPosition(self) -> tuple:
        return (round(self._positionX), round(self._positionY))
    
    def getPositionX(self) -> int:
        return round(self._positionX)
    
    def getPositionY(self) -> int:
        return round(self._positionY)
    
    def setPositionX(self, newPositionX: float):
        self._positionX = newPositionX

    def setPositionY(self, newPositionY: float):
        self._positionY = newPositionY

    def setPosition(self, newPositionX, newPositionY):
        self._positionX, self._positionY = newPositionX, newPositionY

    def setState(self, newState: str):
        self._state = newState

    def getState(self):
        return self._state

    def getSprite(self) -> tuple:
        return self._spriteSheetName, self._state
