from pygame import *
from random import randint
from time import time as timer

font.init()
font1 = font.SysFont('Arial', 40)
win = font1.render("ты победил: ", True,(0,255,0))
lose = font1.render("ты лох: ", True,(255,0,0))
font2 = font.Font(None, 36)

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.sound('fire.ogg')

img_back = 'galaxy.jpg'
img_hero = 'rocket.png'
img_enemy = "ufo.png" 
img_bullet = 'bullet.png'
img_ast = 'asteroid.png'

score = 0
lost = 0
goal =5
max_lost = 3
life = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y,player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_widht - 80:
            self.rect.x +=self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx-22,self.rect.top, -15,45,40)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_widht:
            self.rect.x = randint(80, win_widht - 80)
            self.rect.y = 0
            lost += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

win_widht = 700
win_height = 500
window = display.set_mode((win_widht, win_height))
display.set_caption("spaceshooter")
window = display.set_mode((win_widht, win_height))
background = transform.scale((image.load(img_back)), (win_widht, win_height))

ship = Player(img_hero, 5, win_height - 100,  10, 80, 100)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_widht - 80), -40, randint(1, 5), 80, 50)
    monsters.add(monster)

asteroids = sprite.Group()
for i in range(1, 6):
    asteroids = Enemy(img_ast, randint(30, win_widht - 30), -40, randint(1, 7), 80, 50)
    asteroids.add(asteroid)
bullets = sprite.Group()
game = True
finish = False
clock = time.Clock()
rel_time = False
FPS = 69
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                
            if num_fire > 5 and 
            rel_time == False:
            last_time = timer()
            rel_time = True
            num_fire += 1 
            ship.fire()
        if not finish:
            window.blit(background,(0,0))
            text = font2.render("Счет: " + str(score), 1 ,(255,255,255))
            window.blit(text, (10,20))
            text_lose = font2.render("Пропущено: " + str(lost), 1 ,(255,255,255))
            window.blit(text_lose, (10,50))

            ship.update()
            monsters.update()
            bullets.update()
            ship.reset()
            monsters.draw(window)
            bullets.draw(window)
            asteroids.draw(window)
        
            if rel_time = True 

            collides = sprite.groupcollide(monsters, bullets, True, True)
            for c in collides:
                score += 1
                monster = Enemy(img_enemy, randint(80, win_widht - 80), -40, randint(1, 5), 80, 50)
                monsters.add(monster)

            if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False) :
                sprite.spritecollide(ship, monsters, True)
                sprite.spritecollide(ship, asteroids, True)
                life -= 1
            
            if life == 0 or lost >= max_lost:
                finish = True
                window.blit(lose, (200, 200))
            


        if sprite.spritecollide(ship, monster, False) or lost >= max_lost:
            finish = True
            window.blit(lose,(200,200))
        if score >= goal:
            finish = True
            window.blit(win, (200,200))

        text = font2.render("Счет: " + str(score), 1 ,(255,255,255))
        window.blit(text, (10,20))

        text_lose = font2.render("Пропущено: " + str(lost), 1 ,(255,255,255))
        window.blit(text_lose, (10,50))
        display.update()
    else:
        finish = False
        score = 0
        lost = 0
        num_fire = 0
        for b in bullets:
            b.kill()    
        time.delay(3000)
        for i in range(1, 6):
            monster = Enemy(img_enemy, randint(80, win_widht - 80), -40, randint(1, 5), 80, 50)
            monsters.add(monster) 
    clock.tick(FPS)




        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0, 0)
        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))
        display.update()


            time.delay(1000)
            for i in range(1, 6):
                monster = Enemy(img_enemy, randint(80, win_widht - 80), -40, randint(1, 5), 80, 50)
                monsters.add(monster)
            for i in range(1, 6):
                asteroids = Enemy(img_ast, randint(30, win_widht - 30), -40, randint(1, 7), 80, 50)
                asteroids.add(asteroid)




























































































































































































































































































































































































