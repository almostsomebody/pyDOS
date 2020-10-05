# ------------------------------------------------------------------------------
# obj.py
# Andrew Ortego
# v. 1.0
# ------------------------------------------------------------------------------
import actor, game, item, room

current_game  = game.Game()
current_actor = actor.Actor()

# Rooms ----------------------------------
# Starting Area --------------------------
scottage_inside  = room.scottage_inside()
scottage_kitchen = room.scottage_kitchen()
scottage_outside = room.scottage_outside()

# Inventory Map keeps track of the location of each item in the game. Items that
# can contain objects are also mapped in this dictionary.
# Each room and can_contain-enabled item must be mapped here.

inventory_map = {
    # Inventory ----------------------------------
    'actor' : [],

    # Rooms --------------------------------------

    # Starting Cottage ---------------------------
    'scottage_inside': [],
    'scottage_kitchen': [],
    'scottage_outside': [],
    }