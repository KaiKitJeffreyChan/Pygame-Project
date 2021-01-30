# constants.py is for variables that will NEVER change
# Mainly for colours and coordintes for sprites

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (204, 204, 0)
L_GREY = (191, 191, 191)
D_GREY = (102, 102, 102)
ORANGE = (255, 140, 26)
L_ORANGE = (255, 163, 102)
GRASS_GREEN = (0, 204, 0)
PINK = (255, 77, 166)
L_PINK = (255, 128, 191)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 102, 255)
L_BLUE = (77, 148, 255)

# Variables
char_w = 23
char_h = 31
font_size = 20
font = "rockwell"

# Character locations on spritesheet
nar_up = [(216, 0, 23, 31),
          (240, 0, 23, 31),
          (264, 0, 23, 31)]
nar_right = [(212, 31, 23, 31),
             (240, 31, 23, 31),
             (259, 32, 23, 31)]
nar_down = [(212, 63, 23, 31),
            (240, 63, 23, 31),
            (262, 63, 23, 31)]
nar_left = [(212, 94, 23, 31),
            (240, 94, 23, 31),
            (260, 95, 23, 31)]
narootoe = [nar_up, nar_down, nar_left, nar_right]

sas_up = [(140, 0, 23, 31),
          (165, 0, 23, 31),
          (190, 0, 23, 31)]
sas_right = [(140, 31, 23, 31),
             (165, 31, 23, 31),
             (190, 31, 23, 31)]
sas_down = [(140, 63, 23, 31),
            (165, 63, 23, 31),
            (190, 63, 23, 31)]
sas_left = [(140, 94, 23, 31),
            (165, 94, 23, 31),
            (190, 94, 23, 31)]
sasookee = [sas_up, sas_down, sas_left, sas_right]

sak_up = [(75, 0, 23, 31),
          (100, 0, 23, 31),
          (120, 0, 23, 31)]
sak_right = [(75, 31, 23, 31),
             (100, 31, 23, 31),
             (122, 31, 23, 31)]
sak_down = [(75, 63, 23, 31),
            (100, 63, 23, 31),
            (120, 63, 23, 31)]
sak_left = [(75, 94, 23, 31),
            (100, 94, 23, 31),
            (122, 94, 23, 31)]
sakooru = [sak_up, sak_down, sak_left, sak_right]


# Dragon
drag_width = 128
drag_height = 128
dragon = [(0, 128, 128, 128),
          (128, 128, 128, 128),
          (256, 128, 128, 128),
          (384, 128, 128, 128)]

# OldMan
old_man = [(192, 32, 30, 33),
           (224, 32, 30, 33),
           (256, 32, 30, 33)]

lady = [(288, 160, 30, 33),
        (320, 160, 30, 33),
        (352, 160, 30, 33)]

# Fireball
fireball = [(10, 134, 50, 50),
            (68, 134, 50, 50),
            (68, 135, 50, 50),
            (200, 134, 50, 50),
            (200, 134, 50, 50),
            (10, 134, 50, 50)]

# Rasengan
rasengan = [(20, 70, 65, 65),
            (92, 70, 65, 65),
            (167, 70, 65, 65),
            (249, 70, 65, 65),
            (321, 70, 65, 65),
            (411, 70, 65, 65),
            (489, 70, 65, 65),
            (567, 70, 65, 65),
            (640, 70, 65, 65)]

# Shuriken
shuriken = [(10, 165, 34, 20),
                (44, 165, 34, 20),
                (80, 165, 34, 20),
                (116, 165, 34, 20)]
# walls
walls = [(0, 33, 64, 64),
         (0, 95, 64, 64)]

# attack count colours
attack_c_orange = (65, 448, 30, 30)
attack_c_blue = (290, 448, 30, 30)
attack_c_pink = (388, 448, 30, 30)
attack_c_black = (448, 448, 30, 30)