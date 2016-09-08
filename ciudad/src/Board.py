import pygame
import Tile


class Board():

    def __init__(self, board):
        self.board = board
        self.registro = {}
        self.total = 0
        self.ocupados = 0
        self.top10Q = []

    def getBoard(self):
        return self.board

    def loadBoard(self, archivo):
        k = 0
        lonMin = -87.940110  # Se suma
        latMin = 42.023030  # Se resta
        lonDif = 0.020799
        latDif = 0.018925
        for i in range(20):
            for j in range(20):
                    self.getBoard()[i][j] = Tile.Tile(i, j)
                    self.getBoard()[i][j].id = k
                    self.getBoard()[i][j].setLatLon(lonMin + (lonDif * (i)), latMin - (latDif * (j)), lonMin + (lonDif * (i + 1)), latMin - (latDif * (j + 1)))
                    k = k + 1
        #tile = self.getCoordSelectedTile(-87.940010, 42.022030)
        #tile.ocupado = 1
        with open(archivo) as f:
            for line in f:
                atributos = line.split(',')
                #print atributos[3]
                #print atributos[4]
                #print float(atributos[4])
                if atributos[3] != "" and atributos[4] != "":
                    #print atributos[3]
                    #print atributos[4]
                    tile = self.getCoordSelectedTile(float(atributos[4]), float(atributos[3]))
                    if tile is not None:
                        tile.ocupado = 1
                        tile.count = tile.count + 1
                        self.total = self.total + 1
                        if (atributos[2] in self.registro) is False:
                            self.registro[atributos[2]] = 1
                        else:
                            self.registro[atributos[2]] = self.registro[atributos[2]] + 1
                        if (atributos[2] in tile.registro) is False:
                            tile.registro[atributos[2]] = 1
                        else:
                            tile.registro[atributos[2]] = tile.registro[atributos[2]] + 1
        k = 0
        for i in range(20):
            for j in range(20):
                    if self.getBoard()[i][j].ocupado == 1:
                        k = k + 1
        self.ocupados = k

    def caracterizar(self, x, y):
        cat = []
        total = []
        prop = []
        i = -1
        with open('categorias.csv') as f:
            for line in f:
                tokens = line.split(':')
                if tokens[0] == 'Cat':
                    if i != -1:
                        prop.append((cat[i] / (total[i] + 0.0)))
                    i = i + 1
                    cat.append(0)
                    total.append(0)
                else:
                    if (tokens[0] in self.registro) is True:
                        total[i] = total[i] + self.registro[tokens[0]]
                    if (tokens[0] in self.board[x][y].registro) is True:
                        cat[i] = cat[i] + self.board[x][y].registro[tokens[0]]
            prop.append((cat[i] / (total[i] + 0.0)))
            value = sorted(prop)[3]
            for i in range(len(prop)):
                if prop[i] == value:
                    break
            self.board[x][y].setColor(i)

    def pintarCasilla(self, x, y, ventana, cuadro):
        self.board[x][y].setCoord(cuadro)
        s = pygame.Surface((cuadro[2], cuadro[3]), pygame.SRCALPHA)
        alpha = 56 + (self.board[x][y].count / 5)
        red = self.board[x][y].red
        green = self.board[x][y].green
        blue = self.board[x][y].blue
        if alpha > 192:
            alpha = 255
            self.board[x][y].set255Color()
            red = self.board[x][y].red
            green = self.board[x][y].green
            blue = self.board[x][y].blue
            #red = 180
            #green = 50
            #blue = 70
        s.fill((red, green, blue, alpha))
        if self.board[x][y].ocupado != 0:
            ventana.blit(s, (cuadro[0], cuadro[1]))

    def pintarSimilarity(self, x, y, ventana, cuadro):
        self.board[x][y].setCoord(cuadro)
        s = pygame.Surface((cuadro[2], cuadro[3]), pygame.SRCALPHA)
        alpha = 56 + (self.board[x][y].count / 5)
        red = self.board[x][y].red
        green = self.board[x][y].green
        blue = self.board[x][y].blue
        if alpha > 192:
            alpha = 255
            self.board[x][y].set255Color()
            red = self.board[x][y].red
            green = self.board[x][y].green
            blue = self.board[x][y].blue
            #red = 180
            #green = 50
            #blue = 70
        s.fill((red, green, blue, alpha))
        if self.board[x][y].sim != -1:
            ventana.blit(s, (cuadro[0], cuadro[1]))

    def top10Similarity(self):
        query = {}
        comparaciones = {}
        with open('query.csv') as f:
            for line in f:
                items = line.split(':')
                query[items[0]] = int(items[1])
        for i in range(20):
            for j in range(20):
                if self.board[i][j].ocupado == 1:
                    total = 0
                    for registro in query:
                        if (registro in self.board[i][j].registro) is True:
                            total = total + pow((query[registro] - self.board[i][j].registro[registro]), 2)
                        else:
                            total = total + pow(query[registro], 2)
                    comparaciones[self.board[i][j].id] = total
        l = list(comparaciones.items())
        l.sort(key=lambda x: x[1])
        #print ((l[:20]))
        ids = []
        for i in range(20):
            for j in range(20):
                for a in range(20):  # Aqui va que tantos grupos busco
                    if a < len(l):
                        if self.board[i][j].id == l[a][0]:
                            self.board[i][j].sim = l[a][1]
                            ids.append(str(str(self.board[i][j].id) + ":x = " + str(i) + " y = " + str(j)))
        for i in range(len(ids)):
            for j in range(len(ids)):
                ident = ids[j].split(':')
                if int(ident[0]) == l[i][0]:
                    print ((ids[j] + " -- Similaridad: " + str(l[i][1])))
                    break

    def getMouseSelectedTile(self, pos):
        for i in range(20):
            for j in range(20):
                if self.board[i][j].isMouseSelected(pos):
                    return self.board[i][j]
        return None

    def getCoordSelectedTile(self, x, y):
        for i in range(20):
            for j in range(20):
                if self.board[i][j].isSelected(x, y):
                    return self.board[i][j]
        return None