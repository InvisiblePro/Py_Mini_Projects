import sys
import pygame
import random


from pygame import time

pygame.init()

clock = pygame.time.Clock()

print("Press Q/q for quit/end the game")
time.wait(3000)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong game")

ball = pygame.Rect(screen_width / 2 - 8.5, screen_height / 2 - 8.5, 17, 17)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 100)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 100)
bg_color = pygame.Color("grey20")
light_grey = pygame.Color(200, 200, 200)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 10


def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed - 2
        opponent.bottom = opponent.bottom - 5
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom > 600:
        opponent.bottom = 600


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

    screen.fill(bg_color)
    pygame.draw.rect(screen, "royalblue", player)
    pygame.draw.rect(screen, (255, 85, 0), opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),
                       (screen_width / 2, screen_height))

    ball_animation()
    player_animation()
    opponent_animation()

    pygame.display.flip()
    clock.tick(60)
