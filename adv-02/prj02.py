###################匯入模組###################
import pygame
import sys
import math
import os
###################定義函式###################
def check_click(pos,x_min,y_min,x_max,y_max):
    x_match=x_min<pos[0]<x_max
    y_match=y_min<pos[1]<y_max
    if x_match and y_match:
        return True
    else:
        return False
###################初始化###################
pygame.init() #啟動pygame
width=602 #設定視窗寬度
height=600 #設定視窗高度
os.chdir(sys.path[0])
bg_img='灌籃高手.png'
bg=pygame.image.load(bg_img)
bg_x=bg.get_width()
bg_y=bg.get_height()
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255, 10, 0)

###################建立視窗及物件###################
#設定視窗大小
screen= pygame.display.set_mode((width,height))
#設定視窗標題
pygame.display.set_caption('My Game')
screen=pygame.display.set_mode((bg_x,bg_y))
pygame.display.set_caption('灌籃高手')

###################建立畫布###################
#建立畫布
# bg=pygame.Surface((width,height))
# #畫布為白色(R,G,B)
# bg.fill((255,255,255))
####################撥放音樂######################
mp3_path='692049742.mp3'
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.pause()
pygame.mixer.music.unpause()
pygame.mixer.music.fadeout(3020000)
###################設定文字###################
typeface=pygame.font.get_default_font()
font=pygame.font.Font(typeface,24)
title=font.render('START',True,(255,255,255))
screen.blit(title,(0,0))
tit_w=title.get_width()
tit_h=title.get_height()
####################設定雪花基本參數######################

####################新增fps######################
clock=pygame.time.Clock()
###################循環偵測###################
paint=False
while True:
    clock.tick(20)
    mouse_pos= pygame.mouse.get_pos()
    for event in pygame.event.get():
        #使用者按關按鈕
        if event.type==pygame.QUIT:#如果按下[X]就退出
            sys.exit()#離開遊戲
        if event.type==pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos,0,0,tit_w,tit_h):
                paint = not paint
    if paint:
        title=font.render('STOP',True,RED)
        pygame.mixer.music.play()
    else:
        title=font.render('START',True,RED)
    screen.blit(bg,(0,0))
    screen.blit(title,(0,0))
    pygame.display.update()
    pygame.mouse.get_pos()
    x,y=pygame.mouse.get_pos()
    print(pygame.mouse.get_pos())


    
#     #繪製畫布於視窗上角
#     screen.blit(bg,(0,0))
#     #更新視窗
#     pygame.display.update()
# ###################繪製圖形###################
#     #畫圖形,(畫布,顏色,圓心,半徑,線寬)
    
#     pygame.draw.circle(bg,(0,0,255),(200,100),30,0)
#     pygame.draw.circle(bg,(0,0,255),(400,100),30,0)
#     pygame.draw.rect(bg,(0,255,0),[270,130,60,40],5)
#     pygame.draw.ellipse(bg,(255,0,0),[130,160,60,35],5)
#     pygame.draw.ellipse(bg,(255,0,0),[400,160,60,35],5)
#     pygame.draw.line(bg,(255,0,255),(280,220),(320,220))

#     # pygame.draw.polygon(bg,(100,200,45),[[100,100],[0,200],[200,200]],0)
#     # pygame.draw.arc(bg,(255,10,0),[100,100,100,50],math.radians(180),math.radians(0),2)
#     pygame.mouse.get_pos()
#     x,y=pygame.mouse.get_pos()
    