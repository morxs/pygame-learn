#-------------------------------------------------------------------------------
# Name:        first_pygame
# Purpose:     create pong game from scratch
#
# Author:      vincent
#
# Created:     19/12/2013
# Copyright:   (c) vincent 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, sys, random
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHT_GRAY = (168, 168, 168)

SIZE = (600, 400)

BALL_RADIUS = 20
PAD_HEIGHT = 60
GUTTER_WIDTH = 10
HALF_GUTTER_WIDTH = GUTTER_WIDTH/2
PADDLE_VEL = 4
TEXT_Y_POS = 50
LEFT = 0
RIGHT = 1
FPS = 60

paddle1_pos = (SIZE[1] - PAD_HEIGHT) / 2
paddle2_pos = (SIZE[1] - PAD_HEIGHT) / 2
paddle1_vel = 0
paddle2_vel = 0
ball_vel = [0, 0]
ball_pos = [int(SIZE[0]/2), int(SIZE[1]/2)]
player1_score = 0
player2_score = 0

done = False
start_ball = False

# used to manage how fast the screen updates
clock = pygame.time.Clock()

def main():
    global done, pos_left, pos_right, ball_vel, player1_score, player2_score

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("P-Ong")
    pygame.key.set_repeat(10, 10)

    font = pygame.font.Font('freesansbold.ttf', 32)


    #ball_vel = [2, 2]
    spawn_ball(RIGHT)

    while done == False:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
##            elif event.type == pygame.KEYDOWN:
##                keydown(event.key)
##                #print("User pressed a key.")
##            elif event.type == pygame.KEYUP:
##                keydown(event.key)
##                #print("User let go of a key.")
            keys = pygame.key.get_pressed()
            keydown(keys)

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        # ball bouncing here and there
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
        # left and right gutters
        if ball_pos[0] + ball_vel[0] > SIZE[0] - BALL_RADIUS - GUTTER_WIDTH:
            if paddle2_pos + paddle2_vel <= ball_pos[1] and paddle2_pos + paddle2_vel + PAD_HEIGHT >= ball_pos[1]:
                ball_pos[0] = SIZE[0] - BALL_RADIUS - GUTTER_WIDTH
                ball_vel[0] *= -1
                ball_vel[0] += add_more_velocity(ball_vel[0])
                ball_vel[1] += add_more_velocity(ball_vel[1])
            else:
                # spawn ball
                spawn_ball(LEFT)
                # add score to player 2
                player1_score += 1
        if ball_pos[0] + ball_vel[0] < 0 + BALL_RADIUS + GUTTER_WIDTH:
            if paddle1_pos + paddle1_vel <= ball_pos[1] and paddle1_pos + paddle1_vel + PAD_HEIGHT >= ball_pos[1]:
                ball_pos[0] = 0 + BALL_RADIUS + GUTTER_WIDTH
                ball_vel[0] *= -1
                ball_vel[0] += add_more_velocity(ball_vel[0])
                ball_vel[1] += add_more_velocity(ball_vel[1])
            else:
                # spawn ball
                spawn_ball(RIGHT)
                # add score to player 1
                player2_score += 1

        # top and bottom bouncers
        if ball_pos[1] + ball_vel[1] > SIZE[1] - BALL_RADIUS:
            ball_pos[1] = SIZE[1] - BALL_RADIUS
            ball_vel[1] *= -1
            #ball_vel[1] += add_more_velocity(ball_vel[1])

        if ball_pos[1] + ball_vel[1] < 0 + BALL_RADIUS:
            ball_pos[1] = 0 + BALL_RADIUS
            ball_vel[1] *= -1
            #ball_vel[1] += add_more_velocity(ball_vel[1])
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        pygame.draw.line(screen, LIGHT_GRAY, [GUTTER_WIDTH, 0], [GUTTER_WIDTH, SIZE[1]], 1)
        pygame.draw.line(screen, LIGHT_GRAY, [SIZE[0]-GUTTER_WIDTH, 0], [SIZE[0]-GUTTER_WIDTH, SIZE[1]], 1)
        pygame.draw.line(screen, LIGHT_GRAY, [SIZE[0]/2, 0], [SIZE[0]/2, SIZE[1]], 1)

        #baseSurf = screen.copy()

        # print text
        text_p1 = font.render(str(player1_score), True, LIGHT_GRAY)
        text_p2 = font.render(str(player2_score), True, LIGHT_GRAY)
        text_rect_p1 = text_p1.get_rect()
        text_rect_p1.center = (SIZE[0]/4, TEXT_Y_POS)
        text_rect_p2 = text_p1.get_rect()
        text_rect_p2.center = (SIZE[0]/4*3, TEXT_Y_POS)
        screen.blit(text_p1, text_rect_p1)
        screen.blit(text_p2, text_rect_p2)

        # initialize left player
        pygame.draw.line(screen, GREEN, [HALF_GUTTER_WIDTH, paddle1_pos+paddle1_vel], [HALF_GUTTER_WIDTH,PAD_HEIGHT+paddle1_pos+paddle1_vel], GUTTER_WIDTH)

        # initialize right player
        pygame.draw.line(screen, RED, [SIZE[0]-HALF_GUTTER_WIDTH, paddle2_pos+paddle2_vel], [SIZE[0]-HALF_GUTTER_WIDTH, PAD_HEIGHT+paddle2_pos+paddle2_vel], GUTTER_WIDTH)

        ### last time this place is holding logics

        pygame.draw.circle(screen, WHITE, [int(ball_pos[0]), int(ball_pos[1])] , BALL_RADIUS)
        #print(ball_vel)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        #ball_vel[0] += VEL
        #ball_vel[1] += VEL

        # Go ahead and update the screen with what we've drawn.
        #pygame.display.flip()
        pygame.display.update()

        # Limit to 60 frames per second
        clock.tick(FPS)

    # Make sure you release the pygame resources properly by calling quit()
    pygame.quit()
    sys.exit()

def spawn_ball(direction):
	global ball_pos, ball_vel # these are vectors stored as lists

	ball_pos = [SIZE[0] / 2, SIZE[1] / 2]

	if direction == RIGHT:
		ball_vel[0] = random.randint(2,6)
		ball_vel[1] = random.randint(2,4) * -1
	else:
		ball_vel[0] = random.randint(2,6) * -1
		ball_vel[1] = random.randint(2,4) * -1

def reset_game():
    paddle1_pos = (SIZE[1] - PAD_HEIGHT) / 2
    paddle2_pos = (SIZE[1] - PAD_HEIGHT) / 2
    paddle1_vel = 0
    paddle2_vel = 0
    ball_vel = [0, 0]
    ball_pos = [int(SIZE[0]/2), int(SIZE[1]/2)]
    player1_score = 0
    player2_score = 0

def add_more_velocity(vel):
    return vel * (0.1)

def keyup(key):
    pass

def keydown(key):
    global paddle1_vel, paddle2_vel, done
    if key[pygame.K_UP]:
        if paddle2_pos + paddle2_vel > 0:
            paddle2_vel -= PADDLE_VEL
    if key[pygame.K_DOWN]:
        if paddle2_pos + PAD_HEIGHT + paddle2_vel < SIZE[1]:
            paddle2_vel += PADDLE_VEL
    if key[pygame.K_w]:
        if paddle1_pos + paddle1_vel > 0:
            paddle1_vel -= PADDLE_VEL
    if key[pygame.K_s]:
        if paddle1_pos + PAD_HEIGHT + paddle1_vel < SIZE[1]:
            paddle1_vel += PADDLE_VEL
    if key[pygame.K_ESCAPE]:
        done = True

if __name__ == '__main__':
    main()
