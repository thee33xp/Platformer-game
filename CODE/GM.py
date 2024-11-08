import pygame, sys
from CODE.SETTINGS import *
from CODE.ASST_MANAGER import *
class INIT_GAME():
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        print("Joystick Connecting... ")
        NUM_JOY = pygame.joystick.get_count()
        if NUM_JOY > 0:
            self.STICK = pygame.joystick.Joystick((0))
            print(f'{NUM_JOY}: Joysticks Connected ')

        else:
            NUM_JOY = []
            print('No Joysticks Connected ')
            
            
        self.SCREEN = pygame.display.set_mode((SCREEN_W,SCREEN_H))
        self.MENU_SURF = pygame.Surface((800,640))
        
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PIXEL PRINCESS")
        self.MANS = ASS_MANAGER(SCREEN=(self.SCREEN),CLOCK=(self.clock),Joystick=(self.STICK),
                                                                    MENU_SURF=(self.MENU_SURF))

    def ENTER_ASST_MANAGER(self):
        while True:
            self.MANS.OVERWORLD_LOGIC(ENABLED=(True))
            pygame.display.update()
        
    

    def INIT_STATE(self):
        self.BG = pygame.image.load("ASSETS/GRAPHICS/BG/MENU/MENU.png")
        
        

        while True:
            self.SCREEN.blit(self.BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = get_font_HEAVY(36).render("PIXEL PRINCESS", True, BLACK)
            MENU_RECT = MENU_TEXT.get_rect(center=(HALF_W, HALF_H - TILE_SIZE * 8))
            START_TEXT = get_font(10).render("Click 'Start' to Play!", True, BLACK)
            START_RECT = START_TEXT.get_rect(center=(HALF_W, HALF_H + TILE_SIZE ))
            self.SCREEN.blit(MENU_TEXT, MENU_RECT)
            self.SCREEN.blit(START_TEXT, START_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 6:
                        self.ENTER_ASST_MANAGER()
            pygame.display.update()

    