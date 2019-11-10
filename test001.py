import sys
import pygame
import spritesheet
import random
#newsprite는 일단 필요 없는 파일


#슬라임 정보 


#일단은 기본 크기에 해당 150,119의 세 배
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 357

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Pymon_v001")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 20
pos_y = 20

clock = pygame.time.Clock()

#직접 가져오기
s1 = spritesheet.spritesheet('스프라이트_기본UI.png')
s2 = spritesheet.spritesheet('스프라이트_슬라임형태.png')
s3 = spritesheet.spritesheet('스프라이트_버튼UI.png')
s4 = spritesheet.spritesheet('스프라이트_미니게임.png')
s5 = spritesheet.spritesheet('배경_우주.png')

#이제 넣어줌과 동시에 확대도 시켜주자!
#원래 변수를 넣어야 하지만 여기서는 합친 값121 지정
btu = (150,119)
btu2 = (152,121)
base = []
base.append(s1.image_at((1, 1, btu[0] , btu[1])))
base[0] = pygame.transform.scale(base[0],(btu[0]*3,btu[1]*3))



#슬라임과 표정은 54,37로 같고, 점프만 54,45 좀 더 크다. 2칸씩 여분
slimetu = (54,37,45)
slimetu2 = (56,39,47)


#일반용과 미니게임용 2개로 나뉜다.
slimeE = []
slimeE2 = []
for i in range(0,16):
    slimeE.append(s2.image_at((1+slimetu2[0]*(i+1), 1, slimetu[0] , slimetu[1])))
    slimeE[i] = pygame.transform.scale(slimeE[i],(slimetu[0]*3,slimetu[1]*3))
    slimeE2.append(s2.image_at((1+slimetu2[0]*(i+1), 1, slimetu[0] , slimetu[1])))
    slimeE2[i] = pygame.transform.scale(slimeE2[i],(slimetu[0]*2,slimetu[1]*2))

for i in range(0,17):
    slimeE.append(s2.image_at((1+slimetu2[0]*i, 1+slimetu2[1], slimetu[0] , slimetu[1])))
    slimeE[i+16] = pygame.transform.scale(slimeE[i+16],(slimetu[0]*3,slimetu[1]*3))
    slimeE2.append(s2.image_at((1+slimetu2[0]*i, 1+slimetu2[1], slimetu[0] , slimetu[1])))
    slimeE2[i+16] = pygame.transform.scale(slimeE2[i+16],(slimetu[0]*2,slimetu[1]*2))

#일반용만
slimeB = []
for i in range(0,3) : 
    slimeB.append(s2.image_at((1, 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i] = pygame.transform.scale(slimeB[i],(slimetu[0]*3,slimetu[1]*3))
for i in range(0,3) : 
    slimeB.append(s2.image_at((1+slimetu2[0], 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i+3] = pygame.transform.scale(slimeB[i+3],(slimetu[0]*3,slimetu[1]*3))
for i in range(0,3) : 
    slimeB.append(s2.image_at((1+slimetu2[0]*2, 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i+6] = pygame.transform.scale(slimeB[i+6],(slimetu[0]*3,slimetu[1]*3))
for i in range(0,3) : 
    slimeB.append(s2.image_at((1+slimetu2[0]*2, 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i+9] = pygame.transform.scale(slimeB[i+9],(slimetu[0]*3,slimetu[1]*3))
for i in range(0,3) : 
    slimeB.append(s2.image_at((1+slimetu2[0]*2, 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i+12] = pygame.transform.scale(slimeB[i+12],(slimetu[0]*3,slimetu[1]*3))

#일반용과 미니게임 용
slimeJM = []
slimeJM2 = []                                           
for i in range(0,8):
    slimeJM.append(s2.image_at((1+slimetu2[0]*(i+5), 1+slimetu2[1]*2, slimetu[0] , slimetu[2])))
    slimeJM[i] = pygame.transform.scale(slimeJM[i],(slimetu[0]*3,slimetu[2]*3))
    slimeJM2.append(s2.image_at((1+slimetu2[0]*(i+5), 1+slimetu2[1]*2, slimetu[0] , slimetu[2])))                                       
    slimeJM2[i] = pygame.transform.scale(slimeJM2[i],(slimetu[0]*2,slimetu[2]*2))

#
#미니게임용 추가 이미지
#    
slimeB2 = []
slimeB2.append(s2.image_at((1, 1+slimetu2[1]*(2), slimetu[0] , slimetu[1])))
slimeB2[0] = pygame.transform.scale(slimeB2[0],(slimetu[0]*2,slimetu[1]*2))

#3종의 버튼
btntu = (27,17,38)
btntu2 = (29,19,40)

btnBase = []
for i in range(0,4) :
    btnBase.append(s3.image_at((1+btntu2[0]*i, 1, btntu[0] , btntu[0])))
    btnBase[i] = pygame.transform.scale(btnBase[i],(btntu[0]*3,btntu[0]*3))
    
btnCtrl = []
for i in range(0,3) :
    btnCtrl.append(s3.image_at((1+btntu2[1]*i+btntu2[0]*4, 1, btntu[1] , btntu[1])))
    btnCtrl[i] = pygame.transform.scale(btnCtrl[i],(btntu[1]*3,btntu[1]*3))
for i in range(0,3) :
    btnCtrl.append(s3.image_at((1+btntu2[1]*i+btntu2[0]*4, 1+btntu2[1], btntu[1] , btntu[1])))
    btnCtrl[i+3] = pygame.transform.scale(btnCtrl[i+3],(btntu[1]*3,btntu[1]*3))
    
btnGame = []
for i in range(0,3) :
    btnGame.append(s3.image_at((1+btntu2[2]*i, 1+btntu2[1]*2, btntu[2] , btntu[2])))
    btnGame[i] = pygame.transform.scale(btnGame[i],(btntu[2]*3,btntu[2]*3))


#줄넘기는 직접 그려서 해결하자!
#전방향 1칸씩
#던전60,60
#계단68,22
#구름127, 80
#dt[3] = 70 등으로 불러온다.
#미니게임은 2배율만 한다!
gtu = (60,68,22,127,80)
gtu2 = (62,70,24,129,82)

dun_block = []
for i in range(0,5) :
    dun_block.append(s4.image_at((1+gtu2[0]*i, 1, gtu[0] , gtu[0])))
    dun_block[i] = pygame.transform.scale(dun_block[i],(gtu[0]*2,gtu[0]*2))
for i in range(0,5) :
    dun_block.append(s4.image_at((1+gtu2[0]*(i+9), 1, gtu[0] , gtu[0])))
    dun_block[i+5] = pygame.transform.scale(dun_block[i+5],(gtu[0]*2,gtu[0]*2))

dun_ghost = []
for i in range(0,4):
    dun_ghost.append(s4.image_at((1+gtu2[0]*(i+5), 1, gtu[0] , gtu[0])))
    dun_ghost[i] = pygame.transform.scale(dun_ghost[i],(gtu[0]*2,gtu[0]*2))
    
stair_block = []
for i in range(0,6):
    stair_block.append(s4.image_at((1+gtu2[1]*i, 1+gtu2[0], gtu[1] , gtu[2])))
    stair_block[i] = pygame.transform.scale(stair_block[i],(gtu[1]*2,gtu[2]*2))

stair_cloud = []
for i in range(0,6) : 
    stair_cloud.append(s4.image_at((1+gtu2[3]*i, 1+gtu2[0]+gtu2[2], gtu[3] , gtu[4])))
    stair_cloud[i] = pygame.transform.scale(stair_cloud[i],(gtu[3]*2,gtu[4]*2))
for i in range(0,6) : 
    stair_cloud.append(s4.image_at((1+gtu2[3]*i, 1+gtu2[0]+gtu2[2], gtu[3] , gtu[4])))
    stair_cloud[i] = pygame.transform.scale(stair_cloud[i],(gtu[3]*2,gtu[4]*2))

#우주 이미지
#우주 911 3426
stair_space = s5.image_at((1,1,911,3426))

'''
slime1 = s2.image_at((0,0,56,39))
slimeE1 = s2.image_at((56,0,56,39))
slimeEE1 = s2.image_at((112,0,56,39))
#3배율 사용!
img2 = pygame.transform.scale(img1,(450,357))
slime2 = pygame.transform.scale(slime1,(168,117))
slimeE2 = pygame.transform.scale(slimeE1,(168,117))
slimeEE2 = pygame.transform.scale(slimeEE1,(168,117))
#자르기 연구
#image3 = pygame.image.load('스프라이트_슬라임형태.png').convert_alpha()
#image33 = image3.subsurface((0,0,50,50))

#working하는 동안에는 동작이 되지 않는다. 다중 입력을 막는다
working = 0
emotion = -1

'''


#------------ 인자 모아둠 --------------------------
global On_norm
On_norm = 1
global On_game
On_game = 0
global On_miniGame_stair
On_miniGame_stair = 0
global On_miniGame_dun
On_miniGame_dun = 0


On_work = 0
On_aniCount = 0

norm_num = 0
motion_num = 0

btnB_active = 0
global btnB_ani
btnB_ani = 0

btnC_active = 0
global btnC_ani
btnC_ani = 0

btnG_active = 0
global btnG_ani
btnG_ani = 0


On_miniGame_stair = 0
On_miniGame_Dun = 0
global drag_x
drag_x = 0
global drag_y
drag_y = 0
global impSlime
#계단 생성 리스트 8개 기본으로 가지고 있기
stairs = []
prepare = 0

#---------------------------------------------------

def call_back(types):
    screen.blit(base[0], (0,0))

def call_character(type, base, emo):
    screen.blit (slimeB[base], (150,150))
    screen.blit (slimeE[emo], (150,150))
    '''
    screen.blit (btnBase[0], (50,10))
    screen.blit (btnBase[1], (50,100))
    screen.blit (btnBase[2], (50,190))
    screen.blit (btnBase[3], (50,280))

    '''

#일반 상태 함수
def make_anime_sl_norm(num) :
    if(num >=0 and num < 8):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[0], (150,150))
    elif(num >=8 and num < 16):
        screen.blit (slimeB[1], (150,150))
        screen.blit (slimeE[0], (150,151))
    elif(num >=16 and num < 24):
        screen.blit (slimeB[2], (150,150))
        screen.blit (slimeE[0], (150,151))
    elif(num >=24 and num < 32):
        screen.blit (slimeB[1], (150,150))
        screen.blit (slimeE[0], (150,151))
    elif(num >=32 and num < 40):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[0], (150,150))
    else:
        screen.blit (slimeB[1], (80,80))
        screen.blit (slimeE[0], (80,80))

    back = num + 1
    return back

#먹기 함수
def make_anime_sl_jm(num):
    #테스트용 예시
    #screen.blit (slimeB[6], (150,150))
    #screen.blit (slimeE[6], (150,150))

    #보정이 필요하다 -24(8x3)만큼, 원래 기본보다 픽셀 크기 자체가 달라서
    #상승 (0~4)
    if(num < 2):
        screen.blit(slimeJM[0], (150,126))
    elif(num < 4):
        screen.blit(slimeJM[1], (150,124-6))
    elif(num < 6):
        screen.blit(slimeJM[2], (150,122-12))
    elif(num < 8):
        screen.blit(slimeJM[3], (150,120-18))
    elif(num < 10):
        screen.blit(slimeJM[4], (150,118-24))
    #하강(5~9)
    elif(num < 12):
        screen.blit(slimeJM[5], (150,121-18))
    elif(num < 14):
        screen.blit(slimeJM[6], (150,124-12))
    elif(num < 16):
        screen.blit(slimeJM[7], (150,126-6))
    elif(num < 18):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[2], (150,150))
    elif(num < 20):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[1], (150,150))
    else:
        screen.blit (slimeB[0], (80,80))
        screen.blit (slimeE[0], (80,80))
    back = num + 1
    return back

#게임 내 점프 함수
#크기 감소로 인해 좌표를 28,47만큼 보정해서 중앙으로 보낸다.
#스프라이트 크기 차이에 대한 y좌표는 16(8X2)만큼 보정한다.
#규칙을 바꾸면서 슬라임이 제자리에서 움직이도록 바꿨다. 화면만 움직인다.
#추가적인 점프를 추가한다.
def make_anime_sl_mgjm(num,dir):
    global impSlime
    global drag_x
    global drag_y
    if(num < 1):
        if dir==1:
            #screen.blit(slimeJM2[0], (178+17*1,173-12*1))
            screen.blit(slimeJM2[0], (178,173-4*1))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[0], True, False)
            #screen.blit(impSlime, (178-17*1,173-12*1))
            screen.blit(impSlime, (178,173-4*1))
            drag_x = drag_x-17
            drag_y = drag_y-12
    elif(num < 2):
        if dir==1:
            #screen.blit(slimeJM2[1], (178+17*2,173-12*2))
            screen.blit(slimeJM2[1], (178,173-4*2))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[1], True, False)
            #screen.blit(impSlime, (178-17*2,173-12*2))
            screen.blit(impSlime, (178,173-4*2))
            drag_x = drag_x-17
            drag_y = drag_y-12
    elif(num < 3):
        if dir==1:
            #screen.blit(slimeJM2[2], (178+17*3,173-12*3))
            screen.blit(slimeJM2[2], (178,173-4*3))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[2], True, False)
            #screen.blit(impSlime, (178-17*3,173-12*3))
            screen.blit(impSlime, (178,173-4*3))
            drag_x = drag_x-17
            drag_y = drag_y-12
    elif(num < 4):
        if dir==1:
            #screen.blit(slimeJM2[3], (178+17*4,173-12*4))
            screen.blit(slimeJM2[3], (178,173-4*4))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[3], True, False)
            #screen.blit(impSlime, (178-17*4,173-12*4))
            screen.blit(impSlime, (178,173-4*4))
            drag_x = drag_x-17
            drag_y = drag_y-12
    elif(num < 5):
        if dir==1:
            #screen.blit(slimeJM2[4], (178+17*5,173-12*5))
            screen.blit(slimeJM2[4], (178,173-4*5))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[4], True, False)
            #screen.blit(impSlime, (178-17*5,173-12*5))
            screen.blit(impSlime, (178,173-4*5))
            drag_x = drag_x-17
            drag_y = drag_y-12
    #하강(5~9)
    elif(num < 6):
        if dir==1:
            #screen.blit(slimeJM2[5], (178+17*6,173-12*5+6))
            screen.blit(slimeJM2[5], (178,173-4*4))
            drag_x = drag_x+17
            drag_y = drag_y+6
        else :
            impSlime = pygame.transform.flip(slimeJM2[5], True, False)
            #screen.blit(impSlime, (178-17*6,173-12*5+6))
            screen.blit(impSlime, (178,173-4*4))
            drag_x = drag_x-17
            drag_y = drag_y+6
    elif(num < 7):
        if dir==1:
            #screen.blit(slimeJM2[6], (178+17*7,173-12*5+11))
            screen.blit(slimeJM2[6], (178,173-4*3))
            drag_x = drag_x+17
            drag_y = drag_y+5
        else :
            impSlime = pygame.transform.flip(slimeJM2[6], True, False)
            #screen.blit(impSlime, (178-17*7,173-12*5+11))
            screen.blit(impSlime, (178,173-4*3))
            drag_x = drag_x-17
            drag_y = drag_y+5
    elif(num < 8):
        if dir==1:
            #screen.blit(slimeJM2[7], (178+17*8,173-12*5+16))
            screen.blit(slimeJM2[7], (178,173-4*2))
            drag_x = drag_x+17
            drag_y = drag_y+5
        else :
            impSlime = pygame.transform.flip(slimeJM2[7], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16))
            screen.blit(impSlime, (178,173-4*2))
            drag_x = drag_x-17
            drag_y = drag_y+5
    elif(num < 9):
        if dir==1:
            #screen.blit(slimeB2[0], (178+17*8,173-12*5+16+16))
            #screen.blit(slimeE2[2], (178+17*8,173-12*5+16+16))
            screen.blit(slimeB2[0], (178,189-4))
            screen.blit(slimeE2[2], (178,189-4))
        else :
            impSlime = pygame.transform.flip(slimeB2[0], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16+16))
            screen.blit(impSlime, (178,189-4))
            impSlime = pygame.transform.flip(slimeE2[2], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16+16))
            screen.blit(impSlime, (178,189-4))
    elif(num < 10):
        if dir==1:
            #screen.blit(slimeB2[0], (178+17*8,173-12*5+16+16))
            #screen.blit(slimeE2[1], (178+17*8,173-12*5+16+16))
            screen.blit(slimeB2[0], (178,189))
            screen.blit(slimeE2[1], (178,189))
        else :
            impSlime = pygame.transform.flip(slimeB2[0], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16+16))
            screen.blit(impSlime, (178,189))
            impSlime = pygame.transform.flip(slimeE2[1], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16+16))
            screen.blit(impSlime, (178,189))
    else:
        screen.blit (slimeB2[0], (80,80))
        screen.blit (slimeE2[0], (80,80))
    back = num + 1
    return back

def make_anime_sl_eat(num):
    #입 벌리기
    if(num < 2):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[4], (150,150))
    elif(num < 4):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[5], (150,150))
    elif( num < 6):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[6], (150,150))
    elif(num < 8):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[7], (150,150))
    elif(num < 12):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[8], (150,150))
    #입 다물기
    elif(num < 14):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[9], (150,150))
    elif(num < 16):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[10], (150,150))
    elif(num < 18):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[1], (150,150))
    else:
        screen.blit (slimeB[0], (80,80))
        screen.blit (slimeE[0], (80,80))

    back = num + 1
    return back
'''
def exam_button(x,y,active):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if active==1:
        screen.blit (btnBase[0], (x,y))
        return 1
    elif x+81 > mouse[0] > x and y+81 > mouse[1] > y:
        screen.blit (btnBase[0], (x,y))
        if (click[0] == 1):
            return 1
        return 0
    elif x+81 > mouse[0] > x and y+81 > mouse[1] > y :
        screen.blit (btnBase[0], (x,y))
        return 1
'''
def base_button(x,y,ext):
    global btnB_ani
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #ext는 펄쳐져 있는지 여부를 나타낸다.
    if ext == 0:
        if x+81 > mouse[0] > x and y+81 > mouse[1] > y and click[0] == 1:
            screen.blit (btnBase[1], (x,y))
            return 1
        else :
            screen.blit (btnBase[1], (x,y))
            return 0
    elif ext == 1:
        screen.blit (btnBase[3], (x,y-10*btnB_ani))
        screen.blit (btnBase[2], (x,y-5*btnB_ani))
        screen.blit (btnBase[1], (x,y))
        if btnB_ani < 17:
            btnB_ani = btnB_ani + 3
        if not(x+81 > mouse[0] > x and y+81 > mouse[1] > y) and click[0] == 1:
            btnB_ani = 0
            btnC_ani = 0
            btnG_ani = 0
            return 0
        return 1

def ctrl_button(x,y,ext):
    global btnC_ani
    global On_game
    global On_norm
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if ext == 0:
        if x+51 > mouse[0] > x and y+51 > mouse[1] > y and click[0] == 1:
            screen.blit (btnCtrl[0], (x,y))
            return 1
        else :
            screen.blit (btnCtrl[0], (x,y))
            return 0
    elif ext == 1:
        #3칸씩 18회 1~5 배수로 이동
        screen.blit (btnCtrl[5], (x,y+15*btnC_ani))
        screen.blit (btnCtrl[4], (x,y+12*btnC_ani))
        screen.blit (btnCtrl[3], (x,y+9*btnC_ani))
        screen.blit (btnCtrl[2], (x,y+6*btnC_ani))
        screen.blit (btnCtrl[1], (x,y+3*btnC_ani))
        screen.blit (btnCtrl[0], (x,y))
        if btnC_ani < 18:
            btnC_ani = btnC_ani + 3
        if x+51 > mouse[0] > x and y+51+12*18 > mouse[1] > y+12*18 and click[0] == 1:
            On_norm = 0
            On_game = 1
            return 0
        if not(x+51 > mouse[0] > x and y+51 > mouse[1] > y) and click[0] == 1:
            btnB_ani = 0
            btnC_ani = 0
            btnG_ani = 0    
            return 0
        return 1

def game_button(x,y):
    global btnG_ani
    global On_game
    global On_norm
    global On_miniGame_stair
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

        #3칸씩 18회 1~5 배수로 이동
    screen.blit (btnGame[2], (x+8*btnG_ani,y))
    screen.blit (btnGame[1], (x+4*btnG_ani,y))
    screen.blit (btnGame[0], (x,y))
    if btnG_ani < 36:
        btnG_ani = btnG_ani + 3
    if x+114 > mouse[0] > x and y+114 > mouse[1] > y and click[0] == 1:
        On_miniGame_stair = 1
    elif not(x+114 > mouse[0] > x and y+114 > mouse[1] > y) and click[0] == 1:
        btnB_ani = 0
        btnC_ani = 0
        #btnG_ani = 0
        if btnG_ani == 36 :
            btnG_ani = 0
            On_norm = 1
            On_game = 0
        return 0
    return 1


def drag_ctrlx():
    global drag_x
    if drag_x == 0:
        return 0
    elif drag_x < 0:
        if drag_x <= -8:
            drag_x = drag_x + 8
        elif drag_x > -8:
            drag_x = 0
    elif drag_x > 0:
        if drag_x >= 8:
            drag_x = drag_x - 8
        elif drag_x < 8:
            drag_x = 0
        

def drag_ctrly():
    global drag_y
    if drag_y == 0:
        return 0
    elif drag_y < 0:
        if drag_y <= -3:
            drag_y = drag_y + 3
        elif drag_y > -3:
            drag_y = 0
    elif drag_y > 0:
        if drag_y >= 3:
            drag_y = drag_x - 3
        elif drag_y < 3:
            drag_y = 0
            
#y좌표에 해당하는 num은 1씩 늘려주기만 하면 되고
#x대 대한 랜덤 처리는 본 함수에서 처리한다.
def make_stair(x,num):
    global drag_x
    global drag_y
    if num <= 30:
        screen.blit (stair_block[0], (164-drag_x+136*x,263-drag_y-44*num))
    elif num <= 60:
        screen.blit (stair_block[1], (164-drag_x+136*x,263-drag_y-44*num))
    elif num <= 90 :
        screen.blit (stair_block[2], (164-drag_x+136*x,263-drag_y-44*num))
    elif num <= 150 :
        screen.blit (stair_block[3], (164-drag_x+136*x,263-drag_y-44*num))
    elif num <= 250 :
        screen.blit (stair_block[4], (164-drag_x+136*x,263-drag_y-44*num))
    #return (num+1)

def make_rand_stair(x):
    i = random.randrange(0,2)
    if i == 0 and x>-8:
        return x-1
    elif i == 1 and x < 8:
        return x+1
    elif x<= -8 :
        return x+1
    elif x>= 8 :
        return x-1

#미리 계단 만들어 두기(함수 아님)
#항상 8개를 유지한다.
stairs = []
total_stair = 0
'''
stairs.append(0)
imp = 0
for i in range (1,10):
    imp = make_rand_stair(imp)
    stairs.append(imp)

total_stair = 10;
'''

#-------------------------------------------------------------------
#실질 구현
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if On_norm == 1 :
        #이건 기본적으로 수행하는데..
        call_back(0)
        if On_work == 0 :
            norm_num = make_anime_sl_norm(norm_num)
            if norm_num == 40:
                norm_num = 0
            #기존의 부동 출력 방식
            #call_character(0, 0, 0)

        #본격 애니메이션 받기
        if On_work == 0 :
            key_event = pygame.key.get_pressed()
            if key_event[pygame.K_UP]:
                On_work = 1
            if key_event[pygame.K_RIGHT]:
                On_work = 2
                ''''
            if key_event[pygame.K_LEFT]:
                pos_x -= 1
                emotion = emotion * -1
            if key_event[pygame.K_DOWN]:
                pos_y += 1
                emotion = emotion * -1
                '''
        #이건 특별히 수행하는 애니메이션 다중 수행을 막는다.
        if On_work == 1 :
            motion_num = make_anime_sl_jm(motion_num)
            if motion_num == 20 :
                motion_num = 0
                On_work = 0
                norm_num = 0
            
        if On_work == 2 :
            motion_num = make_anime_sl_eat(motion_num)
            if motion_num == 18 :
                motion_num = 0
                On_work = 0
                norm_num = 0            
        #btnB_active = exam_button(200,200,btnB_active)
        #실제 버튼 구현 부분!!        
        btnB_active = base_button(20,250,btnB_active)
        btnC_active = ctrl_button(380,10,btnC_active)
        #game_button(30,200)
        
        #pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
        
#게임 구현 부분        
    elif On_norm == 0 and On_game == 1 and not (On_miniGame_stair == 1):
        screen.fill((225,198,53))
        game_button(24,200)
        #screen.blit (stair_space, (800,800))
    elif On_miniGame_stair == 1 and total_stair == 0:
        #drag_ctrlx()
        #drag_ctrly()
        stairs = []
        stairs.append(0)
        imp = 0
        for i in range (1,400):
            imp = make_rand_stair(imp)
            stairs.append(imp)
        total_stair = 8
    elif On_miniGame_stair == 1 and total_stair != 0:
        screen.blit (stair_space, (-230-drag_x//5,-3070-drag_y//5))
        #stairs[x]로 값을 가져올 수 있다.
        for i in range (total_stair-8,total_stair):
            make_stair(stairs[i],i)
            
        #screen.blit (stair_space, (-230,-3070))
        if On_work == 0 :
            screen.blit(slimeB2[0], (178,189))
            screen.blit(slimeE2[0], (178,189))
        #random.randrange(0,1)
        if On_work == 0 :
            key_event = pygame.key.get_pressed()
            if key_event[pygame.K_RIGHT]:
                On_work = 1
            if key_event[pygame.K_LEFT]:
                On_work = 2
                
        '''
        key_event = pygame.key._pressed()
        if key_event[pygame.K_RIGHT]:
            On_work = 1
        if key_event[pygame.K_LEFT]:
            On_work = 2
        '''
        if On_work == 1 :
            motion_num = make_anime_sl_mgjm(motion_num,1)
            if motion_num == 10 :
                motion_num = 0
                On_work = 0
                norm_num = 0
                if (stairs[total_stair-7] - stairs[total_stair-8]) == -1:
                    On_work = 3
                total_stair = total_stair + 1
        if On_work == 2 :
            motion_num = make_anime_sl_mgjm(motion_num,-1)
            if motion_num == 10 :
                motion_num = 0
                On_work = 0
                norm_num = 0
                if (stairs[total_stair-7] - stairs[total_stair-8]) == 1:
                    On_work = 3
                total_stair = total_stair + 1
        if On_work == 3:
            break;
        
    #elif  On_miniGame_Dun == 1 :
    pygame.display.update()    


        
