# Import modules
from tkinter import *
import random
import time
from tkinter import font



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
topEnemy=PhotoImage(file="image/helicopter.png")
playerBullet=PhotoImage(file="image/playerbullet.png")
playerBulletTop=PhotoImage(file="image/image.png")
shooter=PhotoImage(file="image/shoot.png")
topEnemyBullet=PhotoImage(file="image/bomb.png")
explosion=PhotoImage(file="image/explosion.png")
life=PhotoImage(file="image/life (2).png")
dead=PhotoImage(file="image/die.png")
win=PhotoImage(file="image/win (2).png")
winText=PhotoImage(file="image/youWin.png")
lost=PhotoImage(file="image/gameOver.gif")
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
POINTS=0
POINTS_TO_WIN=10


ENEMY2_X_START_POSITION = 0
ENEMY2_X_END_POSITION = 960
ENEMY2_Y_START_POSITION = 0
ENEMY2_Y_END_POSITION = 40

ENEMY2_INCREMENT=10

PLAYER_Y_START_POSITION = 350
PLAYER_X_START_POSITION = 120
PLAYER_X_POSITION_INCREMENT = 10
PLAYER_Y_POSITION_INCREMENT = 120

PLAYER_BULLET_POSITION=340
PLAYER_BULLET_INCREMENT=20
ENEMY2_BULLET_X_POSITION=50
ENEMY2_BULLET_Y_POSITION=70


RANDOM_ENEMY_TIME1=random.randrange(2000,4000)

POINTS=0
#---------------------------------------------------------------------------------
# Variables
#---------------------------------------------------------------------------------
player_x = PLAYER_X_START_POSITION
player_y = PLAYER_Y_START_POSITION
player=canvas.create_image(player_x, player_y, image=run,anchor="center")

# enemies
enemy2_X_End=ENEMY2_X_END_POSITION
enemy2_y=ENEMY2_Y_START_POSITION
enemy2_X_Start=ENEMY2_X_START_POSITION
arrayOfEnemiesUp=[]
arrayOfEnemiesRight=[]
# enemies2=canvas.create_image(ENEMY2_X_START_POSITION,enemy2_y,image=topEnemy,anchor="nw",tags="delete")
# Points added

# Bullets Player
arrayOfBulletsEnemy=[]
arrayOfBulletsUp=[]
playerPosition=canvas.coords(player)
bullet_move=PLAYER_BULLET_INCREMENT
pointsDisplay=POINTS


# Bullets Enemy2
startBullet2X=ENEMY2_BULLET_X_POSITION
startBullet2Y=ENEMY2_BULLET_Y_POSITION
# Scores
text=canvas.create_text(525,23,text=pointsDisplay,font=("Purisa",26),fill="red")
# Lives
live=canvas.create_text(40,20,text="LIVES:",fill="red",font=("Purisa",18))
live1=canvas.create_image(80,5,image=life,anchor="nw",tags="lifeOne")
scores=canvas.create_text(450,20,text="SCORES:",fill="red",font=("Purisa",18))
die=0
#---------------------------------------------------------------------------------
# functions
#---------------------------------------------------------------------------------
# Time to win
def winGame():
    global pointsDisplay,die
    if pointsDisplay==POINTS_TO_WIN and die<=3:
        canvas.delete(all)
        canvas.create_image(0,0,image=bg,anchor="nw")
        canvas.create_image(400,300,image=win)
        canvas.create_image(400,120,image=winText)
# Move each individual bombs from top enemies
def bulletEnemies(arrayOfBulletsEenemy):
    global positionEnemies,another1,anotherBullet
    for bullets in arrayOfBulletsEenemy:
        canvas.move(bullets,0,ENEMY2_INCREMENT)
# Create enemy one at a time when an enemy is dead
def addEnemies2():
    global enemies2,positionEnemies,topBullet,arrayOfBulletsEnemy
    positionEnemies=random.randrange(20,850)
    enemies2=canvas.create_image(positionEnemies,80,image=topEnemy,tags="topEn")
    topBullet=canvas.create_image(positionEnemies,80,image=topEnemyBullet,anchor="nw",tags="top")
    arrayOfBulletsEnemy.append(topBullet)
    

# Shoot bullets at enemies when right-click on the mouse
def shootEnemies(event):
    global playerPosition,topShot,arrayOfBulletsUp
    topShot=canvas.create_image(playerPosition[0],PLAYER_BULLET_POSITION,image=playerBulletTop,tags="up")
    arrayOfBulletsUp.append(topShot)
    
# Remove

# Move the player bullet while checking to kill and add points to the scoreboard
def moveBullet():
    global enemies2,topShot,pointsDisplay,arrayOfBulletsUp,topBullet,arrayOfBulletsEnemy
    bulletEnemies(arrayOfBulletsEnemy)
    for bullets in arrayOfBulletsUp:
        winGame()
        canvas.move(bullets,0,-20)
        if len(canvas.coords(bullets))>0:
            if canvas.coords(bullets)[0]>=canvas.coords(enemies2)[0]-40 and canvas.coords(bullets)[0]<=canvas.coords(enemies2)[0]+40 and canvas.coords(bullets)[1]>=canvas.coords(enemies2)[1]-20 and canvas.coords(bullets)[1]<=canvas.coords(enemies2)[1]+20:
                pointsDisplay+=1
                canvas.delete(bullets)
                canvas.delete(enemies2)
                arrayOfBulletsUp.remove(bullets)
                addEnemies2()
                displayScore(pointsDisplay)   
        deadPlay()
    canvas.after(50,moveBullet)
# Change the score when it is added
def displayScore(pointsDisplay):
    canvas.itemconfig(text,text=pointsDisplay)
# Lost
def lostGame():
    canvas.delete(all)
    canvas.create_image(450,300,image=dead)
    canvas.create_image(450,120,image=lost)
# Check for bombs of enemies hitting the player and lost lives
def deadPlay():
    global player,arrayOfBulletsEnemy,die
    posPlayer=canvas.coords(player)
    for bullets in arrayOfBulletsEnemy:
        topBulletPos=canvas.coords(bullets)
        if len(topBulletPos)>0:
            if (topBulletPos[0]-40<=posPlayer[0] and topBulletPos[0]+40>=posPlayer[0] and topBulletPos[1]-40<=posPlayer[1] and topBulletPos[1]+40>=posPlayer[1]):
                die=+1
                canvas.delete(player)
                canvas.delete(bullets)
                canvas.delete(enemies2)
                canvas.delete(topShot)
                canvas.delete("lifeOne")
                lostGame()                
# move left or right
# @param moveRight : if true move right if false move left
def moveHorizontaly(moveRight) :
    global player_x,playerPosition
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

# Start the game
def startGame():
    canvas.delete(all)
    moveBullet()
    addEnemies2()
startGame()

#---------------------------------------------------------------------------------
# bind events
#---------------------------------------------------------------------------------

root.bind("<Left>",movePlayerLeft)
root.bind("<Right>",movePlayerRight)
canvas.bind("<Button-1>",shootEnemies)

canvas.pack(fill="both",expand=True)
root.mainloop()

