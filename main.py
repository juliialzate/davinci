# archivo main.py
import pygame
from info import *
from cuadros import Puzzle

pygame.init()

puzzle = Puzzle()

# Iniciar el juego automáticamente
puzzle.dibujar()
pygame.display.update()

ejecutar = True

while ejecutar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                puzzle.move('up')
            elif event.key == pygame.K_DOWN:
                puzzle.move('down')
            elif event.key == pygame.K_LEFT:
                puzzle.move('left')
            elif event.key == pygame.K_RIGHT:
                puzzle.move('right')

    puzzle.screen.fill(white)  # Limpiar la pantalla
    puzzle.dibujar()           # Volver a dibujar las imágenes
    pygame.display.update()    # Actualizar la pantalla

pygame.quit()