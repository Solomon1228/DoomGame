import pygame
from Sett import *
from collections import deque

class sprites:
    def __init__(self):
        self.sprite_types = { # Тут будет список со всеми текстурами для спрайтов и их анимаций
            'barr': {
                'sprite': pygame.image.load('спрайты/barr/0.png').convert_alpha(),
                'view_ang': None,
                'shift': 1.8,
                'sc': 0.4,
                'anim' : None,
                'anim_dist' : None,
                'anim_spd' : None,},
                
            'billy' : { 
                'sprite': pygame.image.load('спрайты/billy/0.png').convert_alpha(),
                'view_ang' : None,
                'shift': 0.2,
                'sc': 0.7, 
                'anim' : None,
                'anim_dist' : None,
                'anim_spd' : None,},
            
            'devil': {
                'sprite': [pygame.image.load(f'спрайты/d/{i}.png').convert_alpha() for i in range(8)],
                'view_ang': True,
                'shift': -0.2,
                'sc': 1.1,
                'anim': deque(
                    [pygame.image.load(f'спрайты/d/anim/{i}.png').convert_alpha() for i in range(9)]),
                'anim_dist': 200,
                'anim_spd': 10,},
            }


        self.list_of_obj = [ # Размещение объектов(спрайтов)
            spriteobj(self.sprite_types['barr'], (14, 6)),
            spriteobj(self.sprite_types['barr'], (30, 51)),
            #spriteobj(self.sprite_types['billy'], (30, 50)),
            spriteobj(self.sprite_types['devil'], (30, 50)),
            spriteobj(self.sprite_types['devil'], (8.65, 5.5)),
            ]
   
    


   

class spriteobj:
    def __init__(self, par, pos): # тут идет проверка на то, какой передо мной спрайт что за объект, движется он или это просто бочка, его позиция, высота и размер
        self.obj = par['sprite']
        self.view_ang = par['view_ang']
        self.anim = par['anim']
        self.anim_dist = par['anim_dist']
        self.anim_spd = par['anim_spd']
        self.anim_cnt = 0
        self.pos = self.x , self.y = pos[0] * tile, pos[1] * tile
        self.shift = par['shift']
        self.sc = par['sc']
        self.side = 30
        if self.view_ang :
            self.sprite_angle = [frozenset(range(i, i + 45)) for i in range (0, 360 ,45)]
            self.sprite_pos = {angle: pos for angle , pos in zip(self.sprite_angle , self.obj)}

    def is_on_fire(self):
        if centr - self.side // 2 < self.curr < centr + self.side // 2 :
            return self.dist_spr, self.pr_height
        return float('inf'), None

    def pos(self):
        return self.x - self.side // 2 , self.y - self.side // 2

    def obj_locate(self, player):
      
        dx, dy = self.x - player.x , self.y - player.y
        self.dist_spr = math.sqrt(dx ** 2 + dy ** 2)

        self.al = math.atan2(dy, dx)
        bet = self.al - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            bet += pi2

        delta_r = int(bet / delta)
        self.curr = centr + delta_r # Текущий луч
        self.dist_spr *= math.cos(half_fov - self.curr * delta) #Убирание эффекта рыбий глаз 

        fake = self.curr + kk
        if 0 <= fake < kk_c * kk and self.dist_spr > 30:
            self.pr_height = min(int (pr_coef / self.dist_spr * self.sc), d_hei)
            h_prheight = self.pr_height // 2
            shift = h_prheight * self.shift
             
            if self.view_ang:
                if self.al < 0:
                    self.al += pi2
                self.al = 360 - int(math.degrees(self.al))

                for angle in self.sprite_angle:
                    if self.al in angle:
                        self.obj = self.sprite_pos[angle]
                        break
# Анимации
            sprite_obj = self.obj
            if self.anim and self.dist_spr < self.anim_dist:
                sprite_obj = self.anim[0]
                if self.anim_cnt < self.anim_spd:
                    self.anim_cnt += 1
                else:
                    self.anim.rotate()
                    self.anim_cnt = 0

# позиция спрайта
            sprite_pos = (self.curr * scale - h_prheight, half_height - h_prheight + shift) 
            sprite = pygame.transform.scale( sprite_obj, (self.pr_height,self.pr_height))
            return (self.dist_spr , sprite, sprite_pos)
        else:
            return (False,)