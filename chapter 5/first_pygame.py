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

import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHT_GRAY = (168, 168, 168)

SIZE = (600, 400)

BALL_RADIUS = 20
GUTTER_LENGTH = 60
GUTTER_WIDTH = 10
HALF_GUTTER_WIDTH = GUTTER_WIDTH/2
GUTTER_VEL = 2

done = False

# used to manage how fast the screen updates
clock = pygame.time.Clock()

def main():
    global done

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("P-Ong")

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                print("User pressed a key.")
            elif event.type == pygame.KEYUP:
                print("User let go of a key.")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("User pressed a mouse button")

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        pos_left = 120
        pos_right = 60
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # initialize left player
        pygame.draw.line(screen, GREEN, [HALF_GUTTER_WIDTH,0+pos_left], [HALF_GUTTER_WIDTH,GUTTER_LENGTH+pos_left], GUTTER_WIDTH)

        # initialize right player
        pygame.draw.line(screen, RED, [SIZE[0]-HALF_GUTTER_WIDTH, 0+pos_right], [SIZE[0]-HALF_GUTTER_WIDTH, GUTTER_LENGTH+pos_right], GUTTER_WIDTH)

        pygame.draw.line(screen, LIGHT_GRAY, [GUTTER_WIDTH, 0], [GUTTER_WIDTH, SIZE[1]], 1)
        pygame.draw.line(screen, LIGHT_GRAY, [SIZE[0]-GUTTER_WIDTH, 0], [SIZE[0]-GUTTER_WIDTH, SIZE[1]], 1)

        pygame.draw.circle(screen, WHITE, [int(SIZE[0]/2), int(SIZE[1]/2)], BALL_RADIUS)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Make sure you release the pygame resources properly by calling quit()
    pygame.quit()

if __name__ == '__main__':
    main()
