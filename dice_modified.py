from tkinter import *
import random

roll_the_dice = Tk()
roll_the_dice.geometry("500x500")
roll_the_dice.title('Roll the Dice')
roll_the_dice.configure(bg='lime')


def roll_dice():
    dice_code = ['\u2680','\u2681', '\u2682', '\u2683','\u2684', '\u2685']
    numbers = { '\u2680':1,'\u2681':2, '\u2682':3, '\u2683':4,'\u2684':5, '\u2685':6}
    dice = random.choice(dice_code)

    if dice in numbers.keys():
        dice_number = numbers[dice]

    dice1.config (text=dice)
    
    dice1_number.config (text= dice_number)
    
frame = Frame(roll_the_dice)
frame.pack(pady=5)

#dice picture
dice1 = Label(frame,font=('times new roman',150), fg='black', bg='white')
dice1.grid(row=1, column=0)

# dice number below dice picture
dice1_number = Label(frame,font=('times new roman',20))
dice1_number.grid(row=7, column=0)

#dice roll button
button = Button(roll_the_dice, text='Roll Dice', font=('ariel',24), relief=GROOVE, bg ='cyan', command = roll_dice)
button.pack(pady=20)

roll_dice()    
