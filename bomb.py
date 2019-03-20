import pygame
import random
import time

pygame.init()






game=pygame.display.set_mode((160,500))

pygame.display.set_caption("BOMB")

    

pygame.mixer.music.load("Arash - Tekoon Bede (128).mp3")




b=[0,250]

black=(0,0,0)
tosy=(150,150,150)
white=(250,250,250)
bright_tosy=(200,200,200)
green=(0,250,0)
bright_green=(0,200,0)
red=(250,0,0)
bright_red=(200,0,0)






def menu():
    

    while True:

        game.fill(white)


        font=pygame.font.SysFont(None,18)
        text=font.render("GREEN :+3  YELLOW :+1",True,black)
        game.blit(text,(10,100))




        font=pygame.font.SysFont(None,18)
        text=font.render("BLACK :-3     RED :-1",True,black)
        game.blit(text,(12,120))




        font=pygame.font.SysFont(None,18)
        text=font.render("SCOPE>= 8   =>YOU WON",True,black)
        game.blit(text,(12,140))






        font=pygame.font.SysFont(None,16)
        text=font.render("SCOPE<= -8   =>YOU FAILED",True,black)
        game.blit(text,(6,160))






        pygame.draw.rect(game,green,[55,250,50,50])


        font=pygame.font.SysFont(None,25)
        text=font.render("PLAY",True,black)
        game.blit(text,(57,275))



        pygame.draw.rect(game,red,[55,320,50,50])


        font=pygame.font.SysFont(None,25)
        text=font.render("QUIT",True,black)
        game.blit(text,(59,345))


        


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        a=mouse[0]
        d=mouse[1]
        c=click[0]




        if a>55 and a<105 and d>250 and d<300:
            pygame.draw.rect(game,bright_green,[55,250,50,50])
            font=pygame.font.SysFont(None,25)
            text=font.render("PLAY",True,black)
            game.blit(text,(57,275))

            if c==1:
                gameloop()






        if a>55 and a<105 and d>320 and d<370:

            pygame.draw.rect(game,bright_red,[55,320,50,50])

            font=pygame.font.SysFont(None,25)
            text=font.render("QUIT",True,black)
            game.blit(text,(59,345))

            if c==1:
                pygame.quit()
                quit()
               






        pygame.display.update()









def fail():
    #pygame.display.update()
    #time.sleep(2)
    #gameloop()

    pygame.mixer.music.stop()
    while True:

        game.fill(white)

        font=pygame.font.SysFont(None,30)
        text=font.render("YOU FAILED",True,red)
        game.blit(text,(10,100))





        pygame.draw.rect(game,green,[55,250,50,50])


        font=pygame.font.SysFont(None,17)
        text=font.render("TRY AGAIN",True,black)
        game.blit(text,(57,275))



        pygame.draw.rect(game,red,[55,320,50,50])


        font=pygame.font.SysFont(None,25)
        text=font.render("QUIT",True,black)
        game.blit(text,(59,345))


        


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        a=mouse[0]
        d=mouse[1]
        c=click[0]




        if a>55 and a<105 and d>250 and d<300:
            pygame.draw.rect(game,bright_green,[55,250,50,50])
            font=pygame.font.SysFont(None,17)
            text=font.render("TRY AGAIN",True,black)
            game.blit(text,(57,275))

            if c==1:
                gameloop()






        if a>55 and a<105 and d>320 and d<370:

            pygame.draw.rect(game,bright_red,[55,320,50,50])

            font=pygame.font.SysFont(None,25)
            text=font.render("QUIT",True,black)
            game.blit(text,(59,345))

            if c==1:
                pygame.quit()
                quit()
               






        pygame.display.update()





def success():
    #pygame.display.update()
    #time.sleep(2)
    #gameloop()

    pygame.mixer.music.stop()
    while True:

        game.fill(white)

        font=pygame.font.SysFont(None,40)
        text=font.render("YOU WON",True,green)
        game.blit(text,(10,100))





        pygame.draw.rect(game,green,[55,250,50,50])


        font=pygame.font.SysFont(None,17)
        text=font.render("TRY AGAIN",True,black)
        game.blit(text,(57,275))



        pygame.draw.rect(game,red,[55,320,50,50])


        font=pygame.font.SysFont(None,25)
        text=font.render("QUIT",True,black)
        game.blit(text,(59,345))


        


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        a=mouse[0]
        d=mouse[1]
        c=click[0]




        if a>55 and a<105 and d>250 and d<300:
            pygame.draw.rect(game,bright_green,[55,250,50,50])
            font=pygame.font.SysFont(None,17)
            text=font.render("TRY AGAIN",True,black)
            game.blit(text,(57,275))

            if c==1:
                gameloop()






        if a>55 and a<105 and d>320 and d<370:

            pygame.draw.rect(game,bright_red,[55,320,50,50])

            font=pygame.font.SysFont(None,25)
            text=font.render("QUIT",True,black)
            game.blit(text,(59,345))

            if c==1:
                pygame.quit()
                quit()
               






        pygame.display.update()













def gameloop():

    pygame.mixer.music.play(-1)



    rang29=rang27=rang25=rang23=rang21=rang19=rang17=rang15=rang13=rang11=rang9=rang7=rang5=rang3=rang1=bright_tosy
    rang30=rang28=rang26=rang24=rang22=rang20=rang18=rang16=rang14=rang12=rang10=rang8=rang6=rang2=rang4=tosy




    changescore=0
    changescore15=0
    score=0



    while True:

        game.fill(white)


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    score+=changescore



        pygame.draw.rect(game,rang1,[0,0,50,50])

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        a=mouse[0]
        d=mouse[1]
        c=click[0]

        #rang=b[0]

        if a>0 and a<50 and d>0 and d<50:
            pygame.draw.rect(game,rang2,[0,0,50,50])
            if c==1:
                #rand=False

                #while not rand:

                i=random.randrange(0,2)
                j=random.randrange(0,2)

                    #if i!=j:
                        #rand=True

                b=[0,250]
                rang2=rang1=(b[i],b[j],0)

                pygame.draw.rect(game,rang1,[0,0,50,50])
                
                if rang1==(250,0,0):
                    changescore=-1
                if rang1==(250,250,0):
                    changescore=1
                if rang1==(0,250,0):
                    changescore=3
                if rang1==(0,0,0):
                    changescore=-3









        pygame.draw.rect(game,rang3,[54,0,50,50])

        if a>54 and a<104 and d>0 and d<50:
                pygame.draw.rect(game,rang4,[54,0,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang4=rang3=(b[i],b[j],0)


                    pygame.draw.rect(game,rang3,[54,0,50,50])

                    if rang3==(250,0,0):
                        changescore=-1
                    if rang3==(250,250,0):
                        changescore=1
                    if rang3==(0,250,0):
                        changescore=3
                    if rang3==(0,0,0):
                        changescore=-3









        pygame.draw.rect(game,rang5,[108,0,50,50])

        if a>108 and a<158 and d>0 and d<50:
                pygame.draw.rect(game,rang6,[108,0,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang6=rang5=(b[i],b[j],0)


                    pygame.draw.rect(game,rang5,[108,0,50,50])

                    if rang5==(250,0,0):
                        changescore=-1
                    if rang5==(250,250,0):
                        changescore=1
                    if rang5==(0,250,0):
                        changescore=3
                    if rang5==(0,0,0):
                        changescore=-3









        pygame.draw.rect(game,rang7,[0,54,50,50])

        if a>0 and a<50 and d>54 and d<104:
                pygame.draw.rect(game,rang8,[0,54,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang8=rang7=(b[i],b[j],0)


                    pygame.draw.rect(game,rang7,[0,54,50,50])

                    if rang7==(250,0,0):
                        changescore=-1
                    if rang7==(250,250,0):
                        changescore=1
                    if rang7==(0,250,0):
                        changescore=3
                    if rang7==(0,0,0):
                        changescore=-3









        pygame.draw.rect(game,rang9,[54,54,50,50])

        if a>54 and a<104 and d>54 and d<104:
                pygame.draw.rect(game,rang10,[54,54,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang10=rang9=(b[i],b[j],0)


                    pygame.draw.rect(game,rang9,[54,54,50,50])

                    if rang9==(250,0,0):
                        changescore=-1
                    if rang9==(250,250,0):
                        changescore=1
                    if rang9==(0,250,0):
                        changescore=3
                    if rang9==(0,0,0):
                        changescore=-3











        pygame.draw.rect(game,rang11,[108,54,50,50])

        if a>108 and a<158 and d>54 and d<104:
                pygame.draw.rect(game,rang12,[108,54,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang12=rang11=(b[i],b[j],0)


                    pygame.draw.rect(game,rang11,[108,54,50,50])

                    if rang11==(250,0,0):
                        changescore=-1
                    if rang11==(250,250,0):
                        changescore=1
                    if rang11==(0,250,0):
                        changescore=3
                    if rang11==(0,0,0):
                        changescore=-3














        pygame.draw.rect(game,rang13,[0,108,50,50])

        if a>0 and a<50 and d>108 and d<158:
                pygame.draw.rect(game,rang14,[0,108,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang14=rang13=(b[i],b[j],0)


                    pygame.draw.rect(game,rang13,[0,108,50,50])

                    if rang13==(250,0,0):
                        changescore=-1
                    if rang13==(250,250,0):
                        changescore=1
                    if rang13==(0,250,0):
                        changescore=3
                    if rang13==(0,0,0):
                        changescore=-3












        pygame.draw.rect(game,rang15,[54,108,50,50])

        if a>54 and a<104 and d>108 and d<158:
                pygame.draw.rect(game,rang16,[54,108,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang16=rang15=(b[i],b[j],0)


                    pygame.draw.rect(game,rang15,[54,108,50,50])

                    if rang15==(250,0,0):
                        changescore=-1
                    if rang15==(250,250,0):
                        changescore=1
                    if rang15==(0,250,0):
                        changescore=3
                    if rang15==(0,0,0):
                        changescore=-3











        pygame.draw.rect(game,rang17,[108,108,50,50])

        if a>108 and a<158 and d>108 and d<158:
                pygame.draw.rect(game,rang18,[108,108,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang18=rang17=(b[i],b[j],0)


                    pygame.draw.rect(game,rang17,[108,108,50,50])

                    if rang17==(250,0,0):
                        changescore=-1
                    if rang17==(250,250,0):
                        changescore=1
                    if rang17==(0,250,0):
                        changescore=3
                    if rang17==(0,0,0):
                        changescore=-3












        pygame.draw.rect(game,rang19,[0,162,50,50])

        if a>0 and a<50 and d>162 and d<212:
                pygame.draw.rect(game,rang20,[0,162,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang20=rang19=(b[i],b[j],0)


                    pygame.draw.rect(game,rang19,[0,162,50,50])

                    if rang19==(250,0,0):
                        changescore=-1
                    if rang19==(250,250,0):
                        changescore=1
                    if rang19==(0,250,0):
                        changescore=3
                    if rang19==(0,0,0):
                        changescore=-3













        pygame.draw.rect(game,rang21,[54,162,50,50])

        if a>54 and a<104 and d>162 and d<212:
                pygame.draw.rect(game,rang22,[54,162,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang22=rang21=(b[i],b[j],0)


                    pygame.draw.rect(game,rang21,[54,162,50,50])

                    if rang21==(250,0,0):
                        changescore=-1
                    if rang21==(250,250,0):
                        changescore=1
                    if rang21==(0,250,0):
                        changescore=3
                    if rang21==(0,0,0):
                        changescore=-3













        pygame.draw.rect(game,rang23,[108,162,50,50])

        if a>108 and a<158 and d>162 and d<212:
                pygame.draw.rect(game,rang24,[108,162,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang24=rang23=(b[i],b[j],0)


                    pygame.draw.rect(game,rang23,[108,162,50,50])

                    if rang23==(250,0,0):
                        changescore=-1
                    if rang23==(250,250,0):
                        changescore=1
                    if rang23==(0,250,0):
                        changescore=3
                    if rang23==(0,0,0):
                        changescore=-3













        pygame.draw.rect(game,rang25,[0,216,50,50])

        if a>0 and a<50 and d>216 and d<266:
                pygame.draw.rect(game,rang26,[0,216,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang26=rang25=(b[i],b[j],0)


                    pygame.draw.rect(game,rang25,[0,216,50,50])

                    if rang25==(250,0,0):
                        changescore=-1
                    if rang25==(250,250,0):
                        changescore=1
                    if rang25==(0,250,0):
                        changescore=3
                    if rang25==(0,0,0):
                        changescore=-3













        pygame.draw.rect(game,rang27,[54,216,50,50])

        if a>54 and a<104 and d>216 and d<266:
                pygame.draw.rect(game,rang28,[54,216,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang28=rang27=(b[i],b[j],0)


                    pygame.draw.rect(game,rang27,[54,216,50,50])

                    if rang27==(250,0,0):
                        changescore=-1
                    if rang27==(250,250,0):
                        changescore=1
                    if rang27==(0,250,0):
                        changescore=3
                    if rang27==(0,0,0):
                        changescore=-3













        pygame.draw.rect(game,rang29,[108,216,50,50])
    
        if a>108 and a<158 and d>216 and d<266:
                pygame.draw.rect(game,rang30,[108,216,50,50])
                if c==1:
                    

                    i=random.randrange(0,2)
                    j=random.randrange(0,2)

                        

                    b=[0,250]
                    rang30=rang29=(b[i],b[j],0)


                    pygame.draw.rect(game,rang29,[108,216,50,50])
                    if rang29==(250,0,0):
                        changescore=-1
                    if rang29==(250,250,0):
                        changescore=1
                    if rang29==(0,250,0):
                        changescore=3
                    if rang29==(0,0,0):
                        changescore=-3


                    





        
        




        font=pygame.font.SysFont(None,25)
        text=font.render("SCORE :"+str(score),True,black)
        game.blit(text,(50,275))






        if score<=-8:
            fail()
            

        if score>=8:
            success()







        pygame.display.update()







menu()


pygame.quit()
quit()

