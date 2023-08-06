import sys
import pygame
from pygame.locals import *
import random
import time

print('\n\tWelCome to Dou Pong Game by DarBar Bros')
print('\n\t\tPlayer Blue: Up and Down keys')
print('\t\tPlayer Orange: Z and X keys')
print("\n\nPress Q/q for Quit")

pygame.init()

time.sleep(5)
clock = pygame.time.Clock()

score1 = 0
score2 = 0
player_speed = 0

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong game")

ball = pygame.Rect(screen_width / 2 - 8.5, screen_height / 2 - 8.5, 17, 17)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 100)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 100)
bg_color = pygame.Color("grey20")
light_grey = pygame.Color(200, 200, 200)
ball_speed_x = 8 * random.choice((1, -1))
ball_speed_y = 8 * random.choice((1, -1))

opponent_speed = 0


def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_restart()
        score1 + 1
    if ball.right >= screen_width:
        ball_restart()
        score2 + 1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\n\tThank You!! :-)")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("\n\tThank You!! :-)")
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                opponent_speed += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                opponent_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                opponent_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                opponent_speed += 7

    screen.fill(bg_color)
    pygame.draw.rect(screen, ("royalblue"), player)
    pygame.draw.rect(screen, (255, 85, 0), opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),
                       (screen_width / 2, screen_height))

    ball_animation()
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    pygame.display.flip()
    clock.tick(60)
