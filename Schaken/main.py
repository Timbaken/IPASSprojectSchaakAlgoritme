import schaakBord

import pygame
import sys
import itertools

pygame.init()

schaakstukAfbeeldingen = {}
schermlengte = schermbreedte = 512
bordvakken = 8
vakgrootte = schermlengte // bordvakken

screen = pygame.display.set_mode((schermbreedte, schermlengte))
pygame.display.set_caption("Schaken")
icon = pygame.image.load('Schaakstukken/ZQ.png')
pygame.display.set_icon(icon)

colors = itertools.cycle((pygame.Color('white'), pygame.Color('light blue')))
pygameBord = pygame.Surface((schermbreedte, schermlengte))
for y in range(0, schermlengte, vakgrootte):
    for x in range(0, schermbreedte, vakgrootte):
        rect = (x, y, vakgrootte, vakgrootte)
        pygame.draw.rect(pygameBord, next(colors), rect)
    next(colors)

def couplePiecesToImages():
    schaakstukAfbeeldingen['ZR'] = pygame.image.load('Schaakstukken/ZR.png')
    schaakstukAfbeeldingen['ZN'] = pygame.image.load('Schaakstukken/ZN.png')
    schaakstukAfbeeldingen['ZB'] = pygame.image.load('Schaakstukken/ZB.png')
    schaakstukAfbeeldingen['ZQ'] = pygame.image.load('Schaakstukken/ZQ.png')
    schaakstukAfbeeldingen['ZK'] = pygame.image.load('Schaakstukken/ZK.png')
    schaakstukAfbeeldingen['ZP'] = pygame.image.load('Schaakstukken/ZP.png')
    schaakstukAfbeeldingen['WR'] = pygame.image.load('Schaakstukken/WR.png')
    schaakstukAfbeeldingen['WN'] = pygame.image.load('Schaakstukken/WN.png')
    schaakstukAfbeeldingen['WB'] = pygame.image.load('Schaakstukken/WB.png')
    schaakstukAfbeeldingen['WQ'] = pygame.image.load('Schaakstukken/WQ.png')
    schaakstukAfbeeldingen['WK'] = pygame.image.load('Schaakstukken/WK.png')
    schaakstukAfbeeldingen['WP'] = pygame.image.load('Schaakstukken/WP.png')


def main():
    couplePiecesToImages()
    bord = schaakBord.SchaakBord()
    print(bord.bord)
    while True:
        screen.blit(pygameBord, (0, 0))
        tekenStukken(bord.bord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


def tekenStukken(bord):
    for row in range(bordvakken):
        for column in range(bordvakken):
            piece = bord[row][column]
            if piece != '  ':
                screen.blit(schaakstukAfbeeldingen[piece], pygame.Rect(column * vakgrootte, row * vakgrootte, vakgrootte, vakgrootte))



if __name__ == "__main__":
    main()