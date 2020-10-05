# ------------------------------------------------------------------------------
# room.py
# Andrew Ortego
# v. 1.0
# ------------------------------------------------------------------------------
import item, obj, events
from interface import format_output
import json
import random
tavernVisited = False
innVisited = False
houseVisited = False

# Code By almost_somebody - Simplified In-Game Dialogue using JSON #
f = open("rooms.json", "r")
rooms = json.load(f)
# End Code Append #

## This block actually creates the room. ##
class Room:
    def __init__(self):
        self.name = "<Room Name>"
        self._description = "<Decorator Room Description>"
        self.default_direction = "You can't go that way."
        
    @property
    def description(self):
        return self._description
                          
    def hint(self):
        '''<game.hint()> calls this function on the current_room.'''
        format_output("The leaflet is blank.")
    
    def look(self):
        ''' Print information about the current room.'''
        format_output(self.description)
                    
        if item.inventory_map[self.name]:
            for i in item.inventory_map[self.name]:
                print ("There is a", i.name, "here.")
                    
    def north(self): return {'message' : self.default_direction}
    def east(self) : return {'message' : self.default_direction}
    def south(self): return {'message' : self.default_direction}
    def west(self) : return {'message' : self.default_direction}
    def northeast(self): return {'message' : self.default_direction}
    def southeast(self): return {'message' : self.default_direction}
    def southwest(self): return {'message' : self.default_direction}
    def northwest(self): return {'message' : self.default_direction}
    def up(self)   :  return {'message' : "You can't go that way."}
    def down(self) :  return {'message' : "You can't go that way."}
    
    def n(self) : return self.north()
    def e(self) : return self.east()
    def s(self) : return self.south()
    def w(self) : return self.west()
    def ne(self): return self.northeast()
    def se(self): return self.southeast()
    def sw(self): return self.southwest()
    def nw(self): return self.northwest()
    def u(self) : return self.up()
    def d(self) : return self.down()
    
##### STARTING COTTAGE #####

## Template room ##
class scottage_inside(Room):
    def __init__(self):
        Room.__init__(self)
        self.first_visit  = True
        self.default_direction = 'You cannot go that way from here.'
        self.fileName = "room.scottage_inside()"
        self.description = rooms['room.scottage_inside()']['dialogue']['area']
        self.name = rooms['room.scottage_inside()']['area_name']
            
    @property
    def description(self):
        return self._description
        
    @description.setter
    def description(self, description):
        self._description = description
    
    def south(self):
        return {'movement': obj.scottage_outside}

    def east(self):
        return {'movement': obj.scottage_kitchen}

## End Template Room ##

class scottage_kitchen(Room):
    def __init__(self):
        Room.__init__(self)
        self.first_visit  = True
        self.default_direction = 'You cannot go that way from here.'
        self.description = rooms['room.scottage_kitchen()']['dialogue']['area']
        self.fileName = "room.scottage_kitchen()"
        self.name = rooms['room.scottage_kitchen()']['area_name']
            
    @property
    def description(self):
        return self._description
        
    @description.setter
    def description(self, description):
        self._description = description
    
    def west(self):
        return {'movement': obj.scottage_inside}

class scottage_outside(Room):
    def __init__(self):
        Room.__init__(self)
        self.first_visit  = True
        self.default_direction = 'You cannot go that way from here.'
        self.description = rooms['room.scottage_outside()']['dialogue']['area']
        self.fileName = "room.scottage_outside()"
        self.name = rooms['room.scottage_outside()']['area_name']
            
    @property
    def description(self):
        return self._description
        
    @description.setter
    def description(self, description):
        self._description = description

    def north(self):
        return {'movement': obj.scottage_inside}
    
    def south(self):
        return {'movement': obj.forestpath_1}
    
    def east(self):
        return {'movement': obj.broad_1}
