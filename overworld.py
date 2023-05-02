import map100
import random
import os
from msvcrt import getch

class character:
    def __init__(self, name="",initials="", level=1,x=1,y=1 ):
        self.name = name
        self.level = level
        self.x= x
        self.y= y
        if len(initials) > 2:
            self.initials = initials[0:2]
        elif len(initials) < 2:
            self.initials = initials + " "
        else:
            self.initials = initials

    def levelUp(self):
        self.level +=1


    # if negative move left if positive move right
    # if negative move up if positive move down
    def move_toward(self, other_char):
        dx = other_char.x-self.x 
        dy = other_char.y-self.y

        if dx > 0:
            self.x += 1
        elif dx < 0:
            self.x -= 1

        if dy > 0:
            self.y += 1
        elif dy < 0:
            self.y -= 1

           

main_character= character(input("Please enter your name: "),input("Please enter your initials: "),5,3,3)

boss=character("Boss","bb",10,1,1)

def createNewDot(player, boss):
    a = random.randint(2, 6)
    b = random.randint(2, 6)
    while (a==boss.x and b==boss.y)or(a==player.x and b==player.y ):
        a = random.randint(2, 6)
        b = random.randint(2, 6)
    return a,b    


def overworld():
    curmapg = [[0 for j in range(8)] for i in range(8)] #make map
    curmapc = [[0 for j in range(8)] for i in range(8)] #make map collision
    #curmapd = [[0 for j in range(8)] for i in range(8)] #make dots
    mapid = 100 #tells which map your on
    running = 1 #loop
    a,b = createNewDot(main_character, boss)
   
    round=0
    
    while(running == 1):
        os.system('cls')
        round+=1

        print(f"Round {round}, Current level of {main_character.name} is {main_character.level} ")
        if (mapid == 100): #if mapid is 1
            map100.loadmap(curmapg) #load graphics
            map100.loadmapc(curmapc) #load collision
        curmapg[a][b] = "00" #create dots
        curmapg[main_character.y][main_character.x] = main_character.initials #place player
        curmapg[boss.y][boss.x] = boss.level #place boss
       
        for row in curmapg: #print out map
            for elem in row:
                print(elem, end='')
            print()
        
        if round%2==0:    
            boss.move_toward(main_character) #this makes the boss chase the main character

        if curmapg[main_character.y][main_character.x] == curmapg[boss.y][boss.x] and main_character.level>boss.level:
            print("You won that fight, keep it up!")
            boss.level+=5
        elif curmapg[main_character.y][main_character.x] == curmapg[boss.y][boss.x] and main_character.level==boss.level:
            print("You werent quite ready for that fight, it really took a number on you!")
            main_character.level-=5
        elif curmapg[main_character.y][main_character.x] == curmapg[boss.y][boss.x] and main_character.level<boss.level:
            print("You have been defeated! Try again some other time")
            running==0


        if curmapg[main_character.y][main_character.x] == curmapg[a][b]:
            main_character.levelUp()
            print(f"You collected a dot! {main_character.name}'s level increased to {main_character.level}")
            a,b = createNewDot(main_character, boss)

        print("Use WASD to move")
        travel = chr(ord(getch())) #ask for navigation
        
        if (travel == 'up' and main_character.y == 0): #upnewmap
            newmap= curmapc[0][main_character.x]
            mapid = int(newmap)
            main_character.y = 7

        if (travel == 'w' and main_character.y == 0):
            newmap= curmapc[0][main_character.x]
            mapid = int(newmap)
            main_character.y = 7
            
        if (travel == 'down' and main_character.y == 7): #upnewmap
            newmap= curmapc[7][main_character.x]
            mapid = int(newmap)
            main_character.y = 7

        if (travel == 's' and main_character.y == 7):
            newmap= curmapc[7][main_character.x]
            mapid = int(newmap)
            main_character.y = 0
        
        if (travel == 'up' and main_character.y != 0 and curmapc[main_character.y - 1][main_character.x] != 'C'): #up
            main_character.y -= 1

        if (travel == 'w' and main_character.y != 0 and  curmapc[main_character.y- 1][main_character.x] != 'C'):
            main_character.y -=  1

        if (travel == 'down' and curmapc[main_character.y+ 1][main_character.x] != 'C'): #down
            main_character.y += 1

        if (travel == 's' and curmapc[main_character.y+ 1][main_character.x] != 'C'):
            main_character.y += 1

        if (travel == 'left' and curmapc[main_character.y][main_character.x - 1] != 'C'): #left
            main_character.x -= 1

        if (travel == 'a' and curmapc[main_character.y][main_character.x - 1] != 'C'):
            main_character.x -= 1

        if (travel == 'right' and curmapc[main_character.y][main_character.x + 1] != 'C'): #right
            main_character.x += 1

        if (travel == 'd' and curmapc[main_character.y][main_character.x + 1] != 'C'):
            main_character.x += 1

        if (main_character.level >=100):
            print("You reached the highest level. YOU WIN!")
            running==0
        
overworld()
