import pygame
import random
from random import randint

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

score = 0
lives = 3
pygame.display.set_caption("Bounce Game")



#Class for top bricks
class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


#Class for the bouncing ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4,8),randint(-8,8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)


#Platform class
class player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([140, 15])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
pygame.init()


#Booleans
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
font = pygame.font.SysFont("Callibri", 35, True, False)
player = player(280, 470)
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
all_sprites_list = pygame.sprite.Group()
bricks = pygame.sprite.Group()
border = pygame.sprite.Group()


#Positioning Bricks and Color
for i in range(15):
    brick = Brick(YELLOW, 20, 15)
    brick.rect.x = random.randrange(screen_width)
    brick.rect.y = 60
    all_sprites_list.add(brick)
    bricks.add(brick)

for i in range(15):
    brick = Brick(YELLOW, 20, 15)
    brick.rect.x = random.randrange(screen_width)
    brick.rect.y = 80
    all_sprites_list.add(brick)
    bricks.add(brick)

for i in range(15):
    brick = Brick(RED, 20, 15)
    brick.rect.x = random.randrange(screen_width)
    brick.rect.y = 100
    all_sprites_list.add(brick)
    bricks.add(brick)

for i in range(15):
    brick = Brick(RED, 20, 15)
    brick.rect.x = random.randrange(screen_width)
    brick.rect.y = 120
    all_sprites_list.add(brick)
    bricks.add(brick)

for i in range(15):
    brick = Brick(YELLOW, 20, 15)
    brick.rect.x = random.randrange(screen_width)
    brick.rect.y = 140
    all_sprites_list.add(brick)
    bricks.add(brick)

for i in range(15):
    brick = Brick(YELLOW, 20, 15)
    brick.rect.x = random.randrange(screen_width)
    brick.rect.y = 160
    all_sprites_list.add(brick)
    bricks.add(brick)

done = False
clock = pygame.time.Clock()
all_sprites_list.add(player)
all_sprites_list.add(ball)



#Main Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-7, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(7, 0)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(7, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-7, 0)

    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.x > 690:
        player.rect.x = 690
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        
        #Gameover 
        if lives == 0:
            text = font.render("GAME OVER", True, RED)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            done = True

    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, player):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
    brick_collision_list = pygame.sprite.spritecollide(ball,bricks,False)

    #Scoring by destroying bricks
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(bricks)==0:
            text = font.render("YOU WIN!", True, BLUE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)

    screen.fill(BLACK)
    text = font.render("Score:" + str(score), True, WHITE)
    screen.blit(text, (350,0))
    text = font.render("Lives:" + str(lives), True, WHITE)
    screen.blit(text, (50,10))
    all_sprites_list.draw(screen)
    all_sprites_list.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
pygame.quit()
