# Import modules
from tkinter import *
import random
# Create object
root=Tk()
# Adjust size
root.geometry("960x540")
# Add image file
bg=PhotoImage(file="image/background.gif")
shooter=PhotoImage(file="image/run.png")
enemy=PhotoImage(file="image/soldier.png")
topEnemy=PhotoImage(file="image/helicopter.png")
playerBullet=PhotoImage(file="image/bulletPlayer.png")
# Create frame
frame=Frame()
frame.master.title("Nga Hoeun Game Project")
frame.pack(fill="both",expand=True)
# Create canvas
canvas=Canvas(frame)
# background
background=canvas.create_image(0,0,image=bg,anchor="nw")
# Constants Variable
startPos=60
add=10
yCoordinate=350
counterLevelPass=1
# player
player=canvas.create_image(startPos,yCoordinate,image=shooter,anchor="center")
def movePlayerRight(event):
    global startPos,yCoordinate,add
    if startPos>=60 and startPos<900:
        canvas.itemconfig(player, canvas.coords(player,startPos+add,yCoordinate))
        startPos+=add
    yCoordinate=350
def movePlayerLeft(event):
    global startPos,yCoordinate,add
    if startPos<=900 and startPos>60:
        canvas.itemconfig(player,canvas.coords(player,startPos-add,350))
        startPos-=add
    yCoordinate=350
def jump(event):
    global yCoordinate
    canvas.after(250)
    if yCoordinate==350:
        canvas.move(player,0,-100)
        yCoordinate-=100
# enemies
enemyPos=850
enemies=canvas.create_image(enemyPos,300,image=enemy,anchor="nw")
def movingEnemies():
    global enemyPos
    canvas.move(enemies,-20,0)
    canvas.after(100,movingEnemies)
movingEnemies()
topPos=0
enemies2=canvas.create_image(0,topPos,image=topEnemy,anchor="nw")
def movingAirplane():
    global topPos
    if topPos<40:
        posTop=random.randrange(0,40)
        canvas.move(enemies2,20,posTop)
        topPos+=posTop
        canvas.after(100,movingAirplane)
    elif topPos>=0:
        posTop=random.randrange(-40,0)
        canvas.move(enemies2,20,posTop)
        topPos+=posTop
        canvas.after(100,movingAirplane)
movingAirplane()
# Shooting
playerShot=canvas.create_image()
def shootStraight(event):
    position=canvas.coords(player)
canvas.pack(fill="both",expand=True)
root.bind("<Left>",movePlayerLeft)
root.bind("<Right>",movePlayerRight)
root.bind("<Up>",jump)
root.mainloop()