import pygame
import sys

pygame.init()

# WINDO SETUP
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pendulum simulation")

run = True


class Physics():
    def __init__(self, gravity, forcex, forcey):
        self.gravity = gravity
        self.Tstring = -gravity
        self.forcex = forcex
        self.forcey = forcey

    def ApplyPhysics(self):
        totalforcey = self.gravity + self.Tstring + forcey

        if BOOB.x >= 500 and BOOB.x >= 200:
            print("mama")
            self.forcex = -self.forcex
            BOOB.x += self.forcex
            LINE.endposx += self.forcex
        elif BOOB.x <= 300 and BOOB.x <= 500:
            print("joe")
            self.forcex = -self.forcex
            BOOB.x += self.forcex
            LINE.endposx += self.forcex
        else:
            BOOB.y += totalforcey
            BOOB.x += self.forcex
            LINE.endposx += self.forcex
            LINE.endposy += totalforcey


class bob():
    def __init__(self, radius, mass, colour):
        self.x = 400
        self.y = 300
        self.radius = radius
        self.mass = mass
        self.colour = colour

    def DrawBoB(self):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)


class string():
    def __init__(self, colour):
        self.startposx = 400
        self.startposy = 0
        self.endposx = 400
        self.endposy = 300
        self.colour = colour

    def DrawString(self):
        pygame.draw.line(win, self.colour, (self.startposx, self.startposy), (self.endposx, self.endposy))


# INITIALISE DA FUNCTION
forcex = 0.1
forcey = 0
BOOB = bob(30, 10, (255, 255, 255))
LINE = string((255, 255, 255))
PHYSIKZ = Physics(0.98, forcex, forcey)


def main():
    while run:
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        PHYSIKZ.ApplyPhysics()
        BOOB.DrawBoB()
        LINE.DrawString()

        pygame.display.update()


main()

# BOB DAA BUILDER
