from pygame import *
from random import randint
w = 1000
h = 800
window = display.set_mode((w, h))
clock = time.Clock()
Fps = 80
loose_bg = transform.scale(image.load("loose_bg.jpg"), (w, h))
mixer.init()
mixer.music.load("music.ogg")
mixer.music.set_volume(0.5)
mixer.music.play()
death = mixer.Sound("death.ogg")
regenerate = mixer.Sound("life.ogg")
loose = mixer.Sound("loose.ogg")

walkright = [image.load("right.png"),image.load("right.png"),image.load("right.png"),image.load("right.png"),image.load("right.png"),image.load("right.png")]
walkleft = [image.load("left.png"),image.load("left.png"),image.load("left.png"),image.load("left.png"),image.load("left.png"),image.load("left.png")]
walkup = [image.load("up.png"),image.load("up.png"),image.load("up.png"),image.load("up.png"),image.load("up.png"),image.load("up.png")]
walkdown = [image.load("down.png"),image.load("down.png"),image.load("down.png"),image.load("down.png"),image.load("down.png"),image.load("down.png")]
idle = [image.load("stand.png"), image.load("close.png")]
global lost
lost = 0
class Main_ch(sprite.Sprite):
    def __init__(self, x, y, speed, i):
        super().__init__()
        self.image = transform.scale(image.load(i),(100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.left = False
        self.right = False
        self.up = False
        self.down= False
        self.idle = False
        self.count = 0
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def hide(self):
        self.rect.x += 100000
class Heart():
    def __init__(self, x, y, speed, i):
        super().__init__()
        self.image = transform.scale(image.load(i),(100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.left = False
        self.right = False
        self.up = False
        self.down= False
        self.idle = False
        self.count = 0
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def hide(self):
        self.rect.x += 100000
class Slime(Main_ch):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] or keys[K_LEFT] and self.rect.x > 10:
            global speed
            self.rect.x -= self.speed
            self.left = True
            self.right = False
            self.down = False
            self.up = False
            self.idle = False
        elif keys[K_d] or keys[K_RIGHT] and self.rect.x < 800:
            global speed
            self.rect.x += self.speed
            self.left = False
            self.right = True
            self.down = False
            self.up = False
            self.idle = False
        elif keys[K_w] or keys[K_UP] and self.rect.y < 1000:
            self.rect.y -= self.speed
            self.left = False
            self.right = False
            self.down = False
            self.up = True
            self.idle = False
        elif keys[K_s] or keys[K_DOWN] and self.rect.y > 10 or self.rect.y > 500:
            self.rect.y += self.speed
            self.left = False
            self.right = False
            self.down = True
            self.up = False
            self.idle = False
            if self.rect.y > 900:
                    global lost
                    lost += 1
                    self.rect.x = 100
                    self.rect.y = 100
                    death.play()
        elif idle:
            self.idle = True
            self.left = False
            self.right = False
            self.down = False
            self.up = False
            self.count = 0
            self.up = False
    def animation(self):
        if self.count + 1 >= 30:
            self.count = 0
        if self.left == True:
            window.blit(walkleft[self.count//10],(self.rect.x, self.rect.y))
            self.count += 1
        elif self.right == True:
            window.blit(walkright[self.count//10],(self.rect.x, self.rect.y))
            self.count += 1
        elif self.up == True:
            window.blit(walkup[self.count//10],(self.rect.x, self.rect.y))
            self.count += 1
        elif self.down == True:
            window.blit(walkdown[self.count//10],(self.rect.x, self.rect.y))
            self.count += 1
        else:
            window.blit(idle[self.count//10],(self.rect.x, self.rect.y))              
    def start1(self):
        self.rect.y = 100
        self.rect.x = 300
mainch = Slime(100, 100, 8, "stand.png")
bg2 = transform.scale(image.load("floor.jpg"), (w, h))
heart1 = Heart(40, 10, 0, "heart.png")
heart2 = Heart(90, 10, 0, "heart.png")
heart3 = Heart(140, 10, 0, "heart.png")
game = True
final = False
bgx = 0
lose = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if final != True:
        window.blit(bg2, (0, 0))
        mainch.reset()
        mainch.update()
        mainch.animation()
        heart1.reset()
        heart2.reset()
        heart3.reset()
        if lost == 1:
            heart3.hide()
        if lost == 2:
            heart2.hide()
        if lost == 3:
            heart1.hide()
            final = True
            lose = True
            mixer.music.stop()
    if final == True:
        loose.play(True)
        loose.set_volume(0.1)
        window.blit(loose_bg, (bgx +0, 0))
        window.blit(loose_bg, (bgx +1000, 0))
        bgx -= 2
        if bgx == -1000:
            bgx = 0
        
    

    display.update()
    clock.tick(Fps)
