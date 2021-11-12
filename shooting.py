import pygame
import math
import random
import enemyClass as e
import time
import shutil
import sys

# intitalizing pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 800))

# Title and caption

pygame.display.set_caption("Game")
icon = pygame.image.load("game-controller.png")
pygame.display.set_icon(icon)

# creating the player
player = pygame.image.load("ufo.png")
playerX = 400
playerY = 400
player_speed = 0.15
playerX_change = 0
playerY_change = 0

# creating the gun
playerGun = pygame.image.load("gun.png")
gunX = 300
gunY = 300


# creating the bullet
gun_bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 0
bullet_angle = 0
velocity = 0.35

# creating the enemy
# enemy = []
enemy = pygame.image.load('ghost.png')
enemyX = 0
enemyY = 0
enemy_speed = 0.0dd9
enemyY_change = 0
enemyX_change = 0
enemyAngle = 0


collision = False


def gunMovement(x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - x, mouse_y - y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    gun = pygame.transform.rotate(playerGun, angle)

    screen.blit(gun, (x, y))


def enemyDisplay(x, y):

    rel_x, rel_y = playerX - x, playerY - y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    global enemyAngle
    enemyAngle = angle



    screen.blit(enemy, (x, y))




def getAngle(x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    angle = (180 / math.pi) * math.atan2(mouse_y - y, mouse_x - x)

    global bullet_angle, bulletY_change, bulletX_change

    bullet_angle = -angle


def start(x, y):
    screen.blit(player, (x, y))


def shooting(x, y):
    global bullet_angle

    bullet = pygame.transform.rotate(gun_bullet, bullet_angle)

    screen.blit(bullet, (x, y))


isShooting = False
# game loop
running = True
enemyX = random.randint(10, 790)
enemyY = random.randint(10, 790)
while running:
    screen.fill((41, 38, 38))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:

            # WASD
            if event.key == pygame.K_d:
                playerX_change = player_speed
            if event.key == pygame.K_a:
                playerX_change = -player_speed
            if event.key == pygame.K_s:
                playerY_change = player_speed
            if event.key == pygame.K_w:
                playerY_change = -player_speed

            # ARROW kEYS
            # if event.key == pygame.K_RIGHT:
            #     playerX_change = 0.1
            # if event.key == pygame.K_LEFT:
            #     playerX_change = -0.1
            # if event.key == pygame.K_DOWN:
            #     playerY_change = 0.1
            # if event.key == pygame.K_UP:
            #     playerY_change = -0.1

        if event.type == pygame.KEYUP:

            # ARROW kEYS
            # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #     playerX_change = 0
            # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #     playerY_change = 0
            # WASD
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                getAngle(playerX, playerY)

                bulletY = playerY
                bulletX = playerX
                isShooting = True
            if event.button == 3:
                isShooting = False


    if not collision:
        enemyDisplay(enemyX, enemyY)
        enemyX_change = math.cos(-math.pi / 180 * enemyAngle) * enemy_speed

        enemyY_change = math.sin(-math.pi / 180 * enemyAngle) * enemy_speed

        enemyX += enemyX_change
        enemyY += enemyY_change


    if isShooting:
        shooting(bulletX, bulletY)

        bulletX_change = math.cos(-math.pi / 180 * bullet_angle) * velocity

        bulletY_change = math.sin(-math.pi / 180 * bullet_angle) * velocity

        bulletX += bulletX_change
        bulletY += bulletY_change

    if not isShooting:
        bulletY_change = 0
        bulletX_change = 0

    playerX += playerX_change
    playerY += playerY_change
    start(playerX, playerY)

    gunMovement(playerX, playerY)
    pygame.display.update()

pygame.quit()