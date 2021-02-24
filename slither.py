import pygame #imports
import math #needed for sqrt function
import random #needed for randomized integers

pygame.init() #initalizes pygame
pygame.display.set_caption("Slither") #sets up window title
screen = pygame.display.set_mode((400,400)) #creates game screen
clock = pygame.time.Clock() #starts game clock

#game variables
doExit = False

#player 1 variables
xPos = 200
yPos = 200
Vx = 1
Vy = 1

#player 2 variables
xPos2 = 200
yPos2 = 200
Vx2 = 1
Vy2 = 1

#start class pellet+++++++++++++++++++++++++++++++++++++++++++++++++++++
class pellet:
    def __init__(self, xpos, ypos, red, green, blue, radius):
        self.xpos = xpos
        self.ypos = ypos
        self.red = red
        self.green = green
        self.blue = blue
        self.radius = radius
    def collide(self, x, y):
        if math.sqrt((x-self.xpos)*(x-self.xpos)+(y-self.ypos)*(y-self.ypos)) < self.radius + 6:
            self.xpos = random.randrange(20,380)
            self.ypos = random.randrange(20,380)
            self.red = random.randrange(100,240)
            self.green = random.randrange(100,240)
            self.blue = random.randrange(100,240)
            self.radius = random.randrange(5,10)
            return True
    def draw(self):
        pygame.draw.circle(screen, (self.red, self.green, self.blue), (self.xpos, self.ypos), self.radius)
#end class pellet+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#start class tailseg+++++++++++++++++++++++++++++++++++++++++++++++++++++++
class TailSeg:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def update(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen, (250,250,250), (self.xpos, self.ypos), 13)
        pygame.draw.circle(screen, (20,20,20), (self.xpos, self.ypos), 12)
    def collide(self, x, y):
        if math.sqrt((x-self.xpos)*(x-self.xpos)+(y-self.ypos)*(y-self.ypos)) < 6:
            return True

#end class tailseg+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#start class tailseg2+++++++++++++++++++++++++++++++++++++++++++++++++++++++
class TailSeg2:
    def __init__(self, xpos2, ypos2):
        self.xpos2 = xpos2
        self.ypos2 = ypos2
    def update(self, xpos2, ypos2):
        self.xpos2 = xpos2
        self.ypos2 = ypos2
    def draw(self):
        pygame.draw.circle(screen, (20,20,20), (self.xpos2, self.ypos2), 13)
        pygame.draw.circle(screen, (250,250,250), (self.xpos2, self.ypos2), 12)
    def collide(self, x, y):
        if math.sqrt((x-self.xpos2)*(x-self.xpos2)+(y-self.ypos2)*(y-self.ypos2)) < 6:
            return True
#end class tailseg2+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#other variables
oldx = 200
oldy = 200
oldx2 = 200
oldy2 = 200
counter = 0

#list data structures
MyBoisBigBagOfBeans = list()
tail = list()
tail2 = list()

#push 10 pellets into the list
for i in range(10):
    MyBoisBigBagOfBeans.append(pellet(random.randrange(20,380),random.randrange(20,380),random.randrange(100,240),random.randrange(100,240),random.randrange(100,240),random.randrange(5,10)))

#gameloop###############################################################
while not doExit:
    
#event/input section----------------------------------------------------
    clock.tick(60)
    
    for event in pygame.event.get(): #grabs any events (player inputs)
        if event.type == pygame.QUIT: #lets you quit from the game
            doExit = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
            if mousePos[0] > xPos:
                Vx = 1
            else:
                Vx = -1
            if mousePos[1] > yPos:
                Vy = 1
            else:
                Vy = -1
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            Vx2 = 1
        if keys[pygame.K_a]:
            Vx2 = -1
        if keys[pygame.K_s]:
            Vy2 = 1
        if keys[pygame.K_w]:
            Vy2 = -1
                
#physics section--------------------------------------------------------
    counter+=1 #update counter
    if counter == 5: #creates a delay so the tail follows behind
        counter = 0 #reset counter every 5 ticks
        oldx = xPos #hold player 1 pos from 5 ticks ago
        oldy = yPos
        oldx2 = xPos2 #hold player 2 pos from 5 ticks ago
        oldy2 = yPos2
        
        if(len(tail)>1): #dont push numbers if there are no nodes yet
            for i in range (len(tail)): #loop for each slot in list
                #start in LAST position, push the *second to last* into it, repeat til at beginning
                tail[len(tail)-i-1].xpos = tail[len(tail)-i-2].xpos
                tail[len(tail)-i-1].ypos = tail[len(tail)-i-2].ypos
        if(len(tail2)>1): #dont push numbers if there are no nodes yet
            for i in range (len(tail2)): #loop for each slot in list
                #start in LAST position, push the *second to last* into it, repeat til at beginning
                tail2[len(tail2)-i-1].xpos2 = tail2[len(tail2)-i-2].xpos2
                tail2[len(tail2)-i-1].ypos2 = tail2[len(tail2)-i-2].ypos2

        if(len(tail)>0): #if you have at least one segment, push old head position into that
            tail[0].update(oldx, oldy) #push head position into first position of list
        if(len(tail2)>0): #if you have at least one segment, push old head position into that
            tail2[0].update(oldx2, oldy2) #push head position into first position of list
    
    if xPos < 10 or xPos > 390 or yPos < 10 or yPos > 390:
        doExit = True
    if xPos2 < 10 or xPos2 > 390 or yPos2 < 10 or yPos2 > 390:
        doExit = True
    
    xPos += Vx #update p1 circle position
    yPos += Vy
    
    xPos2 += Vx2 #update p2 circle position
    yPos2 += Vy2
    
    for i in range(10):
        if MyBoisBigBagOfBeans[i].collide(xPos, yPos) == True:
            tail.append(TailSeg(oldx, oldy))
        if MyBoisBigBagOfBeans[i].collide(xPos2, yPos2) == True:
            tail2.append(TailSeg2(oldx2, oldy2))
            
    #check if p1 has hit p2s tail:
    for i in range(len(tail2)):
        if tail2[i].collide(xPos,yPos) == True:
            print("p1 hit p2s tail!")
            doExit = True
    #check if p2 has hit p1s tail:
    for i in range(len(tail)):
        if tail[i].collide(xPos2,yPos2) == True:
            print("p2 hit p1s tail!")
            doExit = True
    
#render section---------------------------------------------------------
    screen.fill((60,60,60)) #wipe screen (without this things smear)
    
    for i in range(10):
        MyBoisBigBagOfBeans[i].draw()
    for i in range(len(tail)):
        tail[i].draw()
    for i in range(len(tail2)):
        tail2[i].draw()
    
    pygame.draw.circle(screen, (250,250,250), (xPos, yPos), 13)
    pygame.draw.circle(screen, (20,20,20), (xPos, yPos), 12)

    pygame.draw.circle(screen, (20,20,20), (xPos2, yPos2), 13)
    pygame.draw.circle(screen, (250,250,250), (xPos2, yPos2), 12)

    pygame.display.flip()
    
    
#end game loop##########################################################
    
pygame.quit()