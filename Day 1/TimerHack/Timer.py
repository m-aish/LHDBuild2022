import pygame,sys,random
from pygame import display,mixer
pygame.init()

#game variables
scrwid=700
scrhei=700
white=(255,255,255)
black=(0,0,0)
green=(173,255,47)
red=(255,0,0)
run =True
button=0
go=False
start_ticks=0
go_ticks=0

y1=250
y2=350
y3=450

clock=pygame.time.Clock()
start_ticks=pygame.time.get_ticks()

#setting up window
win=pygame.display.set_mode((scrwid,scrhei))
pygame.display.set_caption("Get Set Go !")

title=pygame.font.Font("LHD/STEAMED.otf",70)
Title=title.render("Timer",True,black)
title1=pygame.font.Font("LHD/STEAMED.otf",45)
Go=title1.render("Go",True,white)

text=pygame.font.Font("LHD/Chicken.ttf",40)
Text1=text.render("30s",True,black)
Text2=text.render("45s",True,black)
Text3=text.render("60s",True,black)

alarm=pygame.image.load("LHD/alarmicon.png")
img= pygame.transform.smoothscale(alarm, (60,60))

def menu():
    win.fill(white)
    win.blit(Title,(300,100))
    win.blit(img,(220,120))
    pygame.draw.rect(win, black , pygame.Rect(250, y1, 200, 60),2)
    win.blit(Text1,(310,y1-5))
    pygame.draw.rect(win, black , pygame.Rect(250, y2, 200, 60),2)
    win.blit(Text2,(310,y2-5))
    pygame.draw.rect(win, black , pygame.Rect(250, y3, 200, 60),2)
    win.blit(Text3,(310,y3-5))
    #pygame.draw.rect(win, black , pygame.Rect(250, y4, 200, 60),2)
    if (button==1 or button==2 or button==3):
        if button==1:
              pygame.draw.rect(win, green , pygame.Rect(250, y1, 200, 60),0)
        if button==2:
              pygame.draw.rect(win, green , pygame.Rect(250, y2, 200, 60),0)
        if button==3:
            pygame.draw.rect(win, green , pygame.Rect(250, y3, 200, 60),0)
    

    win.blit(Text1,(310,y1-5))
    win.blit(Text2,(310,y2-5))
    win.blit(Text3,(310,y3-5))
    pygame.draw.rect(win, black , pygame.Rect(250, y3+100, 200, 60),0)
    win.blit(Go,(325,y3+95))
    pygame.display.update()
def GOO():
   seconds=(pygame.time.get_ticks()-go_ticks)/1000 
   #print(go_ticks," hush ",seconds)
   while seconds<(button+1)*15:
    win.fill(white)
    count=(button+1)*15
    num=pygame.font.Font("LHD/H.ttf",200)
    n=num.render(str(round(count-seconds)),True,black)
    win.blit(n,(250,200))
    pygame.display.update()
    #print(round(count-seconds))
    seconds=(pygame.time.get_ticks()-go_ticks)/1000 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
   else:
      mixer.init()
      mixer.music.load("LHD/sound.mp3")
      mixer.music.play()
      while True:
       win.fill(white)
       timeup=title.render("Time is up!",True,red)
       win.blit(timeup,(100,200))
       pygame.display.update()
       for event in pygame.event.get():
          if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
       
while run:
    
    clock.tick(100000)
    if go:
        
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
          win.fill(white)
          go_ticks=pygame.time.get_ticks()
          GOO()
    else:
        for event in pygame.event.get():
         if event.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            if((mx>250 and mx<450)and (my>y1 and my<y1+60)):
                     button=1
                     #print(button)
            if((mx>250 and mx<450)and (my>y2 and my<y2+60)):
                     button=2
                     #print(button)
            if((mx>250 and mx<450)and (my>y3 and my<y3+60)):
                     button=3
                     #print(button)  
            if((mx>250 and mx<450)and (my>y3+95 and my<y3+95+60)):
                go=True
                #print("Go") 
         if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        menu()          
      
        