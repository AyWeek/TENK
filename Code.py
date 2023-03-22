import pygame as pg, os, math

pg.init()
width = 1024
height = 1024
screen = pg.display.set_mode((width,height))


absolute = os.path.dirname(__file__)
print(absolute)
os.chdir(absolute)
playerPath = "Sprites/Player"
aiPath = "Sprites/AI"
generalPath = "Sprites/General"
playerFolder = os.path.join(absolute, playerPath)
os.chdir(playerFolder)
playerBody = pg.image.load('body.png')
playerTower = pg.image.load('tower.png')


class player(object):
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.w = playerTower.get_width()
        self.h = playerTower.get_height()
        self.rotSpeed = 0.5
        self.tower = 0.5
        self.vel = 0.5


    def drawBody(self, angle):
        self.angle = angle
        rotate = pg.transform.rotate(playerBody, angle)
        screen.blit(rotate, (self.x - int(rotate.get_width()/2), self.y - int(rotate.get_width()/2)))

    def drawTower(self, angle):
        self.angle = angle
        rotate = pg.transform.rotate(playerTower, angle)
        screen.blit(rotate, (self.x - int(rotate.get_width()/2), self.y - int(rotate.get_height()/2)))

def borders():
    if tank.x + (tank.w/2) >= width:
        tank.x = width - (tank.w/2)
    if tank.x - (tank.w/2) <= 0:
        tank.x = 0 + (tank.w/2)
    if tank.y + (tank.h/2) >= height:
        tank.y = height - (tank.h/2) 
    if tank.y - (tank.h/2) <= 0:
        tank.y = 0  + (tank.h/2) 
    
    

def redrawGameScreen():
    screen.fill((255,255,255))
    tank.drawBody(pAngle)
    screen.blit(rotated_image, rect)
    pg.display.update()

def rotate(surface, angle, pivot, offset):
    rotated_image = pg.transform.rotozoom(surface, -angle, 1)
    rotated_offset = offset.rotate(angle)
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect

mainLoop = True
pAngle = 0
tAngle = 0
tank = player(width/2,height/2)
offset = pg.math.Vector2(0,-7)


while mainLoop:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainLoop = False

    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
        pAngle += tank.rotSpeed
        pAngle %= 360
        tAngle -= tank.rotSpeed
        tAngle %= 360
    if keys[pg.K_d]:
        pAngle -= tank.rotSpeed
        pAngle %= 360
        tAngle += tank.rotSpeed
        tAngle %= 360        
    if keys[pg.K_w]:
        tank.x -= (math.sin(math.radians(pAngle)) * tank.vel)
        tank.y -= (math.cos(math.radians(pAngle)) * tank.vel)
    if keys[pg.K_s]:
        tank.x += (math.sin(math.radians(pAngle)) * tank.vel)
        tank.y += (math.cos(math.radians(pAngle)) * tank.vel)
    if keys[pg.K_LEFT]:
        tAngle += tank.tower
        tAngle %= 360
    if keys[pg.K_RIGHT]:
        tAngle -= tank.tower
        tAngle %= 360
    pivot = [tank.x, tank.y]  
    rotated_image, rect = rotate(playerTower, tAngle, pivot, offset)

    
    
    
    
    
    
    borders()
    redrawGameScreen()

pg.quit()