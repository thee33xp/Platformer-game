import pygame
from CODE.SETTINGS import *


class PLAYER(pygame.sprite.Sprite):
    def __init__(self,pos,obs,box,baddie):

        
        self.TOTAL_COINS = 0
        self.HEALTH = 100
        
        
        
        self.obstacle_sprites = obs
        self.box = box
        self.baddie = baddie
        self.flip = False
        self.vel_y = 0
        self.in_air = True
        self.TAKE_DAMAGE = False
        self.JUMP = False
        self.MOVING_LEFT = False
        self.MOVING_RIGHT = False

        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks() 
        scale = 1
        temp_list = []
        for i in range (4):
            img = pygame.image.load(f'ASSETS/GRAPHICS/PRINCESS/IDLE/{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (6):
            img = pygame.image.load(f'ASSETS/GRAPHICS/PRINCESS/RUN/{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (1):
            img = pygame.image.load(f'ASSETS/GRAPHICS/PRINCESS/JUMP/{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (1):
            img = pygame.image.load(f'ASSETS/GRAPHICS/PRINCESS/VICTORY/{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (1):
            img = pygame.image.load(f'ASSETS/GRAPHICS/PRINCESS/HURT/{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(pos))
        self.old_rect = self.rect.copy()

    def update_animation(self):
        ANIMATION_COOLDOWN = 150
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    def update_action(self,new_action):
        #check if action is different from previous
        if new_action != self.action:
            self.action = new_action
        #update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        
    def ANIMATE_INPUT(self):
        
        # IDLE RIGHT AND WALK RIGHT ANIMATION / ACTION

        if self.JUMP:
            self.update_action(2)

        elif self.MOVING_LEFT :
            self.update_action(1)
        elif self.MOVING_RIGHT:
            self.update_action(1)
        else:     
            self.update_action(0)

        
       
                 
        
    def INPUTS(self):
        
        
        self.dx = 0
        self.dy = 0
        self.SPEED = 5

    
        if self.MOVING_LEFT:
            
            self.MOVING = True
            #self.update_action(1)
            self.dx -= self.SPEED
            self.flip = True
       
        if self.MOVING_RIGHT:
            self.MOVING = True
            
            #self.update_action(1)
            self.dx += self.SPEED
            self.flip = False
         
        if self.JUMP and self.in_air == False:
            
            
            
            self.vel_y = -11
            self.in_air = True
            self.JUMP = False
         
        
        
             
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        self.dy += self.vel_y

        self.ANIMATE_INPUT()
        self.SCREEN_COLLISION()
        self.rect.x += self.dx
        self.collision_horz()
        self.rect.y += self.dy
        self.collision_vert()
        self.box_collide()
        self.bad_collide()
        
        

    def SCREEN_COLLISION(self):
        if self.rect.left + self.dx < 0:
            self.dx = 0
        elif self.rect.right + self.dx > SCREEN_W:
            self.dx = 0
    def collision_horz(self):     
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.dx > 0:
                	self.rect.right = sprite.rect.left
                if self.dx < 0: 
                    self.rect.left = sprite.rect.right
    def collision_vert(self):     
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.vel_y > 0 :
                    
                    self.rect.bottom = sprite.rect.top
                    self.in_air = False
                    self.dy = 0
                    self.vel_y = 0
                elif self.dy < 0: 
                    self.in_air = True
                    self.rect.top = sprite.rect.bottom
    def box_collide(self):
        for sprite in self.box:
     
        
            if sprite.rect.colliderect(self.rect):
                if self.vel_y > 0 :
                    
                    self.rect.bottom = sprite.rect.top
                    self.in_air = False
                    self.dy = 0
                    self.vel_y = 0
                elif self.dy < 0: 
                    pass
                    #self.in_air = True

                    #self.rect.top = sprite.rect.bottom

            if sprite.rect.colliderect(self.rect):
                if self.dx > 0:
                	self.rect.right = sprite.rect.left
                if self.dx < 0: 
                    self.rect.left = sprite.rect.right
    def bad_collide(self):
        for sprite in self.baddie:
            if sprite.rect.colliderect(self.rect):

            
                if self.dx > 0:
                	self.rect.right = sprite.rect.left
                if self.dx < 0: 
                    self.rect.left = sprite.rect.right
    def UPDATE(self,screen):


        
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)


class MENUPLAYER(pygame.sprite.Sprite):
    def __init__(self,pos,obs,STOPS):
        self.stops = STOPS
        self.obstacle_sprites = obs
        
        
        self.flip = False
        self.MOVING_LEFT = False
        self.MOVING_RIGHT = False
        self.MOVING_UP = False
        self.MOVING_DOWN = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks() 
        scale = 1
        temp_list = []
        for i in range (1):
            img = pygame.image.load(f'ASSETS/GRAPHICS/MENU//{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(pos))
        self.old_rect = self.rect.copy()

    def update_animation(self):
        ANIMATION_COOLDOWN = 150
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    def update_action(self,new_action):
        #check if action is different from previous
        if new_action != self.action:
            self.action = new_action
        #update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        

    def INPUTS(self):

        self.dx = 0
        self.dy = 0
        self.SPEED = 5

        if self.MOVING_UP:
            self.dy -= self.SPEED
        if self.MOVING_DOWN:
            self.dy += self.SPEED
        if self.MOVING_LEFT:
            self.dx -= self.SPEED
            self.flip = True
        if self.MOVING_RIGHT:
            self.dx += self.SPEED
            self.flip = False


        self.update_action(0)
            

        self.rect.x += self.dx

        self.collision_horz()
        self.STOPS_HOR()
        
        
        self.rect.y += self.dy
        

        self.collision_vert()
        self.STOPS_VER()
        
        

        

                    
    def STOPS_VER(self):
        for sprite in self.stops:
            if sprite.rect.colliderect(self.rect):
                if self.dy > 0 :
                    self.in_air = False
                    self.rect.bottom = sprite.rect.top
                if self.dy < 0: 
                    
                    self.rect.top = sprite.rect.bottom         
    def  STOPS_HOR(self):
        for sprite in self.stops:
            if sprite.rect.colliderect(self.rect):
                if self.dx > 0:
                	self.rect.right = sprite.rect.left
                if self.dx < 0: 
                    self.rect.left = sprite.rect.right
          
    def collision_horz(self): 

        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.dx > 0:
                	self.rect.right = sprite.rect.left
                if self.dx < 0: 
                    self.rect.left = sprite.rect.right
    def collision_vert(self):     
        
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.dy > 0 :
                    self.in_air = False
                    self.rect.bottom = sprite.rect.top
                if self.dy < 0: 
                    
                    self.rect.top = sprite.rect.bottom

    def UPDATE(self,screen):

        
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)



class TILE(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill("Red")
        self.rect = self.image.get_rect(topleft=(pos))
class CHECK_LEVEL(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill("Green")
        self.rect = self.image.get_rect(topleft=(pos))

class WATER(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill("Blue")
        self.rect = self.image.get_rect(topleft=(pos))
class FLAG(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill("Green")
        self.rect = self.image.get_rect(topleft=(pos))
class COIN(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks() 
        scale = 1
        temp_list = []
        for i in range (4):
            img = pygame.image.load(f'ASSETS/GRAPHICS/TILE/COIN/{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(pos))
        self.old_rect = self.rect.copy()

    def update_animation(self):
        ANIMATION_COOLDOWN = 200
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    def update_action(self,new_action):
        #check if action is different from previous
        if new_action != self.action:
            self.action = new_action
        #update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    def update(self):
        self.update_action(0)
        self.update_animation()
        #SCREEN.blit(self.image,(self.rect))


class ITEM_HEART(pygame.sprite.Sprite):
    def __init__(self,x,y,groups,obs,target):

        super().__init__(groups)
        self.target = target
        
        self.obstacle_sprites = obs
        self.image = pygame.image.load('ASSETS/GRAPHICS/TILE/HEART/0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x,y))
        self.lift_speed = -8
        self.drop_speed = 5
        self.max_lift = 74
        self.lifted = 0

        self.topped = False
        self.vel_y = 0
        self.in_air = True

    def INPUTS(self):
        
        
        self.dy = 0
        self.dx = 0

        if self.lifted < self.max_lift:
            self.rect.y += self.lift_speed
            self.lifted -= self.lift_speed
        
            
            
        self.vel_y +=0.2
        if self.vel_y > 10:
            self.vel_y
        self.dy += self.vel_y
        
        
        self.SCREEN_COLLISION()
        self.rect.x += self.dx

        self.collision_horz()
        
        
        self.rect.y += self.dy
        

        self.collision_vert()
        
    
    def SCREEN_COLLISION(self):
        if self.rect.left + self.dx < 0:
            self.dx = 0
        elif self.rect.right + self.dx > SCREEN_W:
            self.dx = 0
    def collision_horz(self):     
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.dx > 0:
                	self.rect.right = sprite.rect.left
                if self.dx < 0: 
                    self.rect.left = sprite.rect.right
    def collision_vert(self):     
        for sprite in self.obstacle_sprites:
            if self.rect.colliderect(sprite.rect):
                self.dy = 0
                self.vel_y = 0
                #print('vert collision w/ heart')
                self.rect.bottom = sprite.rect.top
                
                    
                

    def update(self):
        
        
        self.INPUTS()
        
        
        #SCREEN.blit(self.image,(self.rect))


class ITEMBOX(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('ASSETS/GRAPHICS/TILE/ITEMBOX/0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos))
        
        self.to_destroy = False
    def update(self):
        self.destroy()
        
    def destroy(self):
        self.to_destroy = True
        if self.to_destroy:
            self.kill()
            self.to_destroy = False

class MENU_STOP(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        
        self.image = LOAD_PIC('ASSETS/GRAPHICS/TILE/MENU_STOP/STOP.png')
        
        self.rect = self.image.get_rect(topleft=(pos))
        










class ENEMY(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obs):
        super().__init__(groups)
        self.obstacle_sprites = obs
        self.HEALTH = 50
        self.ATTACK_COOLDOWN = 0
        self.ATTACK_RATE = 60
        self.direction = (-1,0)
        self.flip = False
        self.vel_y = 0
        self.in_air = False
        self.detection_range = (TILE_SIZE * 4)
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks() 
        scale = 1
        temp_list = []
        for i in range (1):
            img = pygame.image.load(f'ASSETS/GRAPHICS/TILE/DEVIL/IDLE/{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (4):
            img = pygame.image.load(f'ASSETS/GRAPHICS/TILE/DEVIL/WALK/{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range (1):
            img = pygame.image.load(f'ASSETS/GRAPHICS/TILE/DEVIL/HURT/{i}.png').convert_alpha()  
            img = pygame.transform.scale(img,(int(img.get_width() * scale),int(img.get_height()*scale)))  
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(pos))
        self.old_rect = self.rect.copy()

    def update_animation(self):
        ANIMATION_COOLDOWN = 200
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    def update_action(self,new_action):
        #check if action is different from previous
        if new_action != self.action:
            self.action = new_action
        #update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()



    def ATTACK(self,target):
        if self.rect.colliderect(target.rect) :
            if self.direction == (-1,0) and self.dx < 0:
                self.rect.left = target.rect.right
            if self.direction ==(1,0) and self.dx > 0:
                self.rect.right = target.rect.left
            
            
            if self.ATTACK_COOLDOWN == 0:
                self.DAMAGE_PLAYER(target=(target))
                self.ATTACK_COOLDOWN = self.ATTACK_RATE
            

    def DAMAGE_PLAYER(self,target):
        if target.rect.bottom > self.rect.top:
            target.HEALTH -= 25
        
    def collision_vert(self):     
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.vel_y > 0 :
                    
                    self.rect.bottom = sprite.rect.top
                    self.in_air = False
                    self.dy = 0
                    self.vel_y = 0
                elif self.dy < 0: 
                    self.in_air = True
                    self.rect.top = sprite.rect.bottom
    def collision_horz(self):     
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.dx > 0:
                	self.rect.right = sprite.rect.left
                if self.dx < 0: 
                    self.rect.left = sprite.rect.right
    def INPUTS(self,target):
        #self.update_action(0)
        self.dx = 0
        self.dy = 0
        self.SPEED = 1.6
        distance = self.rect.centerx - target.rect.centerx
        if self.rect.centery - self.detection_range  <=  target.rect.centery:
            if abs(distance) < self.detection_range:
                if self.rect.x < target.rect.x:
                    self.update_action(1)
                    self.dx += self.SPEED
                    self.direction = (1,0)
                    
                elif self.rect.x > target.rect.x:
                    self.update_action(1)
                    self.dx -= self.SPEED
                    self.direction = (-1,0)
                
        if abs(distance) > self.detection_range:
            self.update_action(0)
            self.dx = 0
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        self.dy += self.vel_y
        self.rect.x += self.dx
        if self.direction == (-1,0):
            self.flip = False
        if self.direction == (1,0):
            self.flip = True

        
            
        self.collision_horz()
        self.rect.y += self.dy
        self.collision_vert()
        if self.ATTACK_COOLDOWN > 0:
            self.ATTACK_COOLDOWN -= 1

        self.ATTACK(target=(target))
        
            
        
    def update(self,target,screen):
        self.update_animation()
        if self.HEALTH > 0 and self.in_air == False:
            self.INPUTS(target=(target))
        else:
            self.update_action(2)

        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)
   
    
        
        
class GROUPS():
    def __init__(self):
        self.obs_ = pygame.sprite.Group()
        self.H20 = pygame.sprite.Group()
        self.FLAGS = pygame.sprite.Group()
        self.COINS = pygame.sprite.Group()
        self.BOXES = pygame.sprite.Group()
        self.HEARTS = pygame.sprite.Group()
        self.ENEMIES = pygame.sprite.Group()
        
        

        self.MENU_obs_ = pygame.sprite.Group()
        self.MENU_STOP = pygame.sprite.Group()
        self.MENU_checks = pygame.sprite.Group()
        self.MENU_check1 = pygame.sprite.Group()
        
        self.MENU_check2 = pygame.sprite.Group()
        
        self.MENU_check3 = pygame.sprite.Group()
        
        self.MENU_check4 = pygame.sprite.Group()
        self.MENU_check5 = pygame.sprite.Group()
        
        
        

