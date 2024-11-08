import pygame
from CODE.LOADER import *
from CODE.STATES import *
from CODE.SETTINGS import *

class ASS_MANAGER():
    def __init__(self,SCREEN,CLOCK,Joystick,MENU_SURF):

        self.SCREEN = SCREEN
        self.CLOCK = CLOCK
        self.MENU_SURF = MENU_SURF
        self.OVERWORLD = "overworld"
        self.LVL = 1
        self.JOYSTICK = Joystick

        self.GAMESTATE = GAMESTATE(self.OVERWORLD,self.LVL)
        self.LOADER = LOADER(self.GAMESTATE,self.LVL)
        
        self.MENU_CHECK = False
        self.CHECK = []
        
        self.CURRENT_LEVEL = 1
        self.LEVEL = 1
        self.LEVEL_COMPLETED = False
        self.GOTTEM = False
        

        self.VICTORY_START_TIME = 0
        self.VICTORY_DURATION = 5000

    def EVENT_LOOP(self):
        while True:
            self.CLOCK.tick(FPS)
            self.OVERWORLD_LOGIC(ENABLED=(True))
            pygame.display.flip()    
    def WORLD_CHECKS(self): 
        
        self.CHECK = {
            1,
            2,
            3,
            4,
            5,
        }
        self.LEVEL = {
            1,
            2,
            3,
            4,
            5,
        }
        for sprite in self.LOADER.GROUPS.MENU_checks:

        
            if self.LOADER.MENU_PLAYER.rect.colliderect(self.LOADER.check1.rect):
                self.CHECK = 1
                self.LEVEL = 1
                self.MENU_CHECK = True
            elif self.LOADER.MENU_PLAYER.rect.colliderect(self.LOADER.check2.rect):
                self.CHECK = 2
                self.LEVEL = 2
                self.MENU_CHECK = True
            elif self.LOADER.MENU_PLAYER.rect.colliderect(self.LOADER.check3.rect):
                self.CHECK = 3
                self.LEVEL = 3
                self.MENU_CHECK = True
            elif self.LOADER.MENU_PLAYER.rect.colliderect(self.LOADER.check4.rect):
                self.CHECK = 4
                self.LEVEL = 4
                self.MENU_CHECK = True
            elif self.LOADER.MENU_PLAYER.rect.colliderect(self.LOADER.check5.rect):
                self.CHECK = 5
                self.LEVEL = 5
                self.MENU_CHECK = True

            
            
        print(self.CHECK)   
        
        
        
        
        
            

    def MENU_PLAYER_HANDLER(self):
        zero_axis = self.JOYSTICK.get_axis(0)
        one_axis = self.JOYSTICK.get_axis(1)
        twelve_axis = self.JOYSTICK.get_axis(12)
        eleven_axis = self.JOYSTICK.get_axis(11)
        thirt_axis = self.JOYSTICK.get_axis(13)
        fourteen_axis = self.JOYSTICK.get_axis(14)
        if abs(one_axis) > 0.05 and (twelve_axis) > 0.05:
            print('up axis')
            self.LOADER.MENU_PLAYER.MOVING_UP = True
        else:
            self.LOADER.MENU_PLAYER.MOVING_UP = False             
        if abs(twelve_axis) > 0.05 and (zero_axis) > 0.05 :
            print('right axis')
            #right
            self.LOADER.MENU_PLAYER.MOVING_RIGHT = True 
        else:
            self.LOADER.MENU_PLAYER.MOVING_RIGHT = False       
        if abs(zero_axis) > 0.05 and (fourteen_axis)> 0.05:
            print('left axis')
            self.LOADER.MENU_PLAYER.MOVING_LEFT = True
            #left
        else:
            self.LOADER.MENU_PLAYER.MOVING_LEFT = False
        if abs(one_axis) > 0.05 and (thirt_axis)> 0.05:
            print('down axis')
            self.LOADER.MENU_PLAYER.MOVING_DOWN = True
        else:
            self.LOADER.MENU_PLAYER.MOVING_DOWN = False                      
    def WORLD_HANDLER(self):
        self.MENU_PLAYER_HANDLER()
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0 and self.MENU_CHECK == True:
                    self.MENU_CHECK = False
                    self.LOADER.LOAD_LEVEL(self.LEVEL)
                    self.LEVEL_LOGIC(ENABLED=(True))
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                
        pygame.display.flip()
    def OVERWORLD_LOGIC(self,ENABLED):
        self.LEVEL_COMPLETED = False
        
        self.LOADER.LOAD_WORLD_BG(WORLD_NUMBER=(self.LEVEL))
        self.LOADER.CREATE_MENU(self.LVL)
        self.UI = USER_INTERFACE(0,0,TARGET=(self.LOADER.MENU_PLAYER))

        while ENABLED == True:

            self.MENU_CHECK = False
            self.CLOCK.tick(FPS)

            #self.SCREEN.fill(WHITE)
            self.LOADER.DRAW_MENU(SCREEN=(self.SCREEN),MENU_SURF=(self.MENU_SURF))
            self.WORLD_CHECKS()
            self.UI.WORLD_STATS(SCREEN=(self.SCREEN),CURRENT_LEVEL=(self.LEVEL)
                 ,MENU_POINT=(self.CHECK) ,ENABLED=(True),CHECKED=(self.MENU_CHECK))
            
            self.WORLD_HANDLER()
            pygame.display.flip()
    
    
    def COMPLETE_LEVEL(self):
        
        if self.LEVEL_COMPLETED:
            pygame.time.wait(1000)
            if self.VICTORY_START_TIME > self.VICTORY_DURATION:
                self.LEVEL_LOGIC(ENABLED=(False))
                self.LOADER.CLEAR_DATA()
                if self.LVL <6:
                    self.LVL +=1
                    self.LEVEL = self.LVL
                print(self.LEVEL)
                print(self.LVL)

                
                self.GAMESTATE.set_state(self.OVERWORLD)
                self.OVERWORLD_LOGIC(ENABLED=(True))
            


       
    def GROUP_LOGIC(self):
        if self.LOADER.PLAYER.HEALTH <= 0:
            self.LEVEL_LOGIC(ENABLED=(False))
            self.LOADER.CLEAR_DATA()
            self.GAMESTATE.set_state(self.OVERWORLD)
            self.OVERWORLD_LOGIC(ENABLED=(True))

        for sprite in self.LOADER.GROUPS.FLAGS:
            if self.LOADER.PLAYER.rect.colliderect(sprite.rect):
                self.LOADER.PLAYER.update_action(3)
                self.LEVEL_COMPLETED = True
                self.VICTORY_START_TIME= pygame.time.get_ticks()
                
                
                
                
                            
                            
        for sprite in self.LOADER.GROUPS.H20:
            if self.LOADER.PLAYER.rect.colliderect(sprite.rect):
                self.LOADER.PLAYER.TAKE_DAMAGE == True
                self.LEVEL_LOGIC(ENABLED=(False))
                self.LOADER.CLEAR_DATA()
                self.GAMESTATE.set_state(self.OVERWORLD)
                self.OVERWORLD_LOGIC(ENABLED=(True))
            if self.LOADER.badguy.rect.colliderect(sprite.rect):
                self.LOADER.badguy.kill()
                
        for sprite in self.LOADER.GROUPS.COINS:
            if self.LOADER.PLAYER.rect.colliderect(sprite.rect):
                self.LOADER.PLAYER.TOTAL_COINS += 1
                #print(self.LOADER.PLAYER.TOTAL_COINS)
                sprite.kill()
        

        for sprite in self.LOADER.GROUPS.ENEMIES:
            
            if self.LOADER.PLAYER.rect.colliderect(sprite.rect):

                if self.LOADER.PLAYER.in_air and self.LOADER.PLAYER.dy >0:
                    sprite.HEALTH = 0
                    
        for sprite in self.LOADER.GROUPS.HEARTS:
            if self.LOADER.PLAYER.rect.colliderect(sprite.rect):
                print("LIFE_GIVER")
                if self.LOADER.PLAYER.HEALTH <=75:
                    self.LOADER.PLAYER.HEALTH += 25
                sprite.kill()
                    

    def LEVEL_LOGIC(self,ENABLED):
        self.LOADER.CLEAR_MENU()
        self.LOADER.CREATE_LEVEL()
        while ENABLED == True:
            self.CLOCK.tick(FPS)
            #print(self.LOADER.PLAYER.TOTAL_COINS)
            self.GROUP_LOGIC()
            
            self.LOADER.DRAW_LEVEL(SCREEN=(self.SCREEN))
            self.LEVEL_HANDLER()
            self.COMPLETE_LEVEL()
            pygame.display.flip()
    def PLAYER_HANDLER(self):
        zero_axis = self.JOYSTICK.get_axis(0)
        one_axis = self.JOYSTICK.get_axis(1)
        twelve_axis = self.JOYSTICK.get_axis(12)
        eleven_axis = self.JOYSTICK.get_axis(11)
        thirt_axis = self.JOYSTICK.get_axis(13)
        fourteen_axis = self.JOYSTICK.get_axis(14)
        if abs(one_axis) > 0.05 and (twelve_axis) > 0.05:
            #print('up axis')
            pass         
        if abs(twelve_axis) > 0.05 and (zero_axis) > 0.05 :
            #print('right axis')
            
            self.LOADER.PLAYER.MOVING_RIGHT = True 
        else:
            self.LOADER.PLAYER.MOVING_RIGHT = False       
        if abs(zero_axis) > 0.05 and (fourteen_axis)> 0.05:
            #print('left axis')
            self.LOADER.PLAYER.MOVING_LEFT = True
            #left
        else:
            self.LOADER.PLAYER.MOVING_LEFT = False
        if abs(one_axis) > 0.05 and (thirt_axis)> 0.05:
            #print('down axis')
            pass
    def LEVEL_HANDLER(self):
        self.PLAYER_HANDLER()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    self.LOADER.PLAYER.JUMP  = True
                if event.button == 6:
                    print('six god')
                    self.LEVEL_LOGIC(ENABLED=(False))
                    self.LOADER.CLEAR_DATA()
                    self.GAMESTATE.set_state(self.OVERWORLD)
                    self.OVERWORLD_LOGIC(ENABLED=(True))
            

            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    self.LOADER.PLAYER.JUMP  = False
        pygame.display.flip()
    
            
        

            
            
            
            
            











