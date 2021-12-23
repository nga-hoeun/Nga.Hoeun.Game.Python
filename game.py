# Import modules
from tkinter import *
import random



#---------------------------------------------------------------------------------
# GRAPHIC WINDOW
#---------------------------------------------------------------------------------

# Create root
root=Tk()
# Adjust size
root.geometry("960x540")
# Add image file
bg=PhotoImage(file="image/background.gif")
run=PhotoImage(file="image/run.png")
enemy=PhotoImage(file="image/soldier.png")
topEnemy=PhotoImage(file="image/helicopter.png")
playerBullet=PhotoImage(file="image/bulletPlayer.png")
shooter=PhotoImage(file="image/shoot.png")

# Create frame
frame=Frame()
frame.master.title("Nga Hoeun Game Project")
frame.pack(fill="both",expand=True)

# Create canvas
canvas=Canvas(frame)

# background
background=canvas.create_image(0,0,image=bg,anchor="nw")


#---------------------------------------------------------------------------------
# Constants
#---------------------------------------------------------------------------------

ENEMY1_X_START_POSITION = 850
ENEMY1_Y_START_POSITION = 300

ENEMY2_X_START_POSITION = 0
ENEMY2_X_END_POSITION = 960
ENEMY2_Y_START_POSITION = 0
ENEMY2_Y_END_POSITION = 40

ENEMY2_INCREMENT= 20
ENEMY1_INCREMENT=-20

PLAYER_Y_START_POSITION = 350
PLAYER_X_START_POSITION = 120
PLAYER_X_POSITION_INCREMENT = 10
PLAYER_Y_POSITION_INCREMENT = 120

PLAYER_BULLET_POSITION=340
PLAYER_BULLET_INCREMENT=20

#---------------------------------------------------------------------------------
# Variables
#---------------------------------------------------------------------------------
player_x = PLAYER_X_START_POSITION
player_y = PLAYER_Y_START_POSITION
player=canvas.create_image(player_x, player_y, image=run,anchor="center")

# enemies
enemy1_x=ENEMY1_X_START_POSITION
enemies=canvas.create_image(enemy1_x, ENEMY1_Y_START_POSITION, image=enemy,anchor="nw",tags="gone")
enemy2_y=ENEMY2_Y_START_POSITION
enemy2_X_End=ENEMY2_X_END_POSITION
enemy2_X_Start=ENEMY2_X_START_POSITION
enemies2=canvas.create_image(ENEMY2_X_START_POSITION,enemy2_y,image=topEnemy,anchor="nw",tags="delete")

# Bullets
playerPosition=canvas.coords(player)
bullet_move=PLAYER_BULLET_INCREMENT

#---------------------------------------------------------------------------------
# functions
#---------------------------------------------------------------------------------
# Bullets for players
def shootEnemies(event):
    global playerPosition
    playerShot=canvas.create_image(playerPosition[0],PLAYER_BULLET_POSITION,image=playerBullet,tags="shot")
    playerBulletMovement()


def playerBulletMovement():
    global playerPosition
    global bullet_move
    bullet_X=playerPosition
    if bullet_X[0]<ENEMY2_X_END_POSITION:
        # canvas.move(,bullet_X[0],0)
        canvas.after(20,playerBulletMovement)
    else:
        canvas.delete("shot")



# move left or right
# @param moveRight : if true move right if false move left
def moveHorizontaly(moveRight) :
    global player_x
    global playerPosition
    if moveRight:
        new_player_x = player_x + PLAYER_X_POSITION_INCREMENT
    else:
        new_player_x = player_x - PLAYER_X_POSITION_INCREMENT

    if new_player_x>=60 and new_player_x<900:
        player_x = new_player_x
        canvas.itemconfig(player, canvas.coords(player,player_x ,player_y))
    playerPosition[0]=new_player_x
    print(playerPosition)

def movePlayerRight(event):
    moveHorizontaly(True)

def movePlayerLeft(event):
    moveHorizontaly(False)


def jumpPlayer(event) :
    go_up()

def go_up():
    global player_y

    new_player_y = player_y - 1
     
    if new_player_y > PLAYER_Y_START_POSITION - PLAYER_Y_POSITION_INCREMENT:
        player_y = new_player_y
        canvas.itemconfig(player, canvas.coords(player,player_x ,player_y))
        canvas.after(1,go_up)

    else :
        go_down()


def go_down():
    global player_y

    new_player_y = player_y + 1
     
    if new_player_y < PLAYER_Y_START_POSITION:
        player_y = new_player_y
        canvas.itemconfig(player, canvas.coords(player,player_x ,player_y))
        canvas.after(1,go_down)



def movingEnemies():
    global enemy1_x
    if enemy1_x>0:
        canvas.move(enemies,ENEMY1_INCREMENT,0)
        canvas.after(100,movingEnemies)
        enemy1_x+=ENEMY1_INCREMENT
    else:
        canvas.delete("gone")
movingEnemies()
    

def movingAirplane():
    global enemy2_y,enemy2_X_End,enemy2_X_Start
    if enemy2_X_Start < enemy2_X_End-100:
        if enemy2_y<ENEMY2_Y_END_POSITION:
            move_y_down=random.randrange(0,40)
            canvas.move(enemies2,ENEMY2_INCREMENT,move_y_down)
            enemy2_y+=move_y_down
            canvas.after(100,movingAirplane)
        elif enemy2_y>=ENEMY2_Y_START_POSITION:
            move_y_up=random.randrange(-40,0)
            canvas.move(enemies2,ENEMY2_INCREMENT,move_y_up)
            enemy2_y+=move_y_up
            canvas.after(100,movingAirplane)
        enemy2_X_Start+=ENEMY2_INCREMENT
    else:
        canvas.delete("delete")
movingAirplane()
# Shooting
# def shootTime(event):
#     positionPlayer=canvas.coords(player)
#     playerShot=canvas.create_image(positionPlayer[0],340,image=playerBullet,tags="shot")
#     print(positionPlayer)




#---------------------------------------------------------------------------------
# bind events
#---------------------------------------------------------------------------------

root.bind("<Left>",movePlayerLeft)
root.bind("<Right>",movePlayerRight)
root.bind("<Up>",jumpPlayer)
root.bind("<w>",shootEnemies)

canvas.pack(fill="both",expand=True)
root.mainloop()

