import pygame
import math
import random
import time
import enemyClass as e
import sys
import asyncio

# intitalizing pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 800))

# Adding text Intitalization
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# Title and caption

pygame.display.set_caption("Game")
icon = pygame.image.load("game-controller.png")
pygame.display.set_icon(icon)

# creating the player
player = pygame.image.load("ufo.png")
playerX = 400
playerY = 400
player_speed = 1.5
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
velocity = 8

# creating the enemy

enemy = pygame.image.load('ghost.png')

enemy_speed = 1.5


enemies = [e.Enemy(random.randint(10, 790), random.randint(10, 790), 0, enemy),
           e.Enemy(random.randint(10, 790), random.randint(10, 790), 0, enemy)]

score = 0

killsToWin = 10


def gunMovement(x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - x, mouse_y - y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    gun = pygame.transform.rotate(playerGun, angle)

    screen.blit(gun, (x, y))


def enemyDisplay(x, y, enemyPic):
    rel_x, rel_y = playerX - x, playerY - y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    screen.blit(enemyPic, (x, y))
    return angle


def collisionDetection(Px, Py, Ex, Ey):
    distance = math.sqrt((Px - Ex) ** 2 + (Py - Ey) ** 2)
    if distance < 30:
        return True
    else:
        return False


def getAngle(x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    angle = (180 / math.pi) * math.atan2(mouse_y - y, mouse_x - x)

    global bullet_angle, bulletY_change, bulletX_change

    bullet_angle = -angle


def start(x, y):
    screen.blit(player, (x, y))
    text = "KillS: {}".format(score)

    # if score == killsToWin:
    #     text = "YOU WIN"

    textsurface = myfont.render(text, False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))

    if score == killsToWin * 10:
        screen.blit(myfont.render("YOU WIN", False, (0, 0, 0)), (0, 0))
        endGame()


def endGame():
    global running
    running = False


def shooting(x, y):
    global bullet_angle

    bullet = pygame.transform.rotate(gun_bullet, bullet_angle)

    screen.blit(bullet, (x, y))


isShooting = False
# game loop
running = True

async def main():
    global running, bulletX, bulletX_change, bulletY, bulletX_change, isShooting, playerX, playerX_change, playerY, playerY_change, score

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

        for e in enemies:
            collision = collisionDetection(bulletX, bulletY, e.xCoor, e.yCoor)

            if not collision:
                enemyAngle = enemyDisplay(e.xCoor, e.yCoor, e.image)
                e.setAngle(enemyAngle)
                enemyX_change = math.cos(-math.pi / 180 * e.angle) * enemy_speed

                enemyY_change = math.sin(-math.pi / 180 * e.angle) * enemy_speed

                e.changeX(enemyX_change)
                e.changeY(enemyY_change)


            else:
                e.setX(random.randint(10, 790))
                e.setY(random.randint(10, 790))

                score += 1

            if isShooting:
                shooting(bulletX, bulletY)

                bulletX_change = math.cos(-math.pi / 180 * bullet_angle) * velocity

                bulletY_change = math.sin(-math.pi / 180 * bullet_angle) * velocity

                bulletX += bulletX_change
                bulletY += bulletY_change

            playerX += playerX_change
            playerY += playerY_change

            start(playerX, playerY)

            if collisionDetection(playerX, playerY, e.xCoor, e.yCoor):
                textsurface = myfont.render("YOU LOSE", False, (0, 0, 0))
                screen.blit(textsurface, (100, 100))
                endGame()

        gunMovement(playerX, playerY)

        pygame.display.update()
        await asyncio.sleep(0)


asyncio.run(main())

