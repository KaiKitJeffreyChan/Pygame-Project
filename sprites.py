# sprites.py alternates between surfaces
# It provides them to the main program so it can draw it

import pygame as pg
import os
from constants import *

'''
up [0]
down [1]
left [2]
right [3]
carry on for sasookee and sakooru
sasookee, sakooru and narootoe all each have 3 for each direction
'''


class SpriteSheetPlayer:
    def __init__(self):
        self.current_char = narootoe
    # Player movement bools, for sprite animations
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.still = True
        self.up_frame = 0
        self.sprite_sheet = pg.image.load(os.path.join("pictures", "naruto2.png"))
        self.character_print = None

    def direction(self):
        keys_pressed = pg.key.get_pressed()
        # To get directions of movement
        if keys_pressed[pg.K_UP] == 1:
            self.up = True
            self.left = False
            self.down = False
            self.right = False
        elif keys_pressed[pg.K_DOWN] == 1:
            self.down = True
            self.up = False
            self.left = False
            self.right = False
        elif keys_pressed[pg.K_LEFT] == 1:
            self.left = True
            self.up = False
            self.down = False
            self.right = False
        elif keys_pressed[pg.K_RIGHT] == 1:
            self.right = True
            self.up = False
            self.left = False
            self.down = False
        else:
            self.still = True
            self.up = False
            self.left = False
            self.down = False
            self.right = False

    def moving_character(self):
        self.direction()
        self.buttons()
        self.character_print = pg.Surface([char_w, char_h])

        # depending on the movement, use according sprites
        if self.up is True:
            self.up_move()
        elif self.down is True:
            self.down_move()
        elif self.left is True:
            self.left_move()
        elif self.right is True:
            self.right_move()
        else: # FAcing down
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[1][1])
            self.character_print.set_colorkey(RED)
            self.character_print = pg.transform.scale(self.character_print, (char_w * 2, char_h * 2))

        self.character_print.set_colorkey(RED)
        self.character_print = pg.transform.scale(self.character_print, (char_w * 2, char_h * 2))
        return self.character_print

    def up_move(self):
        # Alternating frames
        if self.up_frame == 0:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[0][0])
            self.up_frame += 1
        elif self.up_frame == 1:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[0][0])
            self.up_frame += 1
        elif self.up_frame == 2:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[0][2])
            self.up_frame += 1
        elif self.up_frame == 3:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[0][2])
            self.up_frame -= 3

    def down_move(self):
        # Alternating frames
        if self.up_frame == 0:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[1][0])
            self.up_frame += 1
        elif self.up_frame == 1:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[1][0])
            self.up_frame += 1
        elif self.up_frame == 2:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[1][2])
            self.up_frame += 1
        elif self.up_frame == 3:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[1][2])
            self.up_frame -= 3

    def left_move(self):
        # Alternating frames
        if self.up_frame == 0:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[2][0])
            self.up_frame += 1
        elif self.up_frame == 1:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[2][0])
            self.up_frame += 1
        elif self.up_frame == 2:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[2][2])
            self.up_frame += 1
        elif self.up_frame == 3:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[2][2])
            self.up_frame -= 3

    def right_move(self):
        # Alternating frames
        if self.up_frame == 0:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[3][0])
            self.up_frame += 1
        elif self.up_frame == 1:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[3][0])
            self.up_frame += 1
        elif self.up_frame == 2:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[3][2])
            self.up_frame += 1
        elif self.up_frame == 3:
            self.character_print.blit(self.sprite_sheet, (0, 0), self.current_char[3][2])
            self.up_frame -= 3

    def buttons(self):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if 630 + 10 > mouse[0] > 630 and 630 + 10 > mouse[1] > 630:
            if click[0] == 1:
                self.current_char = narootoe

        if 780 + 10 > mouse[0] > 780 and 630 + 10 > mouse[1] > 630:
            if click[0] == 1:
                self.current_char = sasookee

        if 930 + 10 > mouse[0] > 930 and 630 + 10 > mouse[1] > 630:
            if click[0] == 1:
                self.current_char = sakooru

    def character(self):
        return self.current_char

class DragonSprite:
    def __init__(self):
        self.frame = 0
        self.sprite_sheet = pg.image.load(os.path.join("pictures", "dragon3.png"))
        self.drag = dragon

    def fly(self):
        # Alternating frames
        character = pg.Surface([drag_width, drag_height])
        if self.frame == 0:
            character.blit(self.sprite_sheet, (0, 0), self.drag[0])
            self.frame += 1
        elif self.frame == 1:
            character.blit(self.sprite_sheet, (0, 0), self.drag[1])
            self.frame += 1
        elif self.frame == 2:
            character.blit(self.sprite_sheet, (0, 0), self.drag[2])
            self.frame += 1
        elif self.frame == 3:
            character.blit(self.sprite_sheet, (0, 0), self.drag[3])
            self.frame -= 3
        character.set_colorkey((255, 255, 255))
        character = pg.transform.scale(character, (128 * 2, 128 * 2))
        return character

class OldMan:
    def __init__(self):
        self.frame = 0
        self.sprite_sheet = pg.image.load(os.path.join("pictures", "enemies.png"))
        self.o_man = old_man

    def move(self):
        # Alternating frames
        character = pg.Surface([30, 33])
        if self.frame == 0:
            character.blit(self.sprite_sheet, (0, 0), self.o_man[0])
            self.frame += 1
        elif self.frame == 1:
            character.blit(self.sprite_sheet, (0, 0), self.o_man[1])
            self.frame += 1
        elif self.frame == 2:
            character.blit(self.sprite_sheet, (0, 0), self.o_man[2])
            self.frame -= 2

        character.set_colorkey(WHITE)
        character = pg.transform.scale(character, (30 * 2, 33 * 2))
        return character

class Lady:
    def __init__(self):
        self.frame = 0
        self.sprite_sheet = pg.image.load(os.path.join("pictures", "enemies.png"))
        self.lady = lady

    def move(self):
        # Alternating frames
        character = pg.Surface([30, 33])
        if self.frame == 0:
            character.blit(self.sprite_sheet, (0, 0), self.lady[0])
            self.frame += 1
        elif self.frame == 1:
            character.blit(self.sprite_sheet, (0, 0), self.lady[1])
            self.frame += 1
        elif self.frame == 2:
            character.blit(self.sprite_sheet, (0, 0), self.lady[2])
            self.frame -= 2

        character.set_colorkey(WHITE)
        character = pg.transform.scale(character, (30 * 2, 33 * 2))
        return character

class FireBall:
    def __init__(self):
        self.frame = 0
        self.sprite_sheet = pg.image.load(os.path.join("pictures", "fireball.png"))
        self.coords = fireball

    def change(self):
        # Alternating frames
        fire = pg.Surface([50, 50])
        if self.frame == 0:
            fire.blit(self.sprite_sheet, (0, 0), self.coords[0])
            self.frame += 1
        elif self.frame == 1:
            fire.blit(self.sprite_sheet, (0, 0), self.coords[1])
            self.frame += 1
        elif self.frame == 2:
            fire.blit(self.sprite_sheet, (0, 0), self.coords[2])
            self.frame += 1
        elif self.frame == 3:
            fire.blit(self.sprite_sheet, (0, 0), self.coords[3])
            self.frame -= 3

        fire.set_colorkey(WHITE)
        fire = pg.transform.scale(fire, (25, 25))
        fire = pg.transform.rotate(fire, 90)
        return fire

class Rasengan:
    def __init__(self):
        self.frame = 0
        self.sprite_sheet = pg.image.load(os.path.join("pictures", "rasen.png"))
        self.coords = rasengan

    def change(self):
        # Alternating frames
        rasen = pg.Surface([50, 50])
        if self.frame == 0:
            rasen.blit(self.sprite_sheet, (0, 0), self.coords[0])
            self.frame += 1
        elif self.frame == 1:
            rasen.blit(self.sprite_sheet, (0, 0), self.coords[1])
            self.frame += 1
        elif self.frame == 2:
            rasen.blit(self.sprite_sheet, (0, 0), self.coords[2])
            self.frame += 1
        elif self.frame == 3:
            rasen.blit(self.sprite_sheet, (0, 0), self.coords[3])
            self.frame += 1
        elif self.frame == 4:
            rasen.blit(self.sprite_sheet, (0, 0), self.coords[4])
            self.frame += 1
        elif self.frame == 5:
            rasen.blit(self.sprite_sheet, (0, 0), self.coords[5])
            self.frame += 1
        elif self.frame == 6:
            rasen.blit(self.sprite_sheet, (0, 0), self.coords[6])
            self.frame += 1
        elif self.frame == 7:
            rasen.blit(self.sprite_sheet, (0, 0), self.coords[7])
            self.frame += 1
        elif self.frame == 8:
            rasen.blit(self.sprite_sheet, (0, 0), self.coords[8])
            self.frame -= 3
        rasen.set_colorkey((255, 255, 255))
        rasen = pg.transform.scale(rasen, (25, 25))
        rasen = pg.transform.rotate(rasen, 90)
        return rasen

class Shuriken:
    def __init__(self):
        self.frame = 0
        self.sprite_sheet = pg.image.load(os.path.join("pictures", "shuriken.png"))
        self.coords = shuriken

    def change(self):
        # Alternating frames
        shuri = pg.Surface([34, 20])
        if self.frame == 0:
            shuri.blit(self.sprite_sheet, (0, 0), self.coords[0])
            self.frame += 1
        elif self.frame == 1:
            shuri.blit(self.sprite_sheet, (0, 0), self.coords[1])
            self.frame += 1
        elif self.frame == 2:
            shuri.blit(self.sprite_sheet, (0, 0), self.coords[2])
            self.frame += 1
        elif self.frame == 3:
            shuri.blit(self.sprite_sheet, (0, 0), self.coords[3])
            self.frame -= 3

        shuri = pg.transform.scale(shuri, ((34 // 3) * 2, (20 // 3) * 2))
        shuri.set_colorkey((0, 128, 0))
        return shuri