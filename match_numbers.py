
import random
import time
from tkinter import Tk , Button , DISABLED


def show_symbol(x,y):
    global first
    global previousx , previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previousx = x
        previousy = y
        first = False
     
    elif previousx != x or previousy != y:
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
            time.sleep(1.1)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True

win = Tk()
win.title('Match the numbers')
win.resizable(width=False , height=False)
first = True
previousx = 0
previousy = 0
buttons = { }
button_symbols = { }
symbols = ["1","2","3","4","5","6","7","8","9","10","11","12","1","2","3","4","5","6","7","8","9","10","11","12"]

random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command = lambda x=x , y=y: show_symbol(x,y) , width = 8, height = 5, activebackground = 'white', fg = 'red', font = 'helv36' , justify = 'center',  activeforeground = 'black', bg = 'lightblue', bd = 4)
        button.grid(column = x , row = y)
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()

win.mainloop()
#Hastis's emoji match maker