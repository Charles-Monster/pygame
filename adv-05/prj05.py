######################匯入模組######################
import pygame
import sys
import os
import random
####################定義函式######################
def mouse_update():
    global hammer,hammer_tick
    if hammer==ham1:
        if hammer_tick>hammer_max_tick:
            hammer=ham2
            hammer_tick=0
            mouse=ham1
        else:
            hammer_tick+=1
            mouse=ham2
            
    screen.blit(hammer,(mouse_pos[0]-15,mouse_pos[1]-15))
def gophers_update():
    global tick,pos,score,times
    if tick>max_tick:
        new_pos=random.randint(0,5)
        pos=pos6[new_pos]
        tick=0
        times+=1
    elif score>20:
        game_over()
        pygame.display.update()
    else:
        tick+=1
    screen.blit(gopher,(pos[0]-gopher.get_width()/2,pos[1]-gopher.get_height()/2))
    
def score_update():
    score_sur=score_font.render(str(score),False,red)
    screen.blit(score_sur,(10,10))
def check_click(pos,x_min,y_min,x_max,y_max):
    x_match=x_min<pos[0]<x_max
    y_match=y_min<pos[1]<y_max
    if x_match and y_match:
        return True
    else:
        return False
def times_update():
    times_sur=times_font.render(str(times),True,red)
    screen.blit(times_sur,(bg_x-times_sur.get_width()-10,10))
    
def game_over():
    screen.fill(black)
    end_sur=score_font.render(f'game over your score is:{score}',False,red)
    screen.blit(end_sur,(bg_x/2-end_sur.get_width()/2,bg_y/2-end_sur.get_height()/2))
####################初始化######################
os.chdir(sys.path[0])
pygame.init()
blue = (0,0,255)
white=(255,255,255)
black = (0,0,0)
red = (255,0,0)
clock = pygame.time.Clock()
tick = 0
max_tick = 20
bg_img='u.png'
bg=pygame.image.load(bg_img)
bg_x=bg.get_width()
bg_y=bg.get_height()

######################建立視窗######################
bg_x = 800
bg_y = 600
screen = pygame.display.set_mode([bg_x,bg_y])
pygame.display.set_caption("打地鼠")
######################背景物件######################
# 將背景填滿黑色
######################次數物件######################
times=0
times_max=180
typeface=pygame.font.get_default_font()
times_font=pygame.font.Font(typeface,24)


######################地鼠物件######################
pos6 = [[195,305],[400,305],[610,305],[195,450],[400,450],[610,450]]
for  event in pygame.event.get():
    gopher3=random.randint(1,2)
    if gopher3==1:
        gopher2 = pygame.image.load("大熊.jpg")
    else:
        gopher=pygame.image.load('胖虎.jpg')
    # pos6 = [[200,200],[300,200],[400,200],[200,300],[300,300],[400,300]]
    pos = pos6[0] # 外圍記錄圓的位子
    gophers=pygame.image.load('u.png')
######################分數物件######################
score=0
typeface=pygame.font.get_default_font()
score_font=pygame.font.Font(typeface,24)
######################滑鼠物件######################
pygame.mouse.set_visible(False)
ham1=pygame.image.load('Hammer1.png')
ham2=pygame.image.load('Hammer2.png')
hammer=ham2
hammer_tick=0
hammer_max_tick=5
######################循環偵測######################
while True:
    clock.tick(30)
    mouse_pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            for  event in pygame.event.get():
                gopher3=random.randint(1,2)
                # pos6 = [[200,200],[300,200],[400,200],[200,300],[300,300],[400,300]]
                pos = pos6[0] # 外圍記錄圓的位子
                gophers=pygame.image.load('u.png')
            hammer=ham1#new
            if check_click(mouse_pos,pos[0]-50,pos[1]-50,pos[0]+50,pos[1]+50)and gopher3==1:
                score+=1
                gopher2= pygame.image.load("大熊.jpg")
            elif check_click(mouse_pos,pos[0]-50,pos[1]-50,pos[0]+50,pos[1]+50)and gopher3==2:
                score-=3
                gopher=pygame.image.load('胖虎.jpg')
    if times>=times_max:
        game_over()
    else:
        screen.blit(bg,(0,0))
        gophers_update()
        # new pygame.draw.circle(screen,red,mouse_pos,10)
        score_update()
        print(f"{times}")
        times_update()
        mouse_update()#new
    pygame.display.update()