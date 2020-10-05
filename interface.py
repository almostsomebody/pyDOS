# ------------------------------------------------------------------------------
# interface.py
# Andrew Ortego
# v. 1.0
# ------------------------------------------------------------------------------
import textwrap, obj
import os
from os import path

copyright = ''' Text-based Game Demo v.1.0 "The Fundamentals"'''

def format_output(message):
    ''' Formats the output of an on-screen message to fit the screen width.'''
    nLine = ""
    if message is not None:
        message = " ".join(message.split())

        # DO NOT DELETE THIS BLOCK!!! It is how the game reads dialogue in the TK Window. #
        with open(path.join("game", "dia"), "w+") as f:
            f.write(message)
        with open(path.join("game", "dia")) as source:
            with open(path.join("game", "newDia"),'w') as output:
                for line in source:
                    nLine += (line.replace('\n', ','))
                output.write(nLine)
        os.remove(path.join("game", "dia"))
    else:
        print("DBUG: format_output was sent a NoneType object!")
        
def l(self):
    self.look()
        
def look():
    ''' Prints the current room's description, and any available items.'''
    from obj import current_game, inventory_map
    msg = '\n' + current_game.current_room.description
    current_room_obj = current_game.current_room.__class__.__name__
    for i in inventory_map[current_room_obj]:
        if i.visible:
            msg += (' There is a {} here.'.format(i.name[0]))
        if i.contains_item:
            stored_item = inventory_map.get(i.__class__.__name__)[0]
            if stored_item.visible:
                msg += (' There is a {} inside the {}.'.format(\
                    stored_item.name[0],
                    i.name[0]))
    format_output(msg)

   
