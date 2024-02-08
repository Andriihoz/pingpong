from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

back = (200,255,255)
window_width = 600
window_height = 500
window = display.set_mode((window_width,window_height))


game = True 
finish = False
clock = time.Clock()
FPS = 60



class GameSprite(sprite.Sprite):
    def __init__(self,image,x,y,player_width,player_height,speed):
        super().__init__()
        self.image = scale(load(image),(player_width,player_height))
        self.speed = speed

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < window_width - 80:
            self.rect.x += self.speed


racket1 = Player("C:\Users/andri\OneDrive\Робочий стіл\Logika/racket.png",30,200,4,20,150)
racket2 = Player("C:\Users/andri\OneDrive\Робочий стіл\Logika/racket.png",520,200,4,20,150)

ball = GameSprite("C:\Users/andri\OneDrive\Робочий стіл\Logika/tenis_ball.png",200,200,4,50,50)


font.init()
loser1 = font.render('Player 1 loser',True,(100,0,10))
loser2 = font.render('Player 1 loser',True,(100,0,10))

speed_x = 4
speed_y = 4

while game:
    for event in event.get():
        if event == QUIT:
            game = False

        if finish != True:
            window.fill(back)
            racket1.update()
            racket2.update()
            ball.rect.x += speed_x
            ball.rect.y += speed_y

            if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
                speed_x *= -1
                speed_y *= 1


            if ball.rect.y > window_height-50 or ball.rect.y < 0:
                speed_y *= -1

            if ball.rect.x < 0:
                finish = True
                window.blit(loser1,(200,200))
                game_over = True
            
            if ball.rect.x > window_width:
                finish = True
                window.blit(loser2,(200,200))
                game_over = True

            racket1.reset()
            racket2.reset()
            ball.reset()
            

    display.update()
    clock.tick(FPS)   

         