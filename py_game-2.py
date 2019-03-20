import pygame
import time
import random

pygame.init()

width=800
height=600


white=(250,250,250)
black=(0,0,0)
red=(250,0,0)



gameDisplay=pygame.display.set_mode((width,height))

pygame.display.set_caption('RACE CAR')

clock = pygame.time.Clock()


carImg=pygame.image.load("Bug.png")



def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()
  

def massage_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',90)
    textSurf,textRect=text_objects(text,largetext)
    textRect.center=((width/2),(height/2))
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()





def crash():
    massage_display('YOU CRASHED')
      


def stuff(stuffx,stuffy,stuffw,stuffh,color):
    pygame.draw.rect(gameDisplay,color,[stuffx,stuffy,stuffw,stuffh])






def game_loop():
    x=width * 0.4
    y=width * 0.3

    x_change=0
    y_change=0
    

    stuff_startx=random.randrange(0,width)
    stuff_starty=-600
    stuff_width=100
    stuff_height=100
    stuff_speed=7


    gameExit=False

    while not gameExit: 

    
    
        gameDisplay.fill(white)
        car(x,y)
        
        

        
        
        stuff(stuff_startx,stuff_starty,stuff_width,stuff_height,red)
        stuff_starty=stuff_starty + stuff_speed
        if stuff_starty>height:
            stuff_starty=0 - stuff_height
            stuff_startx=random.randrange(0,width)
            




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                  x_change=-5
                if event.key == pygame.K_RIGHT:
                  x_change=5
                
                if event.key == pygame.K_UP:
                    y_change=-5
                
                if event.key == pygame.K_DOWN:
                    y_change=5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change=0     
            
        if x>width - 48  or  x<0:
            crash()    
        if y>height-48 or y<0:
            crash()

        x=x_change+x
        y=y_change+y
        clock.tick(60) 
        pygame.display.update()








game_loop()
pygame.quit()
quit()