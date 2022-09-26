import pygame

pygame.init()

win=pygame.display.set_mode((559,387))

pygame.display.set_caption("Game")

bg= pygame.image.load('background.png')

walkright=pygame.image.load('thief_r.jpg')

walkleft=pygame.image.load('thief_l.jpg')

first=pygame.image.load('thief.jpg')

walkrightp=pygame.image.load('police_r.jpg')

walkleftp=pygame.image.load('police_l.jpg')

firstp=pygame.image.load('police.jpg')

x=150
y=280
width=64
height=64
x_p=50
y_p=280
width_p=64
height_p=64
vel=5
isJump=False
jumpCount=5 
isJumpp=False
jumpCountp=5 

left=False

right=False

leftp=False

rightp=False

walkCount=0

walkCountp=0
v=0

clock= pygame.time.Clock()
run=True

def redrawGameWindow():
    global walkCount
    global walkCountp
    global v
    win.blit(bg,(0,0))
    if walkCount + 1>=27:
        walkCount = 0
    if left:
        win.blit(walkleft,(x,y))
        walkCount+=1
    elif right:
        win.blit(walkright,(x,y))
        walkCount+=1
    else:
        win.blit(first,(x,y))
    if walkCountp + 1>=27:
        walkCountp = 0
    if leftp:
        win.blit(walkleftp,(x_p,y_p))
        walkCountp+=1
    elif rightp:
        win.blit(walkrightp,(x_p,y_p))
        walkCountp+=1
    else:
        win.blit(firstp,(x_p,y_p))

    pygame.display.update()

while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT] and x<559-width-vel:
        x+=vel
        left =False   
        right= True
    elif keys[pygame.K_LEFT] and x> vel:
        x-=vel
        left=True
        right=False
    else:
        right=False
        left =False
        walkCount=0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump=True
            right=False
            left=False
    else:
        if jumpCount>=-5:
            neg=1
            if jumpCount<0:
                neg=-1
            y-=(jumpCount**2)*0.5*neg
            jumpCount-=1
        else:
            isJump=False
            jumpCount=5
        
    if keys[pygame.K_d] and x_p<559-width-vel:
        x_p+=vel
        leftp =False   
        rightp= True
    elif keys[pygame.K_a] and x_p> vel:
        x_p-=vel
        leftp=True
        rightp=False
    else:
        rightp=False
        leftp=False
        walkCountp=0
    if not(isJumpp):
        if keys[pygame.K_w]:
            isJumpp=True
            rightp=False
            leftp=False
    else:
        if jumpCountp>=-5:
            neg=1
            if jumpCountp<0:
                neg=-1
            y_p-=(jumpCountp**2)*0.5*neg
            jumpCountp-=1
        else:
            isJumpp=False
            jumpCountp=5

    if  x_p==x-50:
        break
        
    redrawGameWindow()
pygame.quit()  
    