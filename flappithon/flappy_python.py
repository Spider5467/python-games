


import pygame
import random


pygame.init()
SCREEN_WIDTH=585
SCREEN_HEIGHT=745
GAME_STATE="START"
px=50
py=280
jmpf=5
yv=-0
jt=0
jw=0
fx=0
fsx=966
bx=0
bsx=585
by=0
gap=930
pipx=585
pipy=350#+gap
ebx=165
eby=600
mbx=165
mby=600
sbx=165
sby=390
bt=0
tx=50
ty=50
tt=0
bpt=0
bpt2=0
score=0
cbp=False
cbp2=False
font=pygame.font.SysFont('Pixeled',50)


def score_func():
    score_S=font.render(str(score),False,(0,0,0))
    score_R=score_S.get_rect(center=(300 ,50))
    screen.blit(score_S,score_R)


fy=SCREEN_HEIGHT-120

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run = True
player = pygame.image.load('flappithon/flappy_pythons/python.svg')
bg = pygame.image.load('flappithon/flappy_pythons/background.svg')
floor = pygame.image.load('flappithon/flappy_pythons/floor.svg')
pip1=pygame.image.load('flappithon/flappy_pythons/pipe1.svg')
pip2=pygame.image.load('flappithon/flappy_pythons/pipe2.svg')
SB=pygame.image.load('flappithon/flappy_pythons/start_button.svg')
SB2=pygame.image.load('flappithon/flappy_pythons/start_button2.svg')
MB=pygame.image.load('flappithon/flappy_pythons/menu_button.svg')
MB2=pygame.image.load('flappithon/flappy_pythons/menu_button2.svg')
EB=pygame.image.load('flappithon/flappy_pythons/exit_button.svg')
EB2=pygame.image.load('flappithon/flappy_pythons/exit_button2.svg')
title=pygame.image.load('flappithon/flappy_pythons/title.svg')
died=pygame.image.load('flappithon/flappy_pythons/died.svg')


while run: #just basicly the update function
    if GAME_STATE=="GAME":
        screen.fill((0, 0, 0))
        yv-=0.1
        py-=yv
        pip1_rect = pip1.get_rect(topleft=(pipx, pipy - gap))
        pip2_rect = pip1.get_rect(topleft=(pipx, pipy))
        player_rect = player.get_rect(topleft=(px, py))
        floor_rect = floor.get_rect(topleft=(fx, fy))
        floor_S_rect = floor.get_rect(topleft=(fsx, fy))

        fx+=-1
        fsx+=-1
        bx+=-0.5
        bsx+=-0.5
        pipx-=1

        if pipx <= 0:
            pipy=random.randint(200,500)
            pipx=585-64
            print(pipy)

        if fx <= -966:
            fx=0
            fsx=966
        if bx <= -586:
            bx=0
            bsx=586

        if jt >= 6:
            jt=0

        keys = pygame.key.get_pressed()

        if player_rect.colliderect(floor_rect):
            print("YOU LOSE")
            bx = 0
            eby = 390
            bt = 0
            tt = 0
            ty = 50
            bpt = 0
            GAME_STATE = "GAME_OVER"
        if player_rect.colliderect(floor_S_rect):
            print("YOU LOSE")
            bx = 0
            eby = 390
            bt = 0
            tt = 0
            ty = 50
            bpt = 0
            GAME_STATE = "GAME_OVER"
        if player_rect.colliderect(pip1_rect):
            print("YOU LOSE")
            bx = 0
            eby = 390
            bt = 0
            tt = 0
            ty = 50
            bpt = 0
            GAME_STATE = "GAME_OVER"
        if player_rect.colliderect(pip2_rect):
            print("YOU LOSE")
            bx = 0
            eby = 390
            bt = 0
            tt = 0
            bpt = 0
            ty = 50
            GAME_STATE = "GAME_OVER"

        if px == pipx:
            score += 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    yv=jmpf
                    player = pygame.image.load('flappithon/flappy_pythons/pythonflap.svg')
                if event.key == pygame.K_ESCAPE:
                    event.type = pygame.QUIT
                    pass
            if event.type == pygame.KEYUP:
                if pygame.K_SPACE:
                    player = pygame.image.load('flappithon/flappy_pythons/python.svg')


        screen.blit(bg, (bx, by))
        screen.blit(bg, (bsx, by))
        screen.blit(pip1,(pipx,pipy-gap))
        screen.blit(pip2,(pipx,pipy))
        screen.blit(floor,(fx,fy))
        screen.blit(floor,(fsx,fy))
        screen.blit(player, (px, py))
        score_func()
    if GAME_STATE=="START":
        mouse_pos = pygame.mouse.get_pos()

        SBR = SB.get_rect(topleft=(sbx,sby))
        EBR = SB.get_rect(topleft=(ebx, eby))
        bt+=0.5
        tt+=0.5

        if cbp2:
            bpt2+=1
        if bpt2 >= 10:
            pygame.quit()
        if cbp:
            bpt += 1

        if bt<=40:
            sby+=1
        if bt>=41:
            sby-=1
        if bt == 80:
            bt=0
        if tt<=10:
            ty+=1
        if tt>=11:
            ty-=1
        if tt == 20:
            tt=0

        if bpt >= 10:
            cbp = False
            px=50
            py=280
            yv=-0
            sby=390
            GAME_STATE = "GAME"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if SBR.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed(num_buttons=3 ):
                        SB = SB2
                        cbp=True


                if EBR.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed(num_buttons=3 ):
                        EB=EB2
                        cbp2=True
            if event.type == pygame.KEYDOWN:
                if pygame.K_SPACE:
                    GAME_STATE = "GAME"


        screen.blit(bg, (bx, by))
        screen.blit(SB,(sbx,sby))
        screen.blit(EB,(ebx,eby))
        screen.blit(title, (tx, ty))
    if GAME_STATE=="GAME_OVER":
        screen.fill((0, 0, 0))



        tt+=0.5
        bt+=0.5
        EBR = SB.get_rect(topleft=(ebx, eby))
        MBR = SB.get_rect(topleft=(mbx, mby))
        mouse_pos=pygame.mouse.get_pos()

        if cbp2:
            bpt2+=1
        if bpt2 >= 10:
            cbp2 = False
            cbp = False
            ty=50
            tt=0
            bt=0
            bpt=0
            eby = 600
            bpt2=0
            sbx = 165
            sby = 390
            score=0
            yv=0
            bx=0
            bsx=585
            by=0
            fx = 0
            fsx = 966
            pipy=random.randint(200,500)
            pipx=585
            MB=pygame.image.load('flappithon/flappy_pythons/menu_button.svg')
            GAME_STATE="START"
        if cbp:
            bpt+=1

        if bpt >= 10:
            cbp = False

            pygame.quit()
        if bt <= 40:
            eby += 1
        if bt >= 41:
            eby -= 1
        if bt == 80:
            bt = 0
        if tt <= 10:
            ty += 1
        if tt >= 11:
            ty -= 1
        if tt == 20:
            tt = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EBR.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed(num_buttons=3):
                        EB=EB2
                        cbp = True
                if MBR.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed(num_buttons=3):
                        MB=MB2
                        SB=pygame.image.load('flappithon/flappy_pythons/start_button.svg')
                        cbp2 = True
        screen.blit(bg, (bx, by))
        screen.blit(EB,(ebx,eby))
        screen.blit(MB, (mbx, mby))
        screen.blit(died, (tx, ty))
        score_func()
    pygame.display.update()


pygame.quit()