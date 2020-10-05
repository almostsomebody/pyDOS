## SCRIPT BY ALMOST_SOMEBODY ##
from tkinter import *
import os
from os import path
import obj, tokenizer, interface, room, game
from game import Game
from interface import format_output
import options
        
window = Tk()

windowTitle = options.getWindowTitle()
window.title(windowTitle)
windowGeometry=options.getWindowGeometry()
window.geometry(windowGeometry)
window.resizable(0,0)
window.configure(bg='#0C0C0C')

textLoops = 0
justStarted = True

# make all terminal input uppercase #
def to_uppercase(*args):
    var.set(var.get().lower())
    window.update()

moveFrame = Frame(window)
moveFrame.pack(side=TOP, expand=True)

moveAndArea = Text(moveFrame, fg="#CCCCCC", bg='#0C0C0C', width='600', height="10", borderwidth=0, highlightthickness=0)
moveAndArea.configure(font=("Courier"))
moveAndArea.insert(END, "Something")

comFrame = Frame(window, bg='#0C0C0C', borderwidth=0, highlightthickness=0)
comFrame.pack(side=TOP, anchor=NW)

dynCursorText = str("C:\\"+options.getGameName()+"_")
dyn_cursor = Label(comFrame, text=dynCursorText, fg="#CCCCCC", bg='#0C0C0C')
dyn_cursor.grid(column=1, row=1)
dyn_cursor.configure(font=("Courier"))

var = StringVar(window)

try:
    # python 3.6
    var.trace_add('write', to_uppercase)
except AttributeError:
    # python < 3.6
    var.trace('w', to_uppercase)

dBox = Frame(window)
dBox.pack(side=TOP, expand=True)

dialogBox = Text(dBox,fg="#CCCCCC", bg='#0C0C0C', width='600', height="100", borderwidth=0, highlightthickness=0)
dialogBox.pack(fill='both')
dialogBox.configure(state="disabled")
dialogBox.configure(font=("Courier"))

termInput = Entry(comFrame, textvariable=var, fg="#CCCCCC", bg='#0C0C0C', borderwidth=0, highlightthickness=0)
termInput.grid(column=2, row=1)
termInput.configure(font=("Courier"))

def convert(lst): 
    return ' '.join(lst).split()

def clearChat():
    dialogBox.configure(state="normal")
    dialogBox.delete('1.0', END)
    dialogBox.configure(state="disabled")
    window.update()
        
def newDialogue(x):
    clearChat()
    curInput = termInput.get()
    termInput.delete(0, 'end')
    move(curInput)
    with open(path.join("game", "newDia"), "r") as f:
        for line in f:
            cInput = line.replace('*', '\n')
    newDialog = str(cInput+"\n")
    dialogBox.configure(state="normal")
    dialogBox.insert(END, newDialog)
    
    dialogBox.configure(state="disabled")
    window.update()

## Possible Save Names - Append The Name Of Your JSON Block + Actual Room Block From Room.py ##
possible_saves = {
    'room.scottage_inside()': room.scottage_inside(),
    'room.scottage_kitchen()': room.scottage_kitchen(),
    'room.scottage_outside()': room.scottage_outside()
}   
 
def start_game():
    savePath = options.getSavePath()
    startingRoom = options.getStartingRoom()
    if path.exists(savePath) == False:
        with open(savePath, "w+") as f:
            print(startingRoom)
            f.write(startingRoom)
            f.close
    with open(options.getSavePath(), "r") as f:
        curGameRoom = f.readline()
    obj.current_game.current_room = possible_saves[curGameRoom]
    window.update()

def move(arg):
    ''' Get the user's input, create tokens out of it, and process them.'''
    #current_game.print_header()
    user_input = [arg]
    if user_input:
        tokenized_input = tokenizer.get_token(user_input)
        if tokenized_input:
            token_pattern = tokenizer.pattern_match(tokenized_input)
            if token_pattern:
                tokenizer.execute_command(
                    tokenized_input,
                    token_pattern,
                    obj.current_game)
        else:
            pass
    else:
        format_output("Pardon?")
    window.update()
    
termInput.bind('<Return>', newDialogue)

if justStarted == True:
    start_game()
    move("look")
    with open(path.join("game", "newDia"), "r") as f:
        for line in f:
            cInput = line.replace('*', '\n')
    newDialog = str(cInput+"\n")
    dialogBox.configure(state="normal")
    dialogBox.insert(END, newDialog)
    dialogBox.configure(state="disabled")
    justStarted = False
    

window.mainloop()
