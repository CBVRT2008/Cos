import pygame
import time

screen = ""

def startup():
    global screen, logo, clock
    pygame.init()
    width_screen = 500
    height_screen = 500
    screen = pygame.display.set_mode([width_screen, height_screen])
    logo = pygame.image.load("Images/logo1.png")
    Clock = pygame.time.Clock()

def run(running):
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 252))

        if True:
            Logo(100, 134.5)

        pygame.display.flip()

        Clock.tick(60)


    pygame.quit()


def Logo(x,y):
    screen.blit(logo, (x,y))