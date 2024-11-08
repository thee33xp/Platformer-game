import pygame
from CODE.CLASSES import *
from CODE.UI import *
from CODE.SETTINGS import *
from CODE.CAMERA import *

class LOADER():
    def __init__(self,game_state,LEVEL):
        
        self.level_data = None
        self.game_state = game_state
        self.LEVEL = LEVEL
        self.GROUPS = GROUPS()
        self.LEVEL_NUM = []
        self.heart_trigger = False
        
    # LEVEL METHODS
    def LOAD_LEVEL(self,level_number):
        self.LEVEL_NUM = level_number
        filename = (f"CSV_DATA/level{self.LEVEL_NUM}.csv")
        print(f'Loading {filename} ... ')
        self.game_state.set_state(self.LEVEL)
    def CLEAR_DATA(self):
        self.level_data = None
        self.heart_trigger = False
        self.GROUPS.obs_.empty()
        self.GROUPS.FLAGS.empty()
        self.GROUPS.H20.empty()
        self.GROUPS.BOXES.empty()
        self.GROUPS.COINS.empty()
        self.GROUPS.ENEMIES.empty()
        self.GROUPS.HEARTS.empty()
    def CREATE_LEVEL(self):
        self.LOAD_LEVEL_BG()
        self.level_data = {
            "bound": LOAD_CSV(f'CSV_DATA/LEVEL//LEVEL_{self.LEVEL_NUM}/LEVEL/LEVEL.csv'),
            "water": LOAD_CSV(f'CSV_DATA/LEVEL//LEVEL_{self.LEVEL_NUM}/WATER/water.csv'),
            "PLAYER": LOAD_CSV(f'CSV_DATA/LEVEL//LEVEL_{self.LEVEL_NUM}/PLAYER/player.csv'),
            "flag": LOAD_CSV(f'CSV_DATA//LEVEL/LEVEL_{self.LEVEL_NUM}/FLAG/flag.csv'),
            "item_box1": LOAD_CSV(f'CSV_DATA/LEVEL//LEVEL_{self.LEVEL_NUM}/BOX/box.csv'),
            "coin": LOAD_CSV(f'CSV_DATA/LEVEL//LEVEL_{self.LEVEL_NUM}/COIN/coin.csv'),
            "ENEMY": LOAD_CSV(f'CSV_DATA/LEVEL//LEVEL_{self.LEVEL_NUM}/BADGUY/badguy.csv'),
        } 
        for style,data in self.level_data.items():
            for row_index, row in enumerate(data):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILE_SIZE
                        y = row_index * TILE_SIZE

                        if style == "bound" :
                            TILE((x,y),[self.GROUPS.obs_])
                        if style == "water" :
                            WATER((x,y),[self.GROUPS.H20])     
                        if style == "flag" :
                            self.flag = FLAG((x,y),[self.GROUPS.FLAGS])

                        if style == "item_box1" :
                            self.box = ITEMBOX((x,y),[self.GROUPS.BOXES])
                        if style == "coin" :        
                            self.coin = COIN((x,y),[self.GROUPS.COINS])
                        if style == "ENEMY" :        
                            self.badguy = ENEMY((x,y),[self.GROUPS.ENEMIES],obs=(self.GROUPS.obs_))
                        if style == "PLAYER" :        
                            self.PLAYER = PLAYER((x,y),obs=(self.GROUPS.obs_),box=(self.GROUPS.BOXES),
                                                                    baddie=(self.GROUPS.ENEMIES))           
                        
    def TRIGGER(self,SCREEN):
        for sprite in self.GROUPS.ENEMIES:
            if self.PLAYER.rect.colliderect(sprite.rect):
                self.PLAYER.update_action(4)
                self.PLAYER.dx = 0
        for sprite in self.GROUPS.BOXES:
            if self.PLAYER.rect.colliderect(sprite.rect):
                self.heart = ITEM_HEART(x=(sprite.rect.centerx),y=(sprite.rect.centery - 10 ),
                                        groups=(self.GROUPS.HEARTS),obs=(self.GROUPS.obs_),target=self.PLAYER)
                if self.PLAYER.dy < 0:
                    self.heart_trigger = True
                    sprite.kill()

    def DRAW_LEVEL(self,SCREEN):
        self.GROUPS.COINS.update()
        self.DRAW_LEVEL_BG(SCREEN)
        self.DRAW_LEVEL_GROUPS(SCREEN=(SCREEN))
        self.UI = USER_INTERFACE(0,0,TARGET=(self.PLAYER))
        self.UI.DRAW(SCREEN=(SCREEN))
        self.TRIGGER(SCREEN=(SCREEN))
        if self.heart_trigger:
            self.heart.INPUTS()
            self.GROUPS.HEARTS.draw(surface=(SCREEN))
    def DRAW_LEVEL_GROUPS(self,SCREEN):
        self.GROUPS.ENEMIES.update(target=(self.PLAYER),screen=(SCREEN))
        self.GROUPS.COINS.draw(surface=(SCREEN))
        self.GROUPS.BOXES.draw(surface=(SCREEN))
        self.PLAYER.update_animation()
        self.PLAYER.INPUTS()
        self.PLAYER.UPDATE(screen=(SCREEN)) 
    def LOAD_LEVEL_BG(self):
        self.img = LOAD_PIC(f'ASSETS/GRAPHICS/BG/LEVEL/LEVEL_{self.LEVEL_NUM}.png')    
    def DRAW_LEVEL_BG(self,SCREEN):
        
        SCREEN.blit(self.img,(0,0))
   
    # MENU METHODS
    def LOAD_WORLD_BG(self,WORLD_NUMBER):
        self.WORLD_img = LOAD_PIC(f'ASSETS/GRAPHICS/BG/WORLD/WORLD.png') 
    def DRAW_WORLD_BG(self,SCREEN,MENU_SURF):
        SCREEN.fill('Pink')
        SCREEN.blit(MENU_SURF,(0 - self.cam.offset.x,0 - self.cam.offset.y))
        MENU_SURF.fill('Pink')
        MENU_SURF.blit(self.WORLD_img,(0,0))   
        self.DRAW_MENU_GROUPS(MENU_SURF=(MENU_SURF))        
        
    def CREATE_MENU(self,LEVEL):
        self.level_data = {
            "bound": LOAD_CSV(f'CSV_DATA/MENU/MENU.csv'),
            "CHECK1": LOAD_CSV(f'CSV_DATA/MENU/CHECKS/CHECK1.csv'),
            "CHECK2": LOAD_CSV(f'CSV_DATA/MENU/CHECKS/CHECK2.csv'),
            "CHECK3": LOAD_CSV(f'CSV_DATA/MENU/CHECKS/CHECK3.csv'),
            "CHECK4": LOAD_CSV(f'CSV_DATA/MENU/CHECKS/CHECK4.csv'),
            "CHECK5": LOAD_CSV(f'CSV_DATA/MENU/CHECKS/CHECK5.csv'),


            "PLAYER": LOAD_CSV(f'CSV_DATA/MENU/PLAYER/PLAYER{LEVEL}.csv'),
            "stop": LOAD_CSV(f'CSV_DATA/MENU/STOPS/BOUND{LEVEL}.csv'),
            

        } 
        for style,data in self.level_data.items():
            for row_index, row in enumerate(data):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * 16
                        y = row_index * 16
                        if style == "bound" :
                            TILE((x,y),[self.GROUPS.MENU_obs_])
                        if style == "CHECK1" :
                            self.check1 = CHECK_LEVEL((x,y),[self.GROUPS.MENU_checks,self.GROUPS.MENU_check1])
                        if style == "CHECK2" :
                            self.check2 = CHECK_LEVEL((x,y),[self.GROUPS.MENU_checks,self.GROUPS.MENU_check2])
                        if style == "CHECK3" :
                            self.check3 = CHECK_LEVEL((x,y),[self.GROUPS.MENU_checks,self.GROUPS.MENU_check3])
                        if style == "CHECK4" :
                            self.check4 = CHECK_LEVEL((x,y),[self.GROUPS.MENU_checks,self.GROUPS.MENU_check4])
                        if style == "CHECK5" :
                            self.check5 = CHECK_LEVEL((x,y),[self.GROUPS.MENU_checks,self.GROUPS.MENU_check5])
                        
                        if style == "stop" :
                            self.STOPPER = MENU_STOP((x,y),self.GROUPS.MENU_STOP)
                        if style == "PLAYER" :
                            self.MENU_PLAYER = MENUPLAYER((x,y),self.GROUPS.MENU_obs_,self.GROUPS.MENU_STOP)      
    def CLEAR_MENU(self):
        self.GROUPS.MENU_obs_.empty()
        self.GROUPS.MENU_checks.empty()
        self.GROUPS.MENU_STOP.empty()
    def DRAW_MENU(self,SCREEN,MENU_SURF):
        self.cam = Camera(player=(self.MENU_PLAYER))
        follow = Follow(self.cam,self.MENU_PLAYER)
        self.cam.setmethod(follow)
        self.cam.scroll()

        self.DRAW_WORLD_BG(SCREEN=(SCREEN),MENU_SURF=(MENU_SURF))
        self.MENU_PLAYER.update_animation()
        self.MENU_PLAYER.INPUTS()
        self.MENU_PLAYER.UPDATE(screen=(MENU_SURF))
    def DRAW_MENU_GROUPS(self,MENU_SURF):
        #self.GROUPS.MENU_obs_.draw(surface=(SCREEN))
        #self.GROUPS.MENU_checks_.draw(surface=(SCREEN))
        self.GROUPS.MENU_STOP.draw(surface=(MENU_SURF))

