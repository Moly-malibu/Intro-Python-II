# Write a class to hold player information, e.g. what room they are in
# currently.

from time import sleep 

class Player:
    """what room they are in currently."""
    def __init__(self, name, adventure_room, items=None):
        self.name = name
        self.adventure_room = adventure_room
        self.items = []

    def move(self, direction):

        if direction == 'n' and self.adventure_room.n_to:
            self.adventure_room = self.adventure_room.n_to

        elif direction == 'e' and self.adventure_room.e_to:
            self.adventure_room = self.adventure_room.e_to
        
        elif direction == 's' and self.adventure_room.s_to:
            self.adventure_room = self.adventure_room.s_to

        elif direction == 'w' and self.adventure_room.w_to:
            self.adventure_room = self.adventure_room.w_to
        
        else:
            print('Nothin There.')