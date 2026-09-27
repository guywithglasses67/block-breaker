import sys
import pygame
import random

pygame.init()

blocks = []

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Window")

clock = pygame.time.Clock()
FPS = 60
BALL_SPEED = 4
number_of_powers_left = 3

#User paddle
paddle_width = 100
paddle_rect = pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT-30, paddle_width, 20)

#ball
ball_size = 20
ball_radius = ball_size // 2
ball_rect = pygame.Rect(WINDOW_WIDTH // 2, paddle_rect.y - 20, ball_size, ball_size)

#make blocks
def make_block(row):
    for i in range(5):
        block_rect = pygame.Rect(180+i*90, 50 + row*50, 70, 35)
        pygame.draw.rect(screen, (100, 100, 100), block_rect, border_radius= 10)
        blocks.append(block_rect)


ball_direction = -1
ball_angle = 0
running = True
number_of_blocks = 20

make_block(1)
make_block(2)
make_block(3)
make_block(4)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 20))

    for block in blocks:
        pygame.draw.rect(screen, (100,100,100), block, border_radius= 10)

    #paddle
    pygame.draw.rect(screen, (255,255,255), paddle_rect, border_radius=10)

    #ball
    color = (255,255,255)
    pygame.draw.rect(screen, color, ball_rect, border_radius = ball_size)

    if ball_rect.y < 0:
        ball_rect.y = 1
        ball_direction = 1

        ball_angle = random.randint(-10, 10)

    elif ball_rect.colliderect(paddle_rect):
        ball_direction = -1
        print(BALL_SPEED)

        ball_angle = random.randint(-10,10)
        ball_angle = ball_angle*-1

    elif ball_rect.x < 0:
        ball_angle = ball_angle * -1

    elif ball_rect.x > WINDOW_WIDTH:
        ball_angle = ball_angle *-1
  
    ball_rect.y += ball_direction * BALL_SPEED

    ball_rect.x += ball_angle

    keys = pygame.key.get_pressed()

    SPEED = 10
    if keys[pygame.K_LEFT] and paddle_rect.x > 0:
        paddle_rect.x -= SPEED
    if keys[pygame.K_RIGHT] and paddle_rect.x < WINDOW_WIDTH - 100:
        paddle_rect.x += SPEED
    if keys[pygame.K_SPACE]:
        ball_rect.x = paddle_rect.x + 50
        ball_rect.y = paddle_rect.y - 50
        ball_direction = -1
        ball_angle = 0

    power = False
    if keys[pygame.K_f]:
        power = True

        

        
    for block in blocks:
        if ball_rect.colliderect(block) :#and blocks[i] == True:
            #blocks[block] = False
            block.x = 1000

            angle = random.choice([random.randint(-10, -3), random.randint(3, 10)])
            if not power:
                ball_angle = angle
                ball_direction = ball_direction *-1
                BALL_SPEED = 4

            number_of_blocks -= 1

            if number_of_blocks == 0:
                make_block(1)
                make_block(2)
                make_block(3)
                make_block(4)

                number_of_blocks = 20


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
