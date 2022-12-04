import sys
import time
import pygame_widgets
import pygame
import math
from pygame.locals import*
import json
import random
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import numpy as np

vertex = []
faces = []


def refreshOBJ():
    global vertex
    global faces
    with open("./renderer/cube.obj", "r") as obj:
        line = obj.readlines()
        vertex = []
        faces = []
        for x in range(0, len(line)):
            curline = line[x].split(' ')
            numerator = curline[0]
            if not numerator == '#' and not numerator == 'mtllib' and not numerator == 'vt' and not numerator == 'vn' and not numerator == 's':
                if numerator == 'v':
                    vertex.append((float(curline[1]), float(
                        curline[2]), float(curline[3])))
                elif numerator == 'f':
                    f1, f2, f3 = curline[1].split(
                        '/')[0], curline[2].split('/')[0], curline[3].split('/')[0]
                    faces.append((int(f1), int(f2), int(f3)))


width = 1000
height = 1000
screen_color = (5, 5, 5)
line_color = (255, 255, 255)
cameraX = 0
cameraY = 0
pygame.init()
screen = pygame.display.set_mode((width, height))
slider = Slider(screen, 50, 50, 100, 20, min=2, max=50, step=1)

sliderdegX = Slider(screen, 400, 800, 200, 40, min=0, max=360, step=1)
sliderdegY = Slider(screen, 400, 850, 200, 40, min=0, max=360, step=1)
sliderdegZ = Slider(screen, 400, 900, 200, 40, min=0, max=360, step=1)

output = TextBox(screen, 85, 20, 25, 25, fontSize=20)
fo = TextBox(screen, 40, 1, 100, 25, fontSize=20)

output.disable()
fo.disable()


def drawline(p1, p2, color):
    screenX = width/2
    screenY = height/2
    pygame.draw.line(screen, color, (p1[0]+screenX, p1[1]+screenY),
                     (p2[0]+screenX, p2[1]+screenY))


def vertexProjection(vert, focal):
    x, y, z = vert
    x = (focal * x) / (z + focal) * 30
    y = (focal * y) / (z + focal) * 30
    return (x, y)


def vertexRotation(rx, ry, rz):
    for i in range(0, len(vertex)):
        vert = vertex[i]
        x, y, z = vertex[i][0], vertex[i][1], vertex[i][2]
        r = np.dot(([x, y, z]), ([math.cos(rx), -(math.sin(rx))], [
            math.sin(rx), math.cos(rx)]))
        x, y, z = vertex[i][0], vertex[i][1], vertex[i][2]
        r = np.dot(([x, y, z]), ([math.cos(ry), -(math.sin(ry))], [
            math.sin(ry), math.cos(ry)]))
        x, y, z = vertex[i][0], vertex[i][1], vertex[i][2]
        r = np.dot(([x, y, z]), ([math.cos(rz), -(math.sin(rz))], [
            math.sin(rz), math.cos(rz)]))
        vertex[i] = (r[0], r[1], r[2])


def face_VertexTo3DLine(v1, v2, v3):
    return (vertex[v1], vertex[v2]), (vertex[v2], vertex[v3]), (vertex[v3], vertex[v1])


def main():
    fo.setText('FOCAL')
    f = 11
    prev_degX = 0
    prev_degY = 0
    prev_degZ = 0
    prev_focal = 0
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
        f = int(slider.getValue())
        output.setText(slider.getValue())
        for x in faces:
            lines = face_VertexTo3DLine(
                (x[0] - 1), (x[1] - 1), (x[2] - 1))
            for i in range(0, 3):
                vertX = vertexProjection(lines[i][0], f)
                vertY = vertexProjection(lines[i][1], f)
                drawline(vertX, vertY, (255, 255, 255))
        if not f == prev_focal or not prev_degX == sliderdegX.getValue() or not prev_degY == sliderdegY.getValue() or not prev_degZ == sliderdegZ.getValue():
            prev_focal = f
            prev_degX = sliderdegX.getValue()
            prev_degY = sliderdegY.getValue()
            prev_degZ = sliderdegZ.getValue()
            screen.fill(screen_color)
            refreshOBJ()
            vertexRotation(int(sliderdegX.getValue()), int(
                sliderdegY.getValue()), int(sliderdegZ.getValue()))
        pygame.display.update()
        pygame_widgets.update(events)


main()


# def drawfaces(v1, v2, v3, v4):
#     screenX = width/4
#     screenY = height/4
#     drawfaces((x[0] - 1), (x[1] - 1), (x[2] - 1), (x[3] - 1))
#     # pygame.draw.rect(screen, (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)), [
#     #                  v1+screenX, v2+screenX, v3+screenX, v4+screenX])
