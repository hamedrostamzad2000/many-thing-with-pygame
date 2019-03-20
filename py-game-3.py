import pygame
import random
import time

pygame.init()

pygame.mixer.music.load("world-m.ogg")
#pygame.mixer.music.load("MasoudSadeghloo-ZireBaroonaBeraghs-320(www.Next1.ir).mp3")
#pygame.mixer.music.load("Arash - Tekoon Bede (128).mp3")
crash_sound=pygame.mixer.Sound("lose-m.wav")

white=(250,250,250)
red=(250,0,0)
bright_red=(200,0,0)
black=(0,0,0)
green=(0,250,0)
bright_green=(0,200,0)





def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()
  

def massage_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',70)
    textSurf,textRect=text_objects(text,largetext)
    textRect.center=((width/2),(height/2))
    game.blit(textSurf,textRect)
    pygame.display.update()

    #time.sleep(2)
    
    





def crash():
    massage_display('YOU CRASHED')
    
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)


    menuvasat=True

    while True:
    
        

        

        pygame.draw.rect(game,green,[50,500,50,50])
        pygame.draw.rect(game,red,[450,500,50,50])

        font=pygame.font.SysFont(None,20)
        text=font.render("TRY AGAIN",True,black)
        game.blit(text,(50,520))


        font=pygame.font.SysFont(None,25)
        text=font.render("QUIT",True,black)
        game.blit(text,(455,520))


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        d=mouse[0]
        e=mouse[1]
        f=click[0]

        if d>50 and d<100 and e>500 and e<550:
            pygame.draw.rect(game,bright_green,[50,500,50,50])

            font=pygame.font.SysFont(None,20)
            text=font.render("TRY AGAIN",True,black)
            game.blit(text,(50,520))
    
            if f==1:
                gameloop()

        
        if d>450 and d<500 and e>500 and e<550:

            pygame.draw.rect(game,bright_red,[450,500,50,50])

            font=pygame.font.SysFont(None,25)
            text=font.render("QUIT",True,black)
            game.blit(text,(455,520))
    
            if f==1:
                pygame.quit()
                quit()

        pygame.display.update()
    
    













width=600
height=600

game=pygame.display.set_mode((width,height))

pygame.display.set_caption('MORABBAA BAZY')



clock=pygame.time.Clock()







def menu():
   
    game.fill(white)
    start=False
        
    while not False:


        pygame.draw.rect(game,green,[50,500,50,50])
        pygame.draw.rect(game,red,[450,500,50,50])
        game.blit(pygame.font.SysFont(None,120).render("LET`S GO ",True,black),(40,300))

        font =pygame.font.SysFont(None,24)
        text=font.render("PLAY!",True,black)
        game.blit(text,(50,525))


        font=pygame.font.SysFont(None,24)
        text=font.render("QUIT",True,black)
        game.blit(text,(455,525))

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        a=mouse[0]
        b=mouse[1]
        c=click[0]

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                start=True
                pygame.quit()
                quit()
                    
            
            
            
                
        if a >50 and a <100 and b >500 and b <550:
            pygame.draw.rect(game,bright_green,[50,500,50,50])
            font =pygame.font.SysFont(None,24)
            text=font.render("PLAY!",True,black)
            game.blit(text,(50,525))
            if c == 1:
                gameloop()
                            
        if a>450 and a<500 and b>500 and b<550:
            pygame.draw.rect(game,bright_red,[450,500,50,50])
            font=pygame.font.SysFont(None,24)
            text=font.render("QUIT",True,black)
            game.blit(text,(455,525))
            if c==1:
                pygame.quit()
                quit()

                    
            
        pygame.display.update()









def gameloop():

    pygame.mixer.music.play(-1)

    gameExit=False

    instagramx=100
    instagramy=-600
    speed_instagramy=6
    instagramw=100

    z=0
    

    bugx=300
    bugy=500
    changebugx=0
    changebugy=0


    while not False:

        
        game.fill(white)
        
        #font=pygame.font.SysFont(None,25)
        #text=font.render("score :",True,red)
        #game.blit(text,(0,0))
        
        game.blit(pygame.font.SysFont(None,25).render("SCORE :"+str(z),True,red),(0,0))
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameExit=True
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changebugx=changebugx-5
                if event.key == pygame.K_RIGHT:
                    changebugx=changebugx+5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    changebugx=0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    changebugy=changebugy-1
                if event.key == pygame.K_DOWN:
                    changebugy=changebugy+1
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changebugy=0



        bugx=bugx+changebugx
        bugy=bugy+changebugy


        pygame.draw.rect(game,red,[instagramx,instagramy,instagramw,100])
        car=game.blit(pygame.image.load("bug.png"),(bugx,bugy))
        instagramy=instagramy+speed_instagramy
        
        if instagramy>height:
            instagramy=0
            instagramx=random.randrange(0,400)
            instagramw=random.randrange(100,200)
            speed_instagramy=speed_instagramy+0.3
            z=z+1



        if bugx<0 or bugx>width-48 or bugy<0  or bugy>height-48:
            crash()
            


        if bugx>=instagramx-48 and bugx<=instagramx+instagramw and bugy<=instagramy+100 and bugy>=instagramy:
            crash()
            


        clock.tick(120)
        pygame.display.update()



menu()

gameloop()
pygame.quit()
quit()