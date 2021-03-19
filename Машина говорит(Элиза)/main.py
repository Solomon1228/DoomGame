import pygame # Подключаю все библиотеки и классы
from Sett import*
from player import Player
from sprites import *
from rey import ray_casting_collumns
from draw import draw

pygame.init() #
sc = pygame.display.set_mode((width,height)) # Размер окна игры

sc_minimap = pygame.Surface((mini_res)) # Размещение мини карты в нижнем левом углу
clock = pygame.time.Clock() # Для фпс
player=Player() # Управление игроком и вычисление его угла обзора
img = pygame.image.load('122.jpg').convert() # Иконка игрока на мини карте


dr = draw(sc, sc_minimap,player) # Отрисовка с помощью рейкаст функции
#dr.music() # Музыка в игре
sprites = sprites() #  Объекты(спрайты)
dr.menu()
pygame.mouse.set_visible(False)


while True: # Начало игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()#  Управление в игре
    sc.fill(black)# Заполнение листа черным цветом
    collumns ,coll_shot = ray_casting_collumns(player, dr.textures) #  Нанесение на стены текстур
    dr.back(player.angle) # Отображение заднего фона
    dr.world(collumns + [obj.obj_locate(player) for obj in sprites.list_of_obj]) #  Прорисовка глобальной карты(стены и спрайты)
    dr.fps(clock)  # Отображение фпс(Правый верхний угол)
    #dr.map(player,img)  # Мини карта
    dr.player_weapon([coll_shot])
    pygame.display.flip() #
    clock.tick() # Ограниечение до 60 кадров в секунду(нужно для того чтобы при 200 фпс игрок не летал со скоростью света а спокойно ходил)


     #pygame.draw.circle(sc, green, player_pos, 10)
    #sc.blit(img, player.pos)
    #pygame.draw.line(sc,green, player.pos, (player.x + width * math.cos(player.angle),
    #                                        player.x + width * math.sin(player.angle)))
     
    #for x,y in world_map:
     # pygame.draw.rect(sc, blue,(x,y,tile,tile),2)