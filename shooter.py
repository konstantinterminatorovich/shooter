from pygame import *
import time as t
from random import randint
window = display.set_mode((1000, 700))
display.set_caption('Shooter')
clock = time.Clock()
galaxy = transform.scale(image.load('D:\python_fotos\galaxy.jpg'),(1000, 700))

mixer.init()
'''mixer.music.load('D:\python_fotos\space.ogg')
mixer.music.play()'''
fire_sound = mixer.Sound('D:\python_fotos\\fire.ogg')
font.init()
font1= font.SysFont('Arial', 36, bold=1)

class GameSprite(sprite.Sprite):
    def __init__(self, img, width, height, player_x, player_y, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): #вывести на экран
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > self.speed:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < (930 - self.speed):
            self.rect.x += self.speed
    def fire(self):
        bullet=Bullet('D:\python_fotos\\bullet.png', 10,  25, (self.rect.x + 30), 470, 3)
        bullets.add(bullet)


class Bullet(GameSprite):
    def update(self):
        self.rect.y -=self.speed
        if self.rect.y <-self.height:
            self.kill()

bullets = sprite.Group()
lost=0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 600:
            lost = lost + 1
            self.rect.y = randint(-200, - 80)
            self.rect.x = randint(0, 800)

class Meteorite(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 600:
            lost = lost + 1
            self.rect.y = randint(-200, - 80)
            self.rect.x = randint(0, 800)

meteorites = sprite.Group()

win =  transform.scale(image.load('D:\python_fotos\winwin.jpg'),(1000, 700))
lose = transform.scale(image.load('D:\python_fotos\youlose.jpg'),(1000, 700))

we_win=True
player = GameSprite("D:\python_fotos\\rocket.png", 80, 100, 0, 570, 10)
enemies = sprite.Group()
for i in range(5):
    enemy = Enemy('D:\\python_fotos\\ufo.png', 100 , 60 , randint( 0, 800), -50, randint(2, 4))
    enemies.add(enemy)

for i in range(5):
    meteorite = Meteorite('D:\\python_fotos\meteorite2.png', 100 , 60 , randint( 0, 800), -50, randint(2, 4))
    meteorites.add(meteorite)
monsters_killed=0
finish = False
run = True
health=3
num_fire=5
reloadfire=False
time_of_reload=120
wait=600
while run:
    window.blit(galaxy, (0,0))
    if wait>=0:
        text_rules=font1.render('Задача отразить атаку инопланетян.', 1, (0, 0, 255))
        window.blit(text_rules, (20, 0))
        text_rules2=font1.render('Правила проигрыша:' ,1, (255, 0, 0))
        window.blit(text_rules2, (20, 30))
        text_rules3=font1.render('1) 3 столкновения с НЛО;' ,1, (255, 255, 255))
        window.blit(text_rules3, (20, 60))
        text_rules4=font1.render('2) 1 столкновение с астероидом;', 1, (255, 255, 255))
        window.blit(text_rules4, (20, 90))
        text_rules5=font1.render('3) 8 пропущеных НЛО.', 1, (255, 255, 255))
        window.blit(text_rules5, (20, 120))
        text_rules6=font1.render('Правила выиграша:', 1, (0, 255, 0))
        window.blit(text_rules6, (20, 150))
        text_rules7=font1.render('убить 10 НЛО.', 1, (255, 255, 255))
        window.blit(text_rules7, (20, 180))
        text_rules8=font1.render('Правило игры:', 1, (255, 255, 0))
        window.blit(text_rules8, (20, 210))
        text_rules9=font1.render('корабль дивгаеться вправо,', 1, (255, 255, 255))
        window.blit(text_rules9, (20, 240))
        text_rules10=font1.render('влево и управлеяеться,', 1, (255, 255, 255))
        window.blit(text_rules10, (20, 270))
        text_rules12=font1.render('стрелочками вправо, влево;', 1, (255, 255, 255))
        window.blit(text_rules12, (20, 300)) 
        text_rules13=font1.render('чтобы выстрелить надо', 1, (255, 255, 255))
        window.blit(text_rules13, (20, 330))
        text_rules14=font1.render('нажать на Пробел', 1, (255, 255, 255))
        window.blit(text_rules14, (20, 350))
        text_rules15=font1.render('каждыe 5 выстрелов производиться', 1, (255, 255, 255))
        window.blit(text_rules15, (20, 380))
        text_rules17=font1.render('3 секудная перезарядка.', 1, (255, 255, 255))
        window.blit(text_rules17, (20, 410))
        text_rules18=font1.render('Удачи!!!', 1, (255, 255, 255))
        window.blit(text_rules18, (20, 440))
        wait-=1
    else:
        text_killed = font1.render('Убито:'+str(monsters_killed), 1, (255, 0, 0))
        text_lose = font1.render('Пропущено:'+str(lost), 1, (255, 0, 255))
        text_health = font1.render('Здоровье:'+str(health)+'/3', 1, (0, 255, 0))
        text_num_fire = font1.render('Патроны:'+str(num_fire)+'/5', 1, (255, 75, 0))
        window.blit(text_health, (20, 100))
        window.blit(text_lose, (20, 20))
        window.blit(text_killed, (20, 60))
        window.blit(text_num_fire, (20, 140))
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN and reloadfire==False:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire()
                num_fire-=1
    if wait<0:            
        if not finish:
            player.reset()
            player.move()
            meteorites.draw(window)
            meteorites.update()
            enemies.draw(window)
            enemies.update()
            bullets.draw(window)
            bullets.update()
            kill_list = sprite.groupcollide(enemies, bullets, True, True)
            sprite_list = sprite.spritecollide(player, enemies, True)
            msprite_list = sprite.spritecollide(player, meteorites, True)
            if num_fire==0:
                reloadfire=True
                start_of_reload= t.time()
            if reloadfire==True:
                text_reload = font1.render('Подождите идёт перезарядка:'+str(round(time_of_reload/60)), 1, (255, 255, 255))
                window.blit(text_reload, (300, 500))
                time_of_reload-=1
            if time_of_reload==0:
                reloadfire=False
                num_fire=5
                time_of_reload=120
            if sprite_list:
                health -=1
            for enem in kill_list:
                monsters_killed +=1
                enemy = Enemy('D:\\python_fotos\\ufo.png', 100 , 60 , randint( 0, 800), -50, randint(2, 3))
                enemies.add(enemy)
            if monsters_killed >= 10:
                finish=True
            if lost >= 8 or health <= 0 or msprite_list:
                finish=True
                we_win = False        
        else:
            if we_win:
                window.blit(win,(0,0))
            else:
                window.blit(lose,(0,0))
    display.update()
    clock.tick(60)