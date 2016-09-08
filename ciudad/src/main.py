#!/usr/bin/env python
import pygame
import sys
import Board


def main():
    #Initialize variables
    pygame.init()
    fps = pygame.time.Clock()
    #globalTile = None
    tipo = 1
    bg = pygame.image.load("../images/ciudad.png")
    #Variables de cuadros
    xIni = 0
    yIni = 0
    xFug = 3
    yFug = 3
    xVar = 445
    yVar = 539
    xMult = ((xVar + xFug) / (20)) - (xFug)
    yMult = ((yVar + yFug) / (20)) - (yFug)
    #print xMult
    #print yMult
    #Tabla de crimen
    board = Board.Board([])
    for i in range(20):
        a = [0] * 20
        board.getBoard().append(a)
    board.loadBoard('data2016.csv')
    print (("Registros totales: " + str(board.total) + "\n"))
    #for registro in board.registro:
        #print ((registro + ":" + str(board.registro[registro])))
    board2 = Board.Board([])
    for i in range(20):
        a = [0] * 20
        board2.getBoard().append(a)
    board2.loadBoard('schools.csv')
    board3 = Board.Board([])
    for i in range(20):
        a = [0] * 20
        board3.getBoard().append(a)
    board3.loadBoard('nl.csv')
    #for registro in board2.registro:
        #print ((registro + ":" + str(board2.registro[registro])))
    #Tama~no de ventana
    ventanaP = pygame.display.set_mode((xVar, yVar))
    pygame.display.set_caption("Mapa Chicago")
    ventanaP.blit(bg, (0, 0))
    while True:
        key = 0
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    ventanaP = pygame.display.set_mode((xVar, yVar))
                    ventanaP.blit(bg, (0, 0))
                    if tipo == 2 and key == 0:
                        board.top10Similarity()
                        for j in range(20):
                            for i in range(20):
                                xIni = xFug + i * xMult
                                yIni = 1 + j * yMult
                                cuadro = (xIni + (xFug * i), yIni + (yFug * j), xMult, yMult)
                                board.pintarSimilarity(i, j, ventanaP, cuadro)
                        pygame.display.update()
                        key = 0
                if evento.key == pygame.K_SPACE:
                    if tipo == 0 and key == 0:
                        ventanaP = pygame.display.set_mode((xVar, yVar))
                        ventanaP.blit(bg, (0, 0))
                        pygame.display.update()
                        tipo = 1
                        key = 1
                    if tipo == 1 and key == 0:
                        ventanaP = pygame.display.set_mode((xVar, yVar))
                        ventanaP.blit(bg, (0, 0))
                        for j in range(20):
                            # print ((xIni + xFug + 40))
                            # iniX,iniY,distX,distY
                            for i in range(20):
                                xIni = xFug + i * xMult
                                yIni = 1 + j * yMult
                                #cuadro = (xIni + (xFug * i), yIni + (yFug * j), xMult, yMult)
                                cuadro = (xIni + (xFug * i), yIni + (yFug * j), xMult, yMult)
                                #s = pygame.Surface((xMult, yMult), pygame.SRCALPHA)
                                #s.fill((70, 100, 140, 180))
                                #ventanaP.blit(s, (cuadro[0], cuadro[1]))
                                #print cuadro[0]
                                #print cuadro[1]
                                #print cuadro[2]
                                #print cuadro[3]
                                if board.board[i][j].ocupado != 0:
                                    board.caracterizar(i, j)  # Comentar para solo mapa calor
                                    board.pintarCasilla(i, j, ventanaP, cuadro)
                                #pygame.draw.rect(ventanaP, pygame.Color(70, 100, 140, 255), cuadro)
                        pygame.display.update()
                        tipo = 2
                        key = 1
                    if tipo == 2 and key == 0:
                        ventanaP = pygame.display.set_mode((xVar, yVar))
                        ventanaP.blit(bg, (0, 0))
                        for j in range(20):
                            for i in range(20):
                                xIni = xFug + i * xMult
                                yIni = 1 + j * yMult
                                cuadro = (xIni + (xFug * i), yIni + (yFug * j), xMult, yMult)
                                board2.pintarCasilla(i, j, ventanaP, cuadro)
                                if board.board[i][j].ocupado != 0 and board2.board[i][j].ocupado != 0:
                                    board.pintarCasilla(i, j, ventanaP, cuadro)
                        pygame.display.update()
                        tipo = 3
                        key = 1
                    if tipo == 3 and key == 0:
                        ventanaP = pygame.display.set_mode((xVar, yVar))
                        ventanaP.blit(bg, (0, 0))
                        for j in range(20):
                            for i in range(20):
                                xIni = xFug + i * xMult
                                yIni = 1 + j * yMult
                                cuadro = (xIni + (xFug * i), yIni + (yFug * j), xMult, yMult)
                                board3.pintarCasilla(i, j, ventanaP, cuadro)
                                if board.board[i][j].ocupado != 0 and board3.board[i][j].ocupado != 0:
                                    board.pintarCasilla(i, j, ventanaP, cuadro)
                        pygame.display.update()
                        tipo = 0
                        key = 1
            if evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if tipo == 2:
                    selTile = board.getMouseSelectedTile(pos)  # get the tile selected by the user
                    #globalTile = selTile
                    if selTile is not None:
                        print (("\n" + (str(selTile.id) + " Total registros: " + str(selTile.count))))
                        #print ((str(selTile.xMin) + ":" + str(selTile.yMin) + ":" + str(selTile.xMax) + ":" + str(selTile.yMax)))
                        for registro in selTile.registro:
                            print ((registro + ":" + str(selTile.registro[registro])))
                if tipo == 0:
                    selTile = board2.getMouseSelectedTile(pos)  # get the tile selected by the user
                    #globalTile = selTile
                    if selTile is not None:
                        print (("\n" + (str(selTile.id) + " Total registros: " + str(selTile.count))))
                        #print ((str(selTile.xMin) + ":" + str(selTile.yMin) + ":" + str(selTile.xMax) + ":" + str(selTile.yMax)))
                        for registro in selTile.registro:
                            print ((registro + ":" + str(selTile.registro[registro])))
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fps.tick(2)

main()