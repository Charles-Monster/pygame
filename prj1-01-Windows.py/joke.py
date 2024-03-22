###################匯入模組###################
import pygame
import sys
import math
import random
import os

###################初始化###################
pygame.init() #啟動pygame
width=850#設定視窗寬度
height=432 #設定視窗高度
os.chdir(sys.path[0])
bg_img='i.webp'
bg=pygame.image.load(bg_img)
bg_x=bg.get_width()
bg_y=bg.get_height()
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255, 10, 0)
BLUE=(0,0,255)

###################定義函式###################
def check_click(pos,x_min,y_min,x_max,y_max):
    x_match=x_min<pos[0]<x_max
    y_match=y_min<pos[1]<y_max
    if x_match and y_match:
        return True
    else:
        return False
def snow_fall():
    global x_site,y_site,x_shift,radius
    for snow in snow_list:
        pygame.draw.circle(screen,WHITE,(snow['x_site'],snow['y_site']),snow['radius'])

        snow['x_site']+=snow['x_shift']
        snow['y_site']+=snow['radius']
        if snow['y_site']>bg_y or snow['x_site']>bg_x:
            snow['y_site']=random.randint(-bg_y,-1)
            snow['x_site']=random.randint(0,bg_x)

###################建立視窗及物件###################
#設定視窗大小
screen= pygame.display.set_mode((width,height))
#設定視窗標題
pygame.display.set_caption('My Game')
screen=pygame.display.set_mode((bg_x,bg_y))
pygame.display.set_caption('ooopa loompas')

###################建立畫布###################
#建立畫布
# bg=pygame.Surface((width,height))
# #畫布為白色(R,G,B)
# bg.fill((255,255,255))
####################撥放音樂######################
mp3_path='g.mp3'
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.pause()
pygame.mixer.music.unpause()
pygame.mixer.music.fadeout(3020000)
pygame.mixer.music.pause()
###################設定文字###################
typeface=pygame.font.get_default_font()
font=pygame.font.Font(typeface,24)
title=font.render('START',True,(255,255,255))
screen.blit(title,(0,0))
tit_w=title.get_width()
tit_h=title.get_height()
####################設定雪花基本參數######################
snow_list=[]
for i in range(1500):
    x_site= random.randrange(0,bg_x)
    y_site= random.randrange(-bg_y,-10)
    x_shift=random.randint(-10,1)
    radius=random.randint(4,6)

    snow_list.append({'x_site':x_site,'y_site':y_site,'x_shift':x_shift,'radius':radius})
####################新增fps######################
clock=pygame.time.Clock()
###################循環偵測###################
paint=False
cnt=0
while True:
    clock.tick(100)
    mouse_pos= pygame.mouse.get_pos()
    for event in pygame.event.get():
        #使用者按關按鈕
        if event.type==pygame.QUIT:#如果按下[X]就退出
            sys.exit()#離開遊戲
        if event.type==pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos,0,0,tit_w,tit_h):
                paint = not paint
    if cnt > 10:
        cnt=0
        x_shift=random.randint(-3,3)
    else:
        cnt+=1
    screen.blit(bg,(0,0))
    screen.blit(title,(0,0))
    if paint:
        title=font.render('STOP',True,BLUE)
        pygame.mixer.music.unpause()
    else:
        title=font.render('START',True,BLUE)
        pygame.mixer.music.pause()
    # screen.blit(bg,(0,0))
    # screen.blit(title,(0,0))
    pygame.display.update()
    pygame.mouse.get_pos()
    x,y=pygame.mouse.get_pos()
    # print(pygame.mouse.get_pos())