###############################載入套件###################################
import pygame
import sys
import os
from pygame.locals import *

###############################初期設定###################################
os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()
###############################載入圖片###################################
img_bg = pygame.image.load("image/space.png")
img_sship = [
    pygame.image.load("image/fighter_M.png"),
    pygame.image.load("image/fighter_L.png"),
    pygame.image.load("image/fighter_R.png"),
]

img_burn = pygame.image.load("image/starship_burner.png")
################################遊戲視窗設定##############################
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode(bg_size)
roll_y = 0


####################定義函式######################
def roll_bg():
    """更新背景"""
    global roll_y

    roll_y = (roll_y + 20) % bg_y  # 背景移動
    screen.blit(img_bg, [0, roll_y - bg_y])  # 背景圖左移
    screen.blit(img_bg, [0, roll_y])  # 背景圖接續顯示


def move_starship():
    """移動飛船"""
    global ss_x, ss_y, ss_wh, ss_hh, ss_img
    key = pygame.key.get_pressed()
    ss_img = img_sship[0]
    if key[pygame.K_LEFT]:
        ss_x -= 20
        ss_img = img_sship[1]
    if key[pygame.K_RIGHT]:
        ss_x += 20
        ss_img = img_sship[2]
    if key[pygame.K_UP]:
        ss_y -= 20
    if key[pygame.K_DOWN]:
        ss_y += 20
    ss_hh = ss_img.get_height() / 2
    ss_wh = ss_img.get_width() / 2
    if ss_y < ss_hh:
        ss_y = ss_hh
    if ss_y > bg_y - ss_hh:
        ss_y = bg_y - ss_hh
    if ss_x < ss_wh:
        ss_x = ss_wh
    if ss_x > bg_x - ss_wh:
        ss_x = bg_x - ss_wh
    if ss_x > bg_x - ss_wh:
        ss_x = bg_x - ss_wh
    screen.blit(ss_img, [ss_x - ss_wh, ss_y - ss_hh])


def move_burner():
    """移動燃燒器"""
    global burn_x, burn_y, burn_img
    burn_img = img_burn
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        burn_x -= 20
        ss_img = img_sship[1]
    if key[pygame.K_RIGHT]:
        burn_x += 20
        ss_img = img_sship[2]
    if key[pygame.K_UP]:
        burn_y -= 20
    if key[pygame.K_DOWN]:
        burn_y += 20
    burn_y = ss_y + burn_img.get_height() / 2 + 40
    burn_x = ss_x + burn_img.get_width() / 2 - 9
    burn_hh = burn_img.get_height() / 2
    burn_wh = burn_img.get_width() / 2
    if burn_y < burn_hh:
        burn_y = ss_hh - 20
    if burn_y > bg_y - burn_hh:  # 燃燒器不能超出背景
        burn_y = bg_y - burn_hh
    if burn_x < burn_wh:
        burn_x = ss_wh - 20
    if burn_x > bg_x - burn_wh:
        burn_x = bg_x - burn_wh
    if burn_x > bg_x - burn_wh:
        burn_x = bg_x - burn_wh
    screen.blit(burn_img, [burn_x - burn_wh, burn_y - burn_hh])


###############################玩家設定###################################
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width() / 2
ss_hh = img_sship[0].get_height() / 2
ss_img = img_sship[0]
burn_shift = 0
burn_w, burn_h = img_burn.get_rect().size
mp3_path = "game.mp3"
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.pause()
pygame.mixer.music.unpause()
pygame.mixer.music.fadeout(3020000)
################################主程式##################################
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F1:
                screen = pygame.display.set_mode(bg_size, FULLSCREEN)
            elif event.key == K_ESCAPE:
                screen.pygame.display.set_mode(bg_size)
    roll_bg()
    move_starship()
    move_burner()
    pygame.display.update()
