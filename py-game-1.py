import pygame
import random
import time




pygame.init()


white=(250,250,250)
red=(250,0,0)
bright_red=(200,0,0)
black=(0,0,0)
green=(0,250,0)
bright_green=(0,200,0)
blue=(0,0,250)






game=pygame.display.set_mode((600,600))

pygame.display.set_caption("KAFSH")

clock=pygame.time.Clock() 


pygame.mixer.music.load("world-m.ogg")
crash_sound=pygame.mixer.Sound("lose-m.wav")






def crash():
    
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)


    font=pygame.font.SysFont(None,80)
    text=font.render("YOU CRASHED",True,black)
    game.blit(text,(50,250))
    #pygame.display.update()
    #time.sleep(2)
    #gameloop()
    while True:


        pygame.draw.rect(game,green,[50,450,70,70])

        font=pygame.font.SysFont(None,23)
        text=font.render("PLAY!",True,black)
        game.blit(text,(52,470))


        pygame.draw.rect(game,red,[450,450,70,70])

        font=pygame.font.SysFont(None,25)
        text=font.render("QUIT",True,black)
        game.blit(text,(460,470))


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()


        a=mouse[0]
        b=mouse[1]
        c=click[0]

        if a>50 and a<120 and b>450 and b<520:
            pygame.draw.rect(game,bright_green,[50,450,70,70])

            font=pygame.font.SysFont(None,23)
            text=font.render("PLAY!",True,black)
            game.blit(text,(52,470))


            if c==1:
                gameloop()
        


        if a>450 and a<520 and b>450 and b<520:
            pygame.draw.rect(game,bright_red,[450,450,70,70])
            
            font=pygame.font.SysFont(None,25)
            text=font.render("QUIT",True,black)
            game.blit(text,(460,470))


            if c==1:
                pygame.quit()
                quit()



        pygame.display.update()









def menu():


    while True:
        game.fill(white)

        
        font=pygame.font.SysFont(None,100)
        text=font.render("LET`S PLAY",True,black)
        game.blit(text,(100,200))



        pygame.draw.rect(game,green,[50,450,70,70])

        font=pygame.font.SysFont(None,23)
        text=font.render("PLAY!",True,black)
        game.blit(text,(52,470))


        pygame.draw.rect(game,red,[450,450,70,70])

        font=pygame.font.SysFont(None,25)
        text=font.render("QUIT",True,black)
        game.blit(text,(460,470))


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()


        a=mouse[0]
        b=mouse[1]
        c=click[0]

        if a>50 and a<120 and b>450 and b<520:
            pygame.draw.rect(game,bright_green,[50,450,70,70])

            font=pygame.font.SysFont(None,23)
            text=font.render("PLAY!",True,black)
            game.blit(text,(52,470))


            if c==1:
                gameloop()
        


        if a>450 and a<520 and b>450 and b<520:
            pygame.draw.rect(game,bright_red,[450,450,70,70])
            
            font=pygame.font.SysFont(None,25)
            text=font.render("QUIT",True,black)
            game.blit(text,(460,470))


            if c==1:
                pygame.quit()
                quit()



        pygame.display.update()















def gameloop():

    pygame.mixer.music.play(-1)

    
    gunx=400
    guny=550

    changegunx=0



    bugx=400
    bugy=-600
    speed_bugy=6

    changebugx=0

    topx=gunx
    topy=550
    speed_topy=0



    score=0
    hitten=0



    while True:

        game.fill(white)
        game.blit(pygame.image.load("Bug.png"),(bugx,bugy))


        game.blit(pygame.image.load("Bug.png"),(gunx,guny))

        
        
        pygame.draw.circle(game,red,(topx,topy),4)



        font=pygame.font.SysFont(None,25)
        text=font.render("SCORE :"+str(score),True,black)
        game.blit(text,(0,0))


        font=pygame.font.SysFont(None,25)
        text=font.render("HITTEN :"+str(hitten),True,green)
        game.blit(text,(0,20))





        if topy==guny:
            topx+=changegunx


        

        bugy=bugy+speed_bugy

        if bugy>600:
            bugy=0
            bugx=random.randrange(0,550)
            score+=1



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    changegunx=5
    
                if event.key==pygame.K_LEFT:
                    changegunx=-5

                if event.key==pygame.K_1:
                    speed_topy=6
                    topx!=gunx


            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                    changebugx=0
                    changegunx=0

        

        if topy<0:
            topy=guny
            topx=gunx
            speed_topy=0


        topy-=speed_topy

        gunx+=changegunx


        if topx>bugx-4 and topx<bugx+52 and topy>bugy-4 and topy<bugy+52:
            bugy=700
            topy=-5
            hitten+=1



        if gunx>600:
            gunx=0

        if gunx<0:
            gunx=600



        if topx>600:
            topx=0

        if topx<0:
            topx=600



        
        if score-hitten==5:
            crash()





        clock.tick(60)
        pygame.display.update()
    

menu()
gameloop()
pygame.quit()
quit()