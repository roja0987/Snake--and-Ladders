import tkinter as t
from PIL import ImageTk ,Image
import random
from gtts import gTTS
from playsound import playsound
'''import pygame
print(pygame.__version__)'''
import os
def Speak(Text):
    obj=gTTS(text=Text,lang='en',slow=False)
    obj.save('Text.mp3')
    playsound('Text.mp3')
    os.remove('Text.mp3')
def start_game():
    global b1,b2
    #player1
    b1.place(x=950,y=300)
    #player 2
    b2.place(x=950,y=400)
    #Dice
    dice_image=Image.open("dice.png")
    resized_dice_image=dice_image.resize((65,65),Image.Resampling.LANCZOS)
    images['dice']=ImageTk.PhotoImage(resized_dice_image)
    b4=t.Button(window,image=images['dice'],height=80,width=80)
    b4.place(x=950,y=200)
    #exit button
    b3=t.Button(window,text="Click here to End the Game !",height=2,width=25,fg="red",bg="yellow",font=('Arial',12),activebackground='cyan',command=window.destroy)
    b3.place(x=950,y=700)
def reset_coins():
    global player_1,player_2,Index
    global pos1,pos2
    player_1.place(x=0,y=600)
    player_2.place(x=40,y=600)
    pos1=0
    pos2=0
def load_dice_images():
    global Dice
    names=["1.png","2.png","3.png","4.png","5.png","6.png"]
    for nam in names:
        im=Image.open(nam)
        im=im.resize((65,65))
        im=ImageTk.PhotoImage(im)
        Dice.append(im)
def check_ladder(Turn):
    global pos1,pos2
    global ladder
    f=0 # no laddder
    if(Turn==1):
        if pos1 in ladder:
            pos1=ladder[pos1]
            f=1
    else:
        if pos2 in ladder:
            pos2=ladder[pos2]
            f=1
    return f
def check_snake(Turn):
    global pos1,pos2
    global snake
    if(Turn==1):
        if pos1 in snake:
            pos1=snake[pos1]
    else:
        if pos2 in snake:
            pos2=snake[pos2]
def roll_dice():
    global Dice
    global turn
    global pos1,pos2
    global b1,b2
    r=random.randint(1,6)
    b4=t.Button(window,image=Dice[r-1],height=80,width=80)
    b4.place(x=950,y=200)
   #Speak(str(r))
    lad=0 # no ladder intilally
    if turn==1:
        if (pos1+r)<=100:
             pos1=pos1+r
        lad=check_ladder(turn)
        check_snake(turn)
        move_coin(turn,pos1)
        if r!=6 and lad!=1 :
             turn=2
             b1.configure(state='disabled')
             b2.configure(state='normal')
    else:
        if(pos2+r)<=100:
             pos2=pos2+r
        lad=check_ladder(turn)
        check_snake(turn)
        move_coin(turn ,pos2) 
        if r!=6 and lad!=1:
            turn=1;
            b1.configure(state='normal')
            b2.configure(state='disabled')
    is_winner()
def is_winner():
    global pos1,pos2
    if pos1 ==100:
        msg=" yahoo ! player-1 won "
        label=t.Label(window,text=msg,height=2,width=20,bg="red", font=('Arial ',15))
        label.place(x=300,y=300)
        reset_coins()
    elif pos2==100:
         msg=" yahoo ! player-2 won "
         label=t.Label(window,text=msg,height=2,width=20,bg="blue", font=('Arial',15))
         label.place(x=300,y=300)
         reset_coins()
def move_coin(Turn ,r):
    global player_1,player_2
    global  Index
    if Turn==1:
        player_1.place(x=Index[r][0],y=Index[r][1])
    else:
        player_2.place(x=Index[r][0],y=Index[r][1])  
def get_index():
    global player_1,player_2
    Num = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
           80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
           60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # vertical distance y=90 # horizontal x =70
    row=20
    i=0
    for x in range(1,11):
        col=30
        for y in range(1,11):
            Index[Num[i]]=(col,row)
            i=i+1
            col=col+90
        row=row+60
    print(Index)
#to store dice images
Dice=[]
#to store x and y co ordinates of a given number
Index={}
#initial positions for players
pos1=None
pos2=None
#ladder Button to the top
ladder={8:29 ,22:61, 54:68,65:97,72:93}
#snake head to tail
snake={23:17,45:5,52:33,67:28,90:50,99:24}
window=t.Tk()
window.geometry("1200x800")
window.title("snake and ladders")
F1=t.Frame(window,width=1200,height=800)
F1.place(x=0,y=0)
images={}
#set snake board
snake_image=Image.open("snakes.png")
resized_snake_image = snake_image.resize((900, 600), Image.Resampling.LANCZOS)
images['snake'] = ImageTk.PhotoImage(resized_snake_image)
label=t.Label(F1,image=images['snake'])
label.place(x=0,y=0)
#player-1 button
b1=t.Button(window,text="player -1",height=2,width=15,fg="black",bg="red",font=('Arial',14),activebackground='white',command=roll_dice)
#player 2 button
b2=t.Button(window,text="player -2",height=2,width=15,fg="black",bg="blue",font=('Arial',14),activebackground='white',command=roll_dice)
#player 1 coin
player_1=t.Canvas(window,width=40,height=40)
player_1.create_oval(10,10,40,40,fill="red")
#player 2 coin
player_2=t.Canvas(window,width=40,height=40)
player_2.create_oval(10,10,40,40,fill="blue")
#whose turn first...by default player_1
turn=1
#keep coins at intial position
reset_coins()
#get index of each num
get_index()
#load dice images
load_dice_images()
#set all the buttons
start_game()
window.mainloop()
