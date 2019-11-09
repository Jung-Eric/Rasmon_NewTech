import sys
import pygame
import spritesheet
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
slimetu = (56,39,47)
slimetu2 = (58,41,49)

slimeE = []
for i in range(0,16):
    slimeE.append(s2.image_at((1+slimetu2[0]*(i+1), 1, slimetu[0] , slimetu[1])))
    slimeE[i] = pygame.transform.scale(slimeE[i],(slimetu[0]*3,slimetu[1]*3))
for i in range(0,17):
    slimeE.append(s2.image_at((1+slimetu2[0]*i, 1+slimetu2[1], slimetu[0] , slimetu[1])))
    slimeE[i+16] = pygame.transform.scale(slimeE[i+16],(slimetu[0]*3,slimetu[1]*3))

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
    
slimeJM = []
for i in range(0,8):
    slimeJM.append(s2.image_at((1+slimetu2[0]*(i+5), 1+slimetu2[1]*2, slimetu[0] , slimetu[2])))
    slimeJM[i] = pygame.transform.scale(slimeJM[i],(slimetu[0]*3,slimetu[2]*3))


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
#우주 3426 911
dun_space = s5.image_at((1,1,911,3426))

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
#-------------------------------------------------------------------
#실질 구현
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 1
        #emotion = emotion * -1
    if key_event[pygame.K_RIGHT]:
        pos_x += 1
        #emotion = emotion * -1
    if key_event[pygame.K_UP]:
        pos_y -= 1
        #emotion = emotion * -1
    if key_event[pygame.K_DOWN]:
        pos_y += 1
        #emotion = emotion * -1
        
    #screen.fill(black)
    screen.blit(base[0], (0,0))
    '''
    screen.blit(slime2, (50,50))
    if emotion == -1:
        screen.blit(slimeE2, (50,50))
    else:
        screen.blit(slimeEE2, (50,50))
    #screen.blit(image33, (100,100))
    '''
    pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
    pygame.display.update()
