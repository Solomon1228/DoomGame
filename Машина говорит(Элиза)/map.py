from Sett import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32

_ = False
m_map = [  # Это глобальная карта, ее я меняю как хочу.  использую не текст а списки с цифрами для удобства
    [1, _, _, _, _, 1, _, _, _, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 9, 9, 9, 5, 9, 9, 9, 9, 9, 5, 9, 9, 9, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 9, _, _, _, _, _, _, _, _, _, _, _, 9, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, _, _, _, 1, 1, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 5, _, _, _, _, _, _, _, _, _, _, _, 5, 9, 9, 9, 9, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, _, _, _, 1, 1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 9, _, _, _, _, _, _, _, _, _, _, _, 9, _, _, _, 9, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 9, _, _, _, _, _, _, _, _, _, _, _, 9, _, _, _, 9, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, 1, _, 1, 6, 1, 1, 2, 1, 1, _, 1, _, _, _, 1, 1, 1, 4, 1, 1, 1, 3, _, _, _, _, _, _, _, _, _, _, _, 3, 9, 9, 9, 9, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1, _, 1, _, _, _, 1, _, _, _, _, _, _, 9, _, _, _, _, _, _, _, _, _, _, _, 9, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 4, _, _, _, _, _, _, _, _, 4, 1, 1, _, _, _, 1, 1, 1, _, _, _, _, 9, 9, 9, 5, 9, 9, _, 9, 9, 5, 9, 9, 9, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1, 1, _, 9, _, _, _, 9, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1, 1, _, 9, _, _, _, 9, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1, 1, _, 3, _, _, _, 3, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 4, _, _, _, _, _, _, _, _, 4, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, _, _, _, 9, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, 1, 1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1, _, 9, _, _, _, 9, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, 1, 1, 1, 2, 1, 1, _, 1, 1, 2, 1, 1, _, _, 1, _, _, _, _, _, _, _, 9, 9, 9, 9, 9, 9, _, _, _, 9, 9, 9, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, 1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 9, _, _, _, _, _, _, _, _, _, _, 9, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, _, 1, 1, _, _, _, 4, _, _, _, 4, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 9, _, _, 9, 9, 9, _, _, _, 9, 9, 9, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, 1, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 9, _, _, 9, _, 9, _, _, _, 9, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, 1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 9, _, _, 9, _, 9, _, _, _, 9, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, 9, 9, 9, 9, _, 5, _, _, _, 5, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, 1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, 1, 1, _, _, _, _, _, _, _, _, 1, 1, _, 9, _, _, _, 9, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, _, _, 1, 1, _, _, _, _, _, _, _, _, 1, 1, 1, 9, 5, _, 5, 9, 1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [4, _, _, _, 4, 1, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 4, 1, _, _, _, _, _, 1, 4, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, 7],
    [1, _, _, _, 1, 1, _, _, _, _, _, _, _, _, _, 4, _, _, 1, 1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, 7],
    [1, _, _, _, 1, 1, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, _, _, _, _, _, _, _, _, 7],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1, _, _, 1, 1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, 7],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 8],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1, _, _, 1, 1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, 7],
    [1, _, _, _, 1, 1, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 7, 7, 7, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, 7],
    [1, _, _, _, 1, 1, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 7, 7, _, _, _, 7, 7, 7, 7, _, _, _, _, _, _, _, _, 7],
    [1, _, _, _, 1, 1, _, _, _, _, _, _, _, _, _, 1, _, _, 1, 1, _, _, _, _, _, 1, 1, 6, 1, 1, 1, _, _, _, _, _, 1, 1, 6, 1, 1, 1, _, _, _, 7, _, _, 7, 7, _, _, 7, _, _, _, _, _, _, _, _, 7],
    [6, _, _, _, 6, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, _, _, 1, 1, _, _, _, _, _, _, _, _, _, _, 1, 7, 7, _, 7, 7, 1, _, _, 1, _, _, _, _, _, 7, _, _, 7, _, _, _, 7, 7, 7, _, 7, 7, _, 7, 7, 7],
    [1, _, _, _, 1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, 7, _, _, 7, _, _, _, _, _, 7, 7, 7, 7, 7, 7, _, _],
    [1, _, _, _, 1, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, 7, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [1, _, _, _, 1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, 7, _, _, 7, _, 7, 7, 7, 7, 7, 7, 7, 7, 7, _, _, _],
    [1, _, _, _, _, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, 7, _, _, 7, 7, 7, _, 7, _, 7, _, 7, _, 7, 7, _, _],
    [1, _, _, _, 1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, 7, _, _, _, 7, _, _, _, _, _, _, _, _, _, 7, _, _],
    [1, _, _, _, 1, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, 8, _, _],
    [1, _, _, _, 1, 1, 1, 1, 1, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, _, _, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, 7, _, _, _, 7, _, _, _, _, _, _, _, _, _, 7, _, _],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, 10, 1, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, 7, _, _, _, 7, _, _, 7, _, 7, _, 7, _, 7, 7, _, _],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 11, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, _, _, _],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, 10, 1, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 2, 1, 1, 1, _, _, _, _, _, _, 7, _, _, _, 7, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, 1, 10, 4, _, _, 1, _, _, _, _, _, 1, _, _, _, _, _, 7, 7, 7, 7, 7, 7, 7, _, 7, 7, 7, 7, 7, 7, 7, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, 11, _, _, _, _, 1, _, _, 1, _, 1, 1, _, _, _, _, _, 7, _, _, _, _, 7, _, _, _, 7, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, 1, 10, 4, _, _, _, _, _, 1, 1, 1, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, 1, 1, 1, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 7, _, _, _, _, 7, _, _, _, 7, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, 7, _, _, _, 7, _, _, _, _, 7, 4, 4, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, _, _, _, _, 7, 7, 7, 7, 7, 7, _, _, _, 7, 7, 7, 7, 7, 7, _, 3, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, 7, _, _, _, 7, _, _, _, _, 7, _, 4, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, 13, _, 4, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, 7, _, _, _, 7, _, _, _, _, 7, _, 4, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, 7, 7, 7, 7, 7, _, _, _, 7, 7, 7, 7, 7, 7, _, 6, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, 5, 6, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7, 8, 7, 7, 8, 7, 7, 8, 7, 7, 8, 7, 7, 8, 7, _, _, _, _, _, _, _, _, _, _, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
#text_map = [ # Это глобальная карта, ее я меняю как хочу.  1-это просто стены, остальное уже декорации
#    '1111111111111111111',
#    '1........11.......1',
#    '1......1111.......1',
#    '1.................1',
#    '1.................1',
#    '1.................1',
#    '1.................1',
#    '1111f1f1f1111111111',
#]
wr_wid = len(m_map[1]) * tile
wr_hei = len(m_map) * tile
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
minimap = set()
coll_coll = []
for j, row in enumerate(m_map): # Если программа видит 1 то рисует стену если . - то ничего.
    for i, char in enumerate(row):
        if char:
             minimap.add((i * map_tl, j * map_tl))
             if char != 13:
                coll_coll.append(pygame.Rect(i * tile, j * tile , tile, tile))
             if char == 1:
                world_map[(i * tile, j * tile)] = 1
             elif char == 2:
                world_map[(i * tile, j * tile)] = 2
             elif char == 3:
                world_map[(i * tile, j * tile)] = 3
             elif char == 4:
                world_map[(i * tile, j * tile)] = 4
             elif char == 5:
                world_map[(i * tile, j * tile)] = 5
             elif char == 6:
                world_map[(i * tile, j * tile)] = 6
             elif char == 8:
                world_map[(i * tile, j * tile)] = 8
             elif char == 9:
                world_map[(i * tile, j * tile)] = 9
             elif char == 7:
                world_map[(i * tile, j * tile)] = 7
             elif char == 10:
                world_map[(i * tile, j * tile)] = 10
             elif char == 11:
                world_map[(i * tile, j * tile)] = 11
             elif char == 12:
                world_map[(i * tile, j * tile)] = 12
             elif char == 13:
                world_map[(i * tile, j * tile)] = 12
