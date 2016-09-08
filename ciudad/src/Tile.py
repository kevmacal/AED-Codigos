

class Tile():

    def __init__(self, x, y):
        self.sim = -1
        self.id = -1
        self.tipo = -1
        self.count = 0
        self.x = x
        self.y = y
        self.red = 75
        self.green = 100
        self.blue = 140
        self.ocupado = 0
        self.cuadro = None
        self.registro = {}

    def setCoord(self, cuadro):
        self.cuadro = cuadro

    def setColor(self, tipo):
        self.tipo = tipo
        if tipo == 0:
            self.red = 160
            self.green = 160
            self.blue = 4
        if tipo == 1:
            self.red = 160
            self.green = 8
            self.blue = 8
        if tipo == 2:
            self.red = 160
            self.green = 16
            self.blue = 160
        if tipo == 3:
            self.red = 4
            self.green = 4
            self.blue = 160

    def set255Color(self):
        if self.tipo == 0:
            self.red = 224
            self.green = 224
            self.blue = 8
        if self.tipo == 1:
            self.red = 224
            self.green = 16
            self.blue = 16
        if self.tipo == 2:
            self.red = 224
            self.green = 32
            self.blue = 224
        if self.tipo == 3:
            self.red = 8
            self.green = 8
            self.blue = 224

    def setLatLon(self, xMin, yMin, xMax, yMax):
        self.xMin = xMin
        self.yMin = yMin
        self.xMax = xMax
        self.yMax = yMax

    def isMouseSelected(self, MousePos):
        if self.cuadro is not None:
            if MousePos[0] > self.cuadro[0] and MousePos[0] < self.cuadro[0] + self.cuadro[2]:
                if MousePos[1] > self.cuadro[1] and MousePos[1] < self.cuadro[1] + self.cuadro[3]:
                    return 1
        return 0

    def isSelected(self, x, y):
        #print str(self.xMin)+":"+str(self.xMax)+":"+str(x)
        #print str(self.yMin)+":"+str(self.yMax)+":"+str(y)
        if x > self.xMin and x < self.xMax:
            if y > self.yMax and y < self.yMin:
                return 1
        return 0