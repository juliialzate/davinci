import pygame
from pygame.locals import *
from info import *

class Puzzle:
    def __init__(self):
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Gioconda") 
        self.screen.fill(white)

        self.coordenadas = [(0, 0), (213, 0), (426, 0), (0, 271), (213, 271), (426, 271), (0, 541), (213, 541), (426, 541)]
        self.posicion_vacia = None

        self.inicio_puzzle()

    def inicio_puzzle(self):
        self.matriz_imagenes = [[None, None, None], [None, None, None], [None, None, None]]
        self.matriz_imagenes[0][0] = pygame.image.load('imagenes/monalisa1.png')
        self.matriz_imagenes[0][1] = pygame.image.load('imagenes/monalisa2.png')
        self.matriz_imagenes[0][2] = pygame.image.load('imagenes/monalisa3.png')
        self.matriz_imagenes[1][0] = pygame.image.load('imagenes/monalisa4.png')
        self.matriz_imagenes[1][1] = pygame.image.load('imagenes/monalisa5.png')
        self.matriz_imagenes[1][2] = pygame.image.load('imagenes/monalisa6.png')
        self.matriz_imagenes[2][0] = pygame.image.load('imagenes/monalisa7.png')
        self.matriz_imagenes[2][1] = pygame.image.load('imagenes/monalisa8.png')
        self.matriz_imagenes[2][2] = pygame.image.load('imagenes/monalisa9.png')


        # Encontrar la posición de la imagen "monalisa9"
        for fila, lista_imagenes in enumerate(self.matriz_imagenes):
            for columna, imagen in enumerate(lista_imagenes):
                if imagen == pygame.image.load('imagenes/monalisa9.png'):
                    self.posicion_vacia = (fila, columna)
                    return  # Salir del bucle una vez que se encuentre la posición

    def dibujar(self):
        for i in range(3):
            for j in range(3):
                imagen = self.matriz_imagenes[i][j]
                if imagen:
                    self.screen.blit(imagen, self.coordenadas[i * 3 + j])

    def move(self, direction):
        if direction == 'right':
            self.right()
        elif direction == 'left':
            self.left()
        elif direction == 'up':
            self.up()
        elif direction == 'down':
            self.down()

        
    def right(self):
        fila_vacia, columna_vacia = self.posicion_vacia
        # Verificar que la columna de la monalisa9 sea mayor a 0
        if columna_vacia > 0:
            # Buscar la posición de la imagen monalisa9
            for fila in range(3):
                for columna in range(3):
                    if self.matriz_imagenes[fila][columna] == pygame.image.load('imagenes/monalisa9.png'):
                        # Intercambiar la posición de monalisa9 y la imagen a su izquierda
                        self.matriz_imagenes[fila][columna], self.matriz_imagenes[fila][columna - 1] = \
                            self.matriz_imagenes[fila][columna - 1], self.matriz_imagenes[fila][columna]
                        # Actualizar la posición vacía
                        self.posicion_vacia = (fila, columna)
                        # Actualizar el dibujo de las imágenes
                        self.dibujar()
                        pygame.display.update()
                        return  # Salir del bucle una vez que se haya realizado el intercambio


    def left(self):
        fila_vacia, columna_vacia = self.posicion_vacia
        # Verificar que la columna de la monalisa9 sea menor a 2
        if columna_vacia < 2:
            # Buscar la posición de la imagen monalisa9
            for fila in range(3):
                for columna in range(3):
                    if self.matriz_imagenes[fila][columna] == pygame.image.load('imagenes/monalisa9.png'):
                        # Intercambiar la posición de monalisa9 y la imagen a su derecha
                        self.matriz_imagenes[fila][columna], self.matriz_imagenes[fila][columna + 1] = \
                            self.matriz_imagenes[fila][columna + 1], self.matriz_imagenes[fila][columna]
                        # Actualizar la posición vacía
                        self.posicion_vacia = (fila, columna)
                        # Actualizar el dibujo de las imágenes
                        self.dibujar()
                        pygame.display.update()
                        return  # Salir del bucle una vez que se haya realizado el intercambio


    def up(self):
        fila_vacia, columna_vacia = self.posicion_vacia
        # Verificar que la fila de la monalisa9 sea menor a 2
        if fila_vacia < 2:
            # Buscar la posición de la imagen monalisa9
            for fila in range(3):
                for columna in range(3):
                    if self.matriz_imagenes[fila][columna] == pygame.image.load('imagenes/monalisa9.png'):
                        # Intercambiar la posición de monalisa9 y la imagen abajo de ella
                        self.matriz_imagenes[fila][columna], self.matriz_imagenes[fila + 1][columna] = \
                            self.matriz_imagenes[fila + 1][columna], self.matriz_imagenes[fila][columna]
                        # Actualizar la posición vacía
                        self.posicion_vacia = (fila, columna)
                        # Actualizar el dibujo de las imágenes
                        self.dibujar()
                        pygame.display.update()
                        return  # Salir del bucle una vez que se haya realizado el intercambio


    def down(self):
        fila_vacia, columna_vacia = self.posicion_vacia
        # Verificar que la fila de la monalisa9 sea mayor a 0
        if fila_vacia > 0:
            # Buscar la posición de la imagen monalisa9
            for fila in range(3):
                for columna in range(3):
                    if self.matriz_imagenes[fila][columna] == pygame.image.load('imagenes/monalisa9.png'):
                        # Intercambiar la posición de monalisa9 y la imagen arriba de ella
                        self.matriz_imagenes[fila][columna], self.matriz_imagenes[fila - 1][columna] = \
                            self.matriz_imagenes[fila - 1][columna], self.matriz_imagenes[fila][columna]
                        # Actualizar la posición vacía
                        self.posicion_vacia = (fila, columna)
                        # Actualizar el dibujo de las imágenes
                        self.dibujar()
                        pygame.display.update()
                        return  # Salir del bucle una vez que se haya realizado el intercambio
