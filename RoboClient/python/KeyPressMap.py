class KeyPressMap:
    def __init__(self):
        self.__keymap = {}

    def keyDown(self, key):
        self.__keymap[key] = True

    def keyUp(self, key):
        self.__keymap[key] = False

    def isPressed(self, key):
        result = self.__keymap.get(key)
        
        if result == None:
            return False
        else:
            return self.__keymap[key]

    def allUp(self):
        for key in self.__keymap:
            self.__keymap[key] = False

    def printMap(self):
        print(self.__keymap)

KEYS = KeyPressMap()
