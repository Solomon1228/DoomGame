import math

# sett

width = 1200  # длина и ширина окна pygame
height = 800
half_width = width // 2
half_height = height // 2
d_hei = height * 2
tile = 64  # Длина ширина клетки
fps = 1000


#texture sett

t_wid = 64  #длина и ширина для текстуры 
t_hei = 64
ht_hei = t_hei // 2
t_scale = t_wid // tile

# player

player_pos = (1830, 3225)  # Стартовая позиция игрока
player_angle = 0 # первоначальный угол куда смотрит игрок
player_speed = 2 # скорость игрока

# rey cast

fov = math.pi/3 # угол обзора
half_fov = fov/2 #
numb = 300  # кол-во лучей
max_dep = 2500   #ДЛина луча
delta = fov / numb #
dist = numb / (2 * math.tan(half_fov)) #
pr_coef = 3 * dist * tile  # Коэф проекции для рея
scale = width // numb #

# sprite settings

pi2 = math.pi * 2 #  Для угла
centr = numb // 2 -  1 # центральный луч
kk = 100 # Лучи вне экрана, чтобы объекты(спрайты) не исчезали раньше времени
kk_c = numb - 1 + 2 * kk # Лучи для стен

#minimap

map_sc = 6 # уменьшение миникарты в отношении глобальной картинки
mini_res = (1900 // map_sc, height  // map_sc)
map_scc = 16
map_tl = tile // map_scc # 
map_pos = (0, height - height // map_sc)


# color Просто ргб для цветов можно и вручную написать в коде но зачем
white = (255,255,255)
black = (20,0,0)
red = (255,0,0)
green = (0,150,0)
blue = (90,60,255)
purple = (120,0,120)
brown = (190,75,0)
sky = (0,150,255)
yellow = (200 , 200 , 0)
grey = (80, 80, 80)