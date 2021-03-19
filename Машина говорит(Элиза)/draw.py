import pygame
from Sett import *
from rey import ray_c
from map import minimap 
from collections import deque
from player import Player
from random import  randrange
import sys

class draw:
    def __init__(self,sc,sc_minimap,player):
        self.sc = sc
        self.sc_minimap = sc_minimap
        self.player = player
        self.font = pygame.font.SysFont('Arial',25, bold=True)
        self.textures = {1: pygame.image.load('wolfwall/WALL1.bmp').convert(),  # В этом списке находятся все картинки которые я использую для текстур неба, пола и стен 
                         0: pygame.image.load('wolfwall/WALL0.bmp').convert(),
                         2: pygame.image.load('wolfwall/WALL2.bmp').convert(),
                         3: pygame.image.load('wolfwall/WALL3.bmp').convert(),
                         4: pygame.image.load('wolfwall/WALL4.bmp').convert(),
                       's': pygame.image.load('sky2.jpg').convert(),
                         5: pygame.image.load('wolfwall/WALL5.bmp').convert(),
                         6: pygame.image.load('wolfwall/WALL6.bmp').convert(),
                         8: pygame.image.load('wolfwall/WALL8.bmp').convert(),
                         9: pygame.image.load('wolfwall/WALL9.bmp').convert(),
                         7: pygame.image.load('wolfwall/WALL7.bmp').convert(),
                         10: pygame.image.load('wolfwall/WALL40.bmp').convert(),
                         11: pygame.image.load('wolfwall/WALL41.bmp').convert(),
                         12: pygame.image.load('wolfwall/WALL7.bmp').convert(),
                         13: pygame.image.load('wolfwall/WALL7.bmp').convert(),
                        }
        #Оружие
        self.weapon_sp = pygame.image.load('спрайты/weapon/0.png').convert_alpha()
        self.weapon_shot = deque([pygame.image.load(f'спрайты/weapon/shot/{i}.png').convert_alpha() for i in range(9)])
        self.weapon_wep = deque([pygame.image.load(f'спрайты/weapon/shot/wep/{i}.png').convert_alpha() for i in range(9)])
        self.weapon_rect = self.weapon_sp.get_rect()
        self.weapon_pos = (half_width - self.weapon_rect.width // 2, height - self.weapon_rect.height)
        self.shot_len = len(self.weapon_shot)
        self.shot_spd = 5
        self.shot_cnt = 0
        self.shot_anim_cnt = 0
        self.shot_anim_trigger = True

        self.sfx = deque([pygame.image.load(f'спрайты/weapon/shot/sfx/{i}.png').convert_alpha() for i in range(4)])
        self.sfx_len = len(self.sfx)
        self.sfx_cnt = 0

        # Меню
        self.menu_trigger = True
        self.menu_picture = pygame.image.load('menu1.png')

    def player_weapon(self, shots):

        if self.player.shot:
            shot_sprite = self.weapon_shot[0]
            
           
            shot_sprite_wep = self.weapon_wep[0]
            self.sc.blit(shot_sprite,(525 , 475))
            self.sc.blit(shot_sprite_wep,(525,500))
            self.shot_anim_cnt += 1
            if self.shot_anim_cnt == self.shot_spd:
                self.weapon_shot.rotate(-1)
                self.weapon_wep.rotate(-1)
                self.shot_anim_cnt = 0
                self.shot_cnt += 1
                self.shot_anim_trigger = False
            if self.shot_cnt == self.shot_len:
                self.player.shot = False
                self.shot_cnt = 0

                self.shot_anim_trigger = True
        else:
            self.sc.blit(self.weapon_sp, self.weapon_pos)

    def shot_sfx(self):
        if self.sfx_cnt < self.sfx_len:
            sfx = pygame.transform.scale(self.sfx[0], (self.shot_pr,self.shot_pr))
            sfx_rect = sfx.get_rect()
            self.sc.blit(sfx,(half_width - sfx_rect.w // 2, half_height - sfx_rect.h // 2))
            self.sfx_len += 1
            self.sfx.rotate(-1)

    def back(self, angle):
         sky_off = -10 * math.degrees(angle) % width   #Небо
         self.sc.blit(self.textures['s'], (sky_off , 0))
         self.sc.blit(self.textures['s'], (sky_off - width, 0))
         self.sc.blit(self.textures['s'], (sky_off + width, 0))
         pygame.draw.rect(self.sc, grey, (0,half_height,width,half_height)) # Пол
    
    def world(self, world_obj):
        for obj in sorted(world_obj, key = lambda n: n[0],reverse = True):
            if obj[0]:
                _, obj, object_pos = obj
                self.sc.blit(obj, object_pos)
          
    def fps(self, clock):
        display = str(int(clock.get_fps()))
        ren = self.font.render(display, 0 , white)
        self.sc.blit(ren, (width - 33, 0))

    def map(self, player ,img):
       self.sc_minimap.fill(black)
       map_x, map_y = player.x // map_sc , player.y // map_sc
       
       #pygame.draw.line(self.sc_minimap,red, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
       #map_y + 12 * math.sin(player.angle)), 2)
       self.sc_minimap.blit(img, (map_x, map_y))
       for x,y in minimap:
          pygame.draw.rect(self.sc_minimap, red,(x, y, map_tl, map_tl))
       self.sc.blit(self.sc_minimap,(map_pos))
    
   
    def music(self):
        pygame.mixer.pre_init(44100,-16 , 2, 2048)
        pygame.mixer.init()
        self.music = {
          '1':  pygame.mixer.music.load('1.mp3'),
           '2': pygame.mixer.music.load('2.mp3'),
           #'4': pygame.mixer.music.load('4.mp3'),
           #'3': pygame.mixer.music.load('3.mp3'),
            }
        
        pygame.mixer.music.play()

    def menu(self):
        x = 0 
        button_font = pygame.font.Font('font.ttf', 72)
        label_font = pygame.font.Font('font1.otf', 185)
        start = button_font.render('START' , 1 , pygame.Color('red'))
        button_start = pygame.Rect(0,0,400,150)
        button_start.center = half_width, half_height
        exit = button_font.render('EXIT' , 1 , pygame.Color('red'))
        button_exit = pygame.Rect(0,0,400,150)
        button_exit.center = half_width, half_height + 200

        while self.menu_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()

            self.sc.blit(self.menu_picture, (0, 0), (x % width, 0, width, height))
   

            pygame.draw.rect(self.sc, black, button_start, border_radius=25, width=10)
            self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))

            pygame.draw.rect(self.sc, black, button_exit, border_radius=25, width=10)
            self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))

            #color = randrange(40)
            #label = label_font.render('WOLFESTEIN 3D', 1, (color, color, color))
            #self.sc.blit(label, (15, -30))

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if button_start.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, black, button_start, border_radius=25)
                self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))
                if mouse_click[0]:
                    self.menu_trigger = False
            elif button_exit.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, black, button_exit, border_radius=25)
                self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))
                if mouse_click[0]:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            
