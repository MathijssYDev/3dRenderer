import sys
import time
import pygame
from pygame.locals import*
import json
verts3d = [(0, 0, 0),
           (1, 0, 0),
           (1, 1, 0),
           (0, 1, 0),
           (0, 0, 0),
           (0, 0, 1),
           (1, 0, 1),
           (1, 1, 1),
           (0, 1, 1),
           (0, 0, 1),
           (1, 0, 1),
           (1, 0, 0),
           (1, 1, 0),
           (1, 1, 1),
           (0, 1, 1),
           (0, 1, 0)
           ]

# faces = [(0, 1, 2, 3),
#          (4, 7, 6, 5),
#          (0, 4, 5, 1),
#          (1, 5, 6, 2),
#          (2, 6, 7, 3),
#          (4, 0, 3, 7)]


width = 800
height = 800
screen_color = (0, 0, 0)
line_color = (255, 255, 255)

focal = 50
cameraX = 0
cameraY = 0


def vertscalculate(i, focal):
    vert = verts3d[i]
    x = (focal * (vert[0]+1)) // ((vert[2]+1) * (vert[2]+1) + 1)
    y = (focal * (vert[1]+1)) // ((vert[2]+1) * (vert[2]+1) + 1)
    # x = abs((((vert[0]+1) - cameraX) * (focal/(vert[2]+1))) + cameraX)
    # y = abs((((vert[1]+1) - cameraY) * (focal/(vert[2]+1))) + cameraY)
    # x = (vert[0]+1)*(focal/(vert[2]+1)) * 4
    # y = (vert[1]+1)*(focal/(vert[2]+1)) * 4
    print((x, y))
    return (x, y)


def main():
    screen = pygame.display.set_mode((width, height))
    screen.fill(screen_color)
    pygame.display.flip()
    prev = 0
    for x in range(0, len(verts3d)):
        if x != 0:
            prev = x - 1
            pygame.draw.line(screen, line_color, vertscalculate(
                x, focal), vertscalculate(prev, focal))
            pygame.display.update()
            print(x)

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
        pygame.display.update()


main()
# verts = [(0, 0),
#          (0, 100),
#          (100, 100),
#          (100, 0),
#          (0, 0),
#          ]
# width = 800
# height = 800
# screen_color = (0, 0, 0)
# line_color = (255, 255, 255)


# def main():
#     screen = pygame.display.set_mode((width, height))
#     screen.fill(screen_color)
#     pygame.display.flip()
#     lenth = len(verts)
#     for x in range(0, lenth):
#         if x != 0:
#             prev = x - 1
#             print(verts[x])
#             print(verts[prev])
#             pygame.draw.line(screen, line_color, verts[x], verts[prev])

#     while True:
#         for events in pygame.event.get():
#             if events.type == QUIT:
#                 sys.exit(0)
#         pygame.display.update()


# main()
