# A7,Chi Heng Jeffrey Hui,CIS 345, T TH 12:00 PM
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

number_of_attempt = 1
def event_handler(index):
    """This function makes the program interchange between 'X' and 'O' """
    global  number_of_attempt
    if number_of_attempt % 2 > 0:
        buttons[index].configure(text="X", state=DISABLED)
        number_of_attempt = number_of_attempt+1
    else:
        buttons[index].configure(text='O', state=DISABLED)
        number_of_attempt=number_of_attempt+1
    check_answer()

def check_answer():
    """This function evaluate the winner, reset the number_of_attempt, and create a message box"""
    global  number_of_attempt,cats_game
    if ((button0['text'] == 'X' and button1['text'] == 'X' and button2['text'] == 'X') or (button3['text'] == 'X' and button4['text'] == 'X' and button5['text']=='X') or
            (button6['text']=='X' and button7['text']=='X' and button8['text']=='X')or(button0['text']=='X' and button4['text']=='X' and button8['text']=='X')or(button2['text']=="X" and button4['text']=='X' and button6['text']=='X')or
            (button0['text']=='X' and button3['text']=='X' and button6['text']=='X') or (button1['text']=='X' and button4['text']=='X' and button7['text']=='X') or (button2['text']=='X' and button5['text']=='X' and button8['text']=='X')):
        number_of_attempt=1
        reset()
        tkinter.messagebox.showinfo('Message', "Player one won the game!")
        return

    elif ((button0['text']=='O' and button1['text']=='O' and button2['text']=='O') or (button3['text']=='O' and button4['text']=='O' and button5['text']=='O')or
            (button6['text']=='O' and button7['text']=='O' and button8['text']=='O')or(button0['text']=='O' and button4['text']=='O' and button8['text']== 'O')or(button2['text']=="O" and button4['text']=='O' and button6['text']=='O')
               or (button0['text'] == 'O' and button3['text'] == 'O' and button6['text'] == 'O') or (
                    button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O') or(button2['text']=='O' and button5['text']=='O' and button8['text']=='O')):
        number_of_attempt=1
        reset()
        tkinter.messagebox.showinfo('Message', "Player 2 won the game!")
        return
    if number_of_attempt==10:
        number_of_attempt=1
        reset()
        tkinter.messagebox.showinfo('Error',"Cats Game")

def reset():
    """This function reset the text display inside the button. Also, it change its state to normal"""
    for x in buttons:
        x.configure(text='', state=NORMAL)




#window stuff
window = Tk()
window.title('Tic Tac Toe')
window.configure(background='light blue')
# Buttons
button0 = Button(window, height = 4, width = 10,text='',command=lambda : event_handler(0))
button0.grid(row=0,column=0)
button1 = Button(window, height = 4, width = 10,text='',command=lambda : event_handler(1))
button1.grid(row=0,column=1)
button2 = Button(window, height = 4, width = 10,text='',command=lambda : event_handler(2))
button2.grid(row=0,column=2)
button3 = Button(window,height = 4, width = 10,text='',command=lambda : event_handler(3))
button3.grid(row=1,column=0)
button4 = Button(window,height = 4, width = 10,text='',command=lambda : event_handler(4))
button4.grid(row=1,column=1)
button5 = Button(window,height = 4, width = 10,text='',command=lambda : event_handler(5))
button5.grid(row=1,column=2)
button6 = Button(window,height = 4, width = 10,text='',command=lambda : event_handler(6))
button6.grid(row=2,column=0)
button7 = Button(window,height = 4, width = 10,text='',command=lambda : event_handler(7))
button7.grid(row=2,column=1)
button8 = Button(window,height = 4, width = 10,text='',command=lambda : event_handler(8))
button8.grid(row=2,column=2)
buttons = [button0, button1, button2, button3, button4, button5, button6, button7, button8]
window.mainloop()