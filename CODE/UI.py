import pygame
from CODE.SETTINGS import *

class USER_INTERFACE():
    def __init__(self,x,y,TARGET):

        self.image = pygame.Surface((SCREEN_W,TILE_SIZE * 2 ))
        self.image.fill('Tan')
        self.rect = self.image.get_rect(topleft=(x,y))
                                        #360-144
        self.STAT_SURF = pygame.Surface((HALF_W- TILE_SIZE * 8,HALF_H - TILE_SIZE *4))
        self.STAT_SURF.fill('Brown')
        self.stat_rect_L = self.STAT_SURF.get_rect(topleft=(TILE_SIZE*2,TILE_SIZE*8))
        self.stat_rect_R = self.STAT_SURF.get_rect(topleft=(HALF_W + TILE_SIZE*2,TILE_SIZE*8))


        self.target = TARGET

    def STATS(self,SCREEN):

        
        hearts_to_blit = self.target.HEALTH //25
        for i in range(hearts_to_blit):
            heart = LOAD_PIC('ASSETS/GRAPHICS/UI/HEART.png')
            heart_rect = heart.get_rect(topleft=(TILE_SIZE + 27 * i  ,TILE_SIZE-8))
            SCREEN.blit(heart, heart_rect)


        coin = LOAD_PIC('ASSETS/GRAPHICS/UI/COIN.png')
        coin_rect = coin.get_rect(topleft=(HALF_W,TILE_SIZE-8))
        SCREEN.blit(coin,coin_rect)
        COINS_TEXT = get_font(12).render(f" :{self.target.TOTAL_COINS} ", True, BLACK)
        COINS_RECT = COINS_TEXT.get_rect(topleft=(HALF_W+10,TILE_SIZE-2))
        SCREEN.blit(COINS_TEXT, COINS_RECT)



    def DRAW(self,SCREEN):
        self.STATS(SCREEN=(self.image))
        SCREEN.blit(self.image,(self.rect))
    
    def WORLD_STATS(self,SCREEN,CURRENT_LEVEL,MENU_POINT,ENABLED,CHECKED):
        """
        hearts_to_blit = self.target.HEALTH //25
        for i in range(hearts_to_blit):
            heart = LOAD_PIC('ASSETS/GRAPHICS/UI/HEART.png')
            heart_rect = heart.get_rect(topleft=(TILE_SIZE + 27 * i  ,TILE_SIZE-8))
            SCREEN.blit(heart, heart_rect)


        coin = LOAD_PIC('ASSETS/GRAPHICS/UI/COIN.png')
        coin_rect = coin.get_rect(topleft=(HALF_W,TILE_SIZE-8))
        SCREEN.blit(coin,coin_rect)
        COINS_TEXT = get_font(12).render(f" :{self.target.TOTAL_COINS} ", True, BLACK)
        COINS_RECT = COINS_TEXT.get_rect(topleft=(HALF_W+10,TILE_SIZE-2))
        SCREEN.blit(COINS_TEXT, COINS_RECT)
        """
        #heart = LOAD_PIC('ASSETS/GRAPHICS/UI/HEART.png')

        #heart_rect = heart.get_rect(topleft=(TILE_SIZE + 27 * i  ,TILE_SIZE-8))
        #SCREEN.blit(heart, heart_rect)
        


        
        if ENABLED:
            
            if MENU_POINT ==1:

                
                SCREEN.blit(self.STAT_SURF,(self.stat_rect_L))
                 
                TEXT = get_font(14).render(f"LEVEL 1", True, WHITE)
                TEXT_RECT = TEXT.get_rect(center=(108,TILE_SIZE))
                self.STAT_SURF.blit(TEXT,TEXT_RECT)
                TEXT2 = get_font(10).render(f"Click 'A' to Start!", True, WHITE)
                TEXT_RECT2 = TEXT2.get_rect(center=(108,TILE_SIZE *2))
                self.STAT_SURF.blit(TEXT2,TEXT_RECT2)

            elif MENU_POINT ==2:

                SCREEN.blit(self.STAT_SURF,(self.stat_rect_R))
                 
                TEXT = get_font(14).render(f"LEVEL 2", True, WHITE)
                TEXT_RECT = TEXT.get_rect(center=(108,TILE_SIZE))
                self.STAT_SURF.blit(TEXT,TEXT_RECT)
                TEXT2 = get_font(10).render(f"Click 'A' to Start!", True, WHITE)
                TEXT_RECT2 = TEXT2.get_rect(center=(108,TILE_SIZE *2))
                self.STAT_SURF.blit(TEXT2,TEXT_RECT2)
            elif MENU_POINT ==3:
                SCREEN.blit(self.STAT_SURF,(self.stat_rect_L))
                 
                TEXT = get_font(14).render(f"LEVEL 3", True, WHITE)
                TEXT_RECT = TEXT.get_rect(center=(108,TILE_SIZE))
                self.STAT_SURF.blit(TEXT,TEXT_RECT)
                TEXT2 = get_font(10).render(f"Click 'A' to Start!", True, WHITE)
                TEXT_RECT2 = TEXT2.get_rect(center=(108,TILE_SIZE *2))
                self.STAT_SURF.blit(TEXT2,TEXT_RECT2)
            elif MENU_POINT ==4:
                SCREEN.blit(self.STAT_SURF,(self.stat_rect_R))
                 
                TEXT = get_font(14).render(f"LEVEL 4", True, WHITE)
                TEXT_RECT = TEXT.get_rect(center=(108,TILE_SIZE))
                self.STAT_SURF.blit(TEXT,TEXT_RECT)
                TEXT2 = get_font(10).render(f"Click 'A' to Start!", True, WHITE)
                TEXT_RECT2 = TEXT2.get_rect(center=(108,TILE_SIZE *2))
                self.STAT_SURF.blit(TEXT2,TEXT_RECT2)
            elif MENU_POINT ==5:
                SCREEN.blit(self.STAT_SURF,(self.stat_rect_L))
                 
                TEXT = get_font(14).render(f"LEVEL 5", True, WHITE)
                TEXT_RECT = TEXT.get_rect(center=(108,TILE_SIZE))
                self.STAT_SURF.blit(TEXT,TEXT_RECT)
                TEXT2 = get_font(10).render(f"Click 'A' to Start!", True, WHITE)
                TEXT_RECT2 = TEXT2.get_rect(center=(108,TILE_SIZE *2))
                self.STAT_SURF.blit(TEXT2,TEXT_RECT2)
                                 
            else:
                self.STAT_SURF.fill('Brown')
                SCREEN.blit(self.image,(self.rect))
                self.image.fill(WHITE)

                    

        
