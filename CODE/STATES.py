import pygame




class GAMESTATE():
    def __init__(self,WORLD,LEVEL):
         
        self.LEVEL = LEVEL
        self.WORLD = WORLD
        self.state = self.WORLD
    def set_state(self,new_state):
        self.state = new_state
    def is_overworld(self):
        return self.state == self.WORLD
    def is_level(self):
        return self.state == self.LEVEL