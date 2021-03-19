import pygame
from Sett import *
from map import world_map , wr_wid , wr_hei
from numba import njit

@njit(fastmath=True)
def mapp(a, b):
    return (a // tile) * tile, (b // tile) * tile

@njit(fastmath=True)
def ray_c(player_pos, player_angle, world_map):
    casted_coll = []
    ox, oy = player_pos
    texture_v , texture_h = 1, 1
    xm, ym = mapp(ox, oy)
    cur = player_angle - half_fov
    for rayy in range(numb):
        sin_a = math.sin(cur)
        cos_a = math.cos(cur)
        sin_a = sin_a if sin_a else 0.0001
        cos_a = cos_a if cos_a else 0.0001

        #vert
        x,dx = (xm + tile, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, wr_wid, tile):
            dep_v = (x - ox) / cos_a
            yv = oy + dep_v * sin_a
            tile_v = mapp(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * tile
        
        #horiz
        y,dy = (ym + tile , 1) if sin_a >=0 else (ym, -1)
        for i in range (0, wr_hei, tile):
            dep_h = (y - oy) / sin_a
            xh = ox + dep_h * cos_a
            tile_h = mapp(xh, y+ dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * tile

        #dive
        dep , offset , texture = (dep_v, yv, texture_v) if dep_v < dep_h else (dep_h, xh, texture_h)
        offset = int(offset) % tile
        dep *= math.cos(player_angle - cur)
        dep = max(dep , 0.0001)
        pr = int(pr_coef / dep)
       
        casted_coll.append((dep, offset, pr, texture))
        cur += delta
    return casted_coll

def ray_casting_collumns(player, textures):
            casted_coll = ray_c(player.pos, player.angle, world_map)
            coll_shot = casted_coll [centr][0], casted_coll [centr][2]
            collumns = []
            for ray, casted_values in enumerate(casted_coll):
                dep, offset, pr, texture = casted_values
                if pr > height:
                   coeff = pr / height
                   tt_hei = t_hei / coeff
                   collumn = textures[texture].subsurface(offset * t_scale, ht_hei - tt_hei // 2, t_scale, tt_hei)
                   collumn = pygame.transform.scale(collumn, (scale, height))
                   collumn_pos = (ray * scale, 0)
                else:
                  collumn = textures[texture].subsurface(offset * t_scale, 0, t_scale, t_hei)
                  collumn = pygame.transform.scale(collumn, (scale, pr))
                  collumn_pos = (ray * scale, half_height - pr // 2)
                collumns.append((dep, collumn, collumn_pos))
            return collumns ,coll_shot


        #def ray(sc,player_pos,player_angle):
#    cur = player_angle - half_fov
#    xo, yo = player_pos
#    for ray in range(numb):
#        sin_a = math.sin(cur)
#        cos_a = math.cos(cur)
#        for depth in range(max_dep):
#          x = xo + depth * cos_a
#          y = yo + depth * sin_a
#          #pygame.draw.line(sc,red,player_pos,(x,y),2)
#          if (x // tile * tile, y // tile * tile) in world_map:
#            depth *= math.cos(player_angle - cur)
#            pr = pr_coef / depth
#            c = 255 / (1 + depth * depth * 0.00003)
#            color = (c, c // 2, c // 3)
#            pygame.draw.rect(sc, color , (ray * scale, half_height - pr // 2 , scale , pr))
#            break
#        cur += delta

          #c = 255 / (1 + dep * dep * 0.00002)
        #color = (c, c // 2, c // 3)
        #pygame.draw.rect(sc, color , (rayy * scale, half_height - pr // 2 , scale , pr))