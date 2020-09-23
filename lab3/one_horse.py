import pygame
from pygame.draw import *

def outranging_number_of_ellipses(x0, y0, size):
    color1 = (233, 175, 175)
    color2 = (233, 198, 175)
    color3 = (255, 238, 170)
    color4 = (229, 255, 128)
    color5 = (233, 175, 175)
    color6 = (175, 233, 231)
    color7 = (221, 175, 233)
    ellipse(screen, color1, sn(x0 - 80, y0 - 200, 50, 20, size))
    ellipse(screen, color2, sn(x0 - 85, y0 - 190, 40, 35, size))
    ellipse(screen, color3, sn(x0 - 65, y0 - 185, 40, 25, size))
    ellipse(screen, color1, sn(x0 - 62, y0 - 170, 50, 20, size))
    ellipse(screen, color2, sn(x0 - 90, y0 - 167, 40, 15, size))
    ellipse(screen, color7, sn(x0 - 80, y0 - 155, 50, 20, size))
    ellipse(screen, color4, sn(x0 - 90, y0 - 160, 40, 25, size))
    ellipse(screen, color2, sn(x0 - 55, y0 - 158, 50, 30, size))
    ellipse(screen, color3, sn(x0 - 80, y0 - 150, 50, 30, size))
    ellipse(screen, color1, sn(x0 - 95, y0 - 147, 50, 35, size))
    ellipse(screen, color5, sn(x0 - 60, y0 - 140, 40, 20, size))
    ellipse(screen, color6, sn(x0 - 80, y0 - 130, 60, 30, size))
    ellipse(screen, color6, sn(x0 - 50, y0 - 125, 70, 35, size))
    ellipse(screen, color5, sn(x0 - 95, y0 - 120, 75, 25, size))
    ellipse(screen, color7, sn(x0 - 80, y0 - 115, 70, 30, size))
    ellipse(screen, color6, sn(x0 - 90, y0 - 110, 70, 25, size))
    ellipse(screen, color6, sn(x0 - 70, y0 - 100, 80, 40, size))
    ellipse(screen, color5, sn(x0 - 80, y0 - 95, 80, 40, size))
    ellipse(screen, color7, sn(x0 - 100, y0 - 90, 75, 30, size))
    ellipse(screen, color3, sn(x0 - 70, y0 - 87, 90, 35, size))
    ellipse(screen, color2, sn(x0 - 95, y0 - 82, 95, 25, size))


def tree(size, x0, y0):
    rect(screen, (255, 255, 255), (int(x0 * size), int((y0 - 200) * size), int(40 * size), int(200 * size)))
    ellipse(screen, (0, 128, 0), (int((x0-80) * size), int((y0-280) * size), int(200 * size), int(150 * size)))
    ellipse(screen, (0, 128, 0), (int((x0 - 50) * size), int((y0 - 500) * size), int(150 * size), int(200 * size)))
    ellipse(screen, (0, 128, 0), (int((x0 - 120) * size), int((y0 - 400) * size), int(300 * size), int(175 * size)))
    circle(screen, (255, 204, 170), (int((x0 + 70) * size), int((y0-170) * size)), int(30 * size))
    circle(screen, (255, 204, 170), (int((x0 + -75) * size), int((y0 - 300) * size)), int(30 * size))
    circle(screen, (255, 204, 170), (int((x0 + 120) * size), int((y0 - 300) * size)), int(30 * size))
    circle(screen, (255, 204, 170), (int((x0 + 60) * size), int((y0 - 450) * size)), int(30 * size))


# 'sn' function is for shortening 'int(n*size)' and easily producing 'rectangle' type data
def sn(n1, n2, n3, n4, size):
    return (int(n1*size), int(n2*size), int(n3*size), int(n4*size))


def horse(x0, y0, size):

    # coloring
    white = (255, 255, 255)
    color1 = (233, 175, 175)
    color2 = (233, 198, 175)
    color3 = (255, 238, 170)
    color4 = (229, 255, 128)
    color5 = (233, 175, 175)
    color6 = (175, 233, 231)
    color7 = (221, 175, 233)

    # upper tail
    outranging_number_of_ellipses(x0, y0, size)
    # Lowest part of tail
    ellipse(screen, color4, sn(x0 - 75, y0 - 80, 105, 50, size))
    ellipse(screen, color1, sn(x0 - 60, y0 - 70, 90, 40, size))
    ellipse(screen, color3, sn(x0 - 100, y0 - 60, 86, 35, size))
    ellipse(screen, color6, sn(x0 - 80, y0 - 55, 70, 30, size))
    ellipse(screen, color7, sn(x0 - 90, y0 - 50, 65, 30, size))
    ellipse(screen, color2, sn(x0 - 65, y0 - 47, 70, 25, size))
    ellipse(screen, color5, sn(x0 - 60, y0 - 42, 60, 25, size))
    ellipse(screen, color4, sn(x0 - 50, y0 - 40, 50, 30, size))

    # body
    rect(screen, white, sn(x0, y0 - 200, 20, 200, size))
    ellipse(screen, white, sn(x0 - 50, y0 - 250, 300, 100, size))
    rect(screen, white, sn(x0 + 60, y0 - 220, 20, 200, size))
    rect(screen, white, sn(x0 + 200, y0 - 220, 20, 200, size))
    rect(screen, white, sn(x0 + 140, y0 - 200, 20, 200, size))
    rect(screen, white, sn(x0 + 160, y0 - 350, 80, 150, size))
    ellipse(screen, white, sn(x0 + 130, y0 - 400, 120, 75, size))
    ellipse(screen, white, sn(x0 + 180, y0 - 380, 100, 50, size))

    # head features
    # hairs
    outranging_number_of_ellipses(x0+195, y0 - 190, size)
    # corn
    corn_point1=(int((x0 + 145) * size), int((y0 - 387) * size))
    corn_point2=(int((x0 + 160) * size), int((y0 - 497) * size))
    corn_point3=(int((x0 + 180) * size), int((y0 - 397) * size))
    polygon(screen, color1, [corn_point1, corn_point2, corn_point3])
    #eye
    circle(screen, (229, 128, 255), (int((x0 + 200) * size), int((y0 - 365) * size)), int(15 * size))
    circle(screen, (0, 0, 0), (int((x0 + 202) * size), int((y0 - 365) * size)), int(7 * size))
    ellipse(screen, white, sn(x0 + 187, y0 - 375, 15, 10, size))


pygame.init()

FPS = 30


# Begin drowing
# Picture_size controlls size of the picture. I used 0.5 during the development due to the fact that full-scale picture is higher than my laptop screen
picture_size = 0.5

# screen & background
screen = pygame.display.set_mode((int(794*picture_size), int(1123*picture_size)))
rect(screen, (0, 255, 0), (0, 0, int(794*picture_size), int(1123*picture_size)))
rect(screen, (0, 255, 255), (0, 0, int(794*picture_size), int(512*picture_size)))

# sun
circle(screen, (255, 221, 85), (758//2, int(112*picture_size)), int(150*picture_size))

# features
tree(picture_size, 100, 780)
horse(395, 980, picture_size)


# End drowing


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()