# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
titulo = input("Insertar el titulo: ")

# Define size of windows
height = int(input("Altura:"))
width = int(input("Ancho:"))

size = (width, height)


colorR = int (input("Verde:"))
colorV = int (input("Rojo:"))
colorH = int (input("Azul:"))
colordefondo = (colorR, colorV, colorH)


main2(size, titulo, colordefondo)


