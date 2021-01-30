# Logic:
# Use sprites.py to alternate between surfaces
# Classes in main program moves and draws the given sprite
# Classes in main also manage other variables for playable game
# constants.py is for variables that will NEVER change

# Jeffrey Chan
# Farzin Aliverdi

from sprites import *
from constants import *
import pygame as pg
import os


class Player:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.speed = 7

    def restrictions(self):
        global screen_height, screen_width, game_stage
        keys_pressed = pg.key.get_pressed()

        # Stopping player from leaving restricted area by speeding up
        if keys_pressed[pg.K_LSHIFT] == 1:
            multiplyer = 2
        else:
            multiplyer = 1

        # Different x restrictions for different time in game
        if game_stage == 1:
            restrictionx = 470
        elif game_stage == 2:
            restrictionx = 1025
        elif game_stage == 3:
            restrictionx = screen_width

        # Actual restrictions
        if self.x_position < 1:
            self.x_position += self.speed * multiplyer
        elif self.x_position > restrictionx - 43:
            self.x_position -= self.speed * multiplyer
        if self.y_position < 400:
            self.y_position += self.speed * multiplyer
        elif self.y_position > screen_height - 100:
            self.y_position -= self.speed * multiplyer

    def update(self):
        keys_pressed = pg.key.get_pressed()

        # Moving(Shift to speed up)
        if keys_pressed[pg.K_LSHIFT] == 1:
            if keys_pressed[pg.K_UP] == 1:
                self.y_position += -(self.speed * 2)
            elif keys_pressed[pg.K_DOWN] == 1:
                self.y_position += (self.speed * 2)
            elif keys_pressed[pg.K_LEFT] == 1:
                self.x_position += -(self.speed * 2)
            elif keys_pressed[pg.K_RIGHT] == 1:
                self.x_position += (self.speed * 2)
        else:
            if keys_pressed[pg.K_UP] == 1:
                self.y_position += -self.speed
            elif keys_pressed[pg.K_DOWN] == 1:
                self.y_position += self.speed
            elif keys_pressed[pg.K_LEFT] == 1:
                self.x_position += -self.speed
            elif keys_pressed[pg.K_RIGHT] == 1:
                self.x_position += self.speed

        self.restrictions()

    def draw(self, character):
        self.update()
        # Bliting character on the screen
        screen.blit(character, (self.x_position, self.y_position))

    def rects(self):
        # Creates a Rect to use for checking collisions
        rect = pg.Rect(self.x_position, self.y_position, 43, 61)
        return rect

class Enemy():
    def __init__(self, x_position, y_position, frame_attack, width, height, att_speed, enemy, damage):
        self.x_position = x_position
        self.y_position = y_position
        self.right = True
        self.attack_speed = att_speed
        self.frame = 1
        self.steps = 0
        self.speed = 5
        self.e_attack = ""
        self.frame_attack = frame_attack
        self.width = width
        self.height = height
        self.enemy_class = enemy
        self.damage = damage

    def update(self):
        # Moving side to side
        if self.right is True:
            self.x_position += self.speed
            self.steps += 1
            if self.steps == 45:
                self.right = False
                self.steps = 0
        else:
            self.x_position -= self.speed
            self.steps += 1
            if self.steps == 45:
                self.right = True
                self.steps = 0

    def attack(self):
        global attack_moving_d

        # Used a class as Enemy classes have a Rec function like Player
        if self.enemy_class == 1:
            self.enemy_class = boss
        elif self.enemy_class == 2:
            self.enemy_class = mini_boss_1
        elif self.enemy_class == 3:
            self.enemy_class = mini_boss_2

        # Enemy moves 10 times and attacks
        if self.steps < 30 and self.steps > 10:
            if self.steps == 11:  # To make sure to use Attack class once otherwise attack wont move down
                self.e_attack = Attack(self.enemy_class, self.width // 2, "Down", self.attack_speed)
            attack_moving_d = True
        else:
            attack_moving_d = False

        if attack_moving_d is True:
            # Draws attack on screen through reference to class: Attack() -- self.e_attack
            attack = self.frame_attack.change()
            attack = pg.transform.rotate(attack, 180)
            self.e_attack.draw(attack)
            att_r = self.e_attack.rects()
            self.collisions(att_r)

    def collisions(self, attack_r):
        global team_health
        # Check collision with Player and does damage
        if attack_r.colliderect(player.rects()):
            if team_health > 0:
                team_health -= self.damage

    def draw(self, character):
        self.update()
        self.attack()
        # Flipping character
        if self.right is False:
            screen.blit(character, (self.x_position, self.y_position))
        else:
            character = pg.transform.flip(character, True, False)
            screen.blit(character, (self.x_position, self.y_position))

    def rects(self):
        rect = pg.Rect(self.x_position, self.y_position, self.width, self.height)
        return rect


class Attack:
    def __init__(self, player, player_width, direction, speed):
        self.speed = speed
        self.x = player.rects()[0] + player_width
        self.y = player.rects()[1]
        self.direction = direction
        self.player_width = player_width

    def move(self):
        # For moving up and down
        if self.direction == "Down":
            self.y += self.speed
        else:
            self.y -= self.speed

    def draw(self, attack):
        self.move()
        # Drawing
        screen.blit(attack, (self.x, self.y))

    def rects(self):
        # Creates a Rect to use for checking collisions
        rect = pg.Rect(self.x, self.y, self.player_width, 30)
        return rect


def check_collisions(att, list, cur_player):
    # creating Rects
    enemy_drag_r = list[0]
    enemy_drag_r = enemy_drag_r.rects()
    enemy_old_man_r = list[2]
    enemy_old_man_r = enemy_old_man_r.rects()
    enemy_queen = list[3]
    enemy_queen = enemy_queen.rects()

    # Collisions
    if att.colliderect(enemy_drag_r):
        if drag_health > 0:  # Stop excess damage
            damage(cur_player, dragon)
    elif att.colliderect(enemy_old_man_r):
        if mini_boss_1_health > 0:
            damage(cur_player, old_man)
    elif att.colliderect(enemy_queen):
        if mini_boss_2_health > 0:
            damage(cur_player, lady)

def draw_attack():
    global attack_moving_p, attack, narootoe_attack_count, sakooru_attack_count, sasookee_attack_count, attack_count_stop
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[pg.K_SPACE] == 1:
        attack = Attack(player, char_w, "Up", 20)
        attack_moving_p = True
        player_in_use = frame_player.character()

        # To make sure to decrease count once when you click space
        if attack_count_stop > 1:
            if player_in_use == narootoe:
                narootoe_attack_count -= 1
            elif player_in_use == sasookee:
                sasookee_attack_count -= 1
            elif player_in_use == sakooru:
                sakooru_attack_count -= 1
            attack_count_stop -= 1
    else:
        attack_count_stop = 2

    if attack_moving_p is True:
        # Each player has a different attack
        fire = frame_fire.change()
        rasen = frame_rasengan.change()
        shuri = frame_shuriken.change()
        player_in_use = frame_player.character()

        # Attack depending on the player
        if player_in_use == narootoe:
            if narootoe_attack_count > -1:  # Restricting attacks so spams do not work
                attack.draw(rasen)
        elif player_in_use == sasookee:
            if sasookee_attack_count > -1:
                attack.draw(fire)
        elif player_in_use == sakooru:
            if sakooru_attack_count > -1:
                attack.draw(shuri)
        att_r = attack.rects()

        check_collisions(att_r, player_list, player_in_use)


def damage(char, enemy):
    global team_health, narootoe_attack, sakooru_attack, sasookee_attack, sakooru_heal, drag_health, mini_boss_1_health
    global mini_boss_2_health

    # Checking to see for the enemy and which character is in use..
    # ..to do damage accordingly
    if char == narootoe and enemy == dragon:
        drag_health -= narootoe_attack
    elif char == sasookee and enemy == dragon:
        drag_health -= sasookee_attack
    elif char == sakooru and enemy == dragon:
        drag_health -= sakooru_attack
        if team_health < 100:  # So you dont heal above 100
            team_health += sakooru_heal
    elif char == narootoe and enemy == old_man:
        mini_boss_1_health -= narootoe_attack * 4  # Balancing attack by *4
    elif char == sasookee and enemy == old_man:
        mini_boss_1_health -= sasookee_attack * 4
    elif char == sakooru and enemy == old_man:
        mini_boss_1_health -= sakooru_attack * 4
        if team_health < 100:
            team_health += sakooru_heal * 4
    elif char == narootoe and enemy == lady:
        mini_boss_2_health -= narootoe_attack * 4
    elif char == sasookee and enemy == lady:
        mini_boss_2_health -= sasookee_attack * 4
    elif char == sakooru and enemy == lady:
        mini_boss_2_health -= sakooru_attack * 4
        if team_health < 100:
            team_health += sakooru_heal * 4

def char_bar():
    sprite_face = pg.image.load(os.path.join("pictures", "SelectionScreenPortraits.png"))
    nar_pic = pg.Surface([97, 30])
    sas_pic = pg.Surface([97, 30])
    sak_pic = pg.Surface([90, 30])
    mouse = pg.mouse.get_pos()

    # Narootoe Bar
    pg.draw.rect(screen, ORANGE, pg.Rect(580, 650, 110, 140))
    pg.draw.rect(screen, L_GREY, pg.Rect(590, 640, 90, 160))
    pg.draw.rect(screen, L_GREY, pg.Rect(570, 660, 130, 120))
    nar_pic.blit(sprite_face, (0, 0), (540, 74, 97, 30))
    nar_pic.set_colorkey((0, 0, 100))
    screen.blit(nar_pic, (585, 645))

    # Button interaction
    if 630+10 > mouse[0] > 630 and 630+10 > mouse[1] > 630:
        pg.draw.rect(screen, L_ORANGE, pg.Rect(630, 630, 10, 10))
    else:
        pg.draw.rect(screen, ORANGE, pg.Rect(630, 630, 10, 10))

    # Sasookee Bar
    pg.draw.rect(screen, BLUE, pg.Rect(730, 650, 110, 140))
    pg.draw.rect(screen, L_GREY, pg.Rect(740, 640, 90, 160))
    pg.draw.rect(screen, L_GREY, pg.Rect(720, 660, 130, 120))
    sas_pic.blit(sprite_face, (0, 0), (631, 74, 97, 30))
    sas_pic.set_colorkey((0, 0, 100))
    screen.blit(sas_pic, (735, 645))

    # Button interaction
    if 780+10 > mouse[0] > 780 and 630+10 > mouse[1] > 630:
        pg.draw.rect(screen, L_BLUE, pg.Rect(780, 630, 10, 10))
    else:
        pg.draw.rect(screen, BLUE, pg.Rect(780, 630, 10, 10))

    # Sakooru Bar
    pg.draw.rect(screen, PINK, pg.Rect(880, 650, 110, 140))
    pg.draw.rect(screen, L_GREY, pg.Rect(890, 640, 90, 160))
    pg.draw.rect(screen, L_GREY , pg.Rect(870, 660, 130, 120))
    sak_pic.blit(sprite_face, (0, 0), (0, 104, 90, 30))
    sak_pic.set_colorkey((0, 0, 100))
    screen.blit(sak_pic, (890, 640))

    # Button interaction
    if 930+10 > mouse[0] > 930 and 630+10 > mouse[1] > 630:
        pg.draw.rect(screen, L_PINK, pg.Rect(930, 630, 10, 10))
    else:
        pg.draw.rect(screen, PINK, pg.Rect(930, 630, 10, 10 ))

    # Text in bar, and attack circles(attack counters)
    text_print(font, font_size, "Narootoe", BLACK, 630, 680)
    text_print(font, 15, "Attack: Medium", BLACK, 630, 730)
    text_print(font, 15, "Ability: None", BLACK, 630, 750)
    attack_count_print(ORANGE, narootoe_attack_count, 590, 700)

    text_print(font, font_size, "Sasookee", BLACK, 780, 680)
    text_print(font, 15, "Attack: High", BLACK, 780, 730)
    text_print(font, 15, "Ability: None", BLACK, 780, 750)
    attack_count_print(BLUE, sasookee_attack_count, 760, 700)

    text_print(font, font_size, "Sakooru", BLACK, 930, 680)
    text_print(font, 15, "Attack: Low", BLACK, 930, 730)
    text_print(font, 15, "Ability: Heal", BLACK, 930, 750)
    attack_count_print(PINK, sakooru_attack_count, 900, 700)

def attack_regen():
    global narootoe_attack_count, sasookee_attack_count, sakooru_attack_count, sasookee_regen, sakooru_regen, narootoe_regen

    # Counter for regen of attack count
    if narootoe_regen == 100:  # Balancing because he has x2 the attack count
        if narootoe_attack_count < 6:  # Restricting attack count
            narootoe_attack_count += 1
    if sakooru_regen == 50:
        if sakooru_attack_count < 4:
            sakooru_attack_count += 1
    if sasookee_regen == 50:
        if sasookee_attack_count < 3:
            sasookee_attack_count += 1

    # Stops spam attacking from countinuously decreasing attack count and go negative
    if narootoe_attack_count < -1:
        narootoe_attack_count = -1
    if sakooru_attack_count < 0:
        sakooru_attack_count = -1
    if sasookee_attack_count < 0:
        sasookee_attack_count = -1

    # Resets regen count
    if narootoe_regen > 100:
        narootoe_regen = 1
    if sasookee_regen > 100:
        sasookee_regen = 1
    if sakooru_regen > 100:
        sakooru_regen = 1

    narootoe_regen += 1
    sakooru_regen += 1
    sasookee_regen += 1

def attack_count_print(colour, count, x, y):
    ball_colour = pg.Surface([30, 30])
    ball_black = pg.Surface([30, 30])
    ball_black.blit(attack_count_sprite, (0, 0), attack_c_black)

    # Different colour depending on the character
    if colour == ORANGE:
        ball_colour.blit(attack_count_sprite, (0, 0), attack_c_orange)
        temp_count = 6
    elif colour == BLUE:
        ball_colour.blit(attack_count_sprite, (0, 0), attack_c_blue)
        temp_count = 3
    elif colour == PINK:
        ball_colour.blit(attack_count_sprite, (0, 0), attack_c_pink)
        temp_count = 4

    ball_black.set_colorkey(BLACK)
    ball_colour.set_colorkey(BLACK)
    ball_black = pg.transform.scale(ball_black, (15, 15))
    ball_colour = pg.transform.scale(ball_colour, (15, 15))

    # Draws the attacks you have
    # Black = used attack
    # Colour = attack can be used
    other_count = count
    while temp_count != 0:
        if other_count > 0:
            screen.blit(ball_colour, (x, y))
        else:
            screen.blit(ball_black, (x, y))

        temp_count -= 1
        other_count -= 1
        x += 15


def text_print(font, size, message, colour, x, y):
    # Prints text
    text = pg.font.SysFont(font, size)
    text_surf = text.render(message, True, colour)
    text_rect = text_surf.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)


def map():
    global wall_list, game_stage

    cross_red = pg.Rect(0, 400, screen_width, 5)
    pg.draw.rect(screen, RED, cross_red)

    # Draws the walls
    wall_sprite = pg.image.load(os.path.join("pictures", "wall.png"))
    wall_top = pg.Surface([64, 64])
    wall_bot = pg.Surface([64, 64])
    wall_top.blit(wall_sprite, (0, 0), (walls[0]))
    wall_bot.blit(wall_sprite, (0, 0), (walls[1]))
    y = 336
    screen.blit(wall_bot, (1025, 400))
    for x in range(15):
        screen.blit(wall_top, (1025, y))
        rect = pg.Rect(1025, y, 64, 64)
        wall_list += [rect]
        y -= 64

    y = 336
    screen.blit(wall_bot, (470, 400))
    for x in range(15):
        screen.blit(wall_top, (470, y))
        rect = pg.Rect(470, y, 64, 64)
        wall_list += [rect]
        y -= 64

    rect1 = pg.Rect(470, 464, 5, 400)
    rect2 = pg.Rect(1025, 464, 5, 400)
    if game_stage == 1:
        pg.draw.rect(screen, RED, rect1)
    if game_stage == 2:
        pg.draw.rect(screen, RED, rect2)


def health_bar(x, y, health, max):
    health_bar = pg.Rect(x, y, health, 10)
    health_bar_2 = pg.Rect(x, y, max, 10)
    health_bar_3 = pg.Rect(x - 3, y - 3, max + 6, 16)

    pg.draw.rect(screen, BLACK, health_bar_3)
    pg.draw.rect(screen, L_GREY, health_bar_2)

    #  middle = yellow and low is red
    if health < max // 4:
        pg.draw.rect(screen, RED, health_bar)
    elif health < max // 2:
        pg.draw.rect(screen, YELLOW, health_bar)
    else:
        pg.draw.rect(screen, GRASS_GREEN, health_bar)

def game_stage_change():
    # Change game stage
    global game_stage
    if drag_health <= 0:
        game_stage = 3
    if mini_boss_1_health <= 0:
        game_stage = 2
    if mini_boss_2_health <= 0:
        game_stage = 3

pg.init()

# The screen
screen_width = 1536
screen_height = 864
screen_size = (screen_width, screen_height)
screen = pg.display.set_mode(screen_size, pg.RESIZABLE)
pg.display.set_caption("FARREY")

sprite_face = pg.image.load(os.path.join("pictures", "SelectionScreenPortraits.png"))
attack_count_sprite = pg.image.load(os.path.join("pictures", "ability.png"))
character_print = pg.Surface([131, 43])
character_print.blit(sprite_face, (0, 0), (524, 269, 131, 43))
character_print.set_colorkey((0, 0, 100))

game_stage = 1
# 1 = level one...

# Player and enemy variables
drag_health = 250
mini_boss_1_health = 50
mini_boss_2_health = 100
team_health = 100
narootoe_attack = 0.5
sasookee_attack = 1
sakooru_attack = 0.2
sakooru_heal = 0.5
narootoe_attack_count = 6
sasookee_attack_count = 3
sakooru_attack_count = 4
attack_count_stop = 2
narootoe_regen = 1
sakooru_regen = 1
sasookee_regen = 1
wall_list = []

# Frames of different players and attacks
frame_lady = Lady()
frame_old_man = OldMan()
frame_player = SpriteSheetPlayer()
frame_dragon = DragonSprite()
frame_fire = FireBall()
frame_rasengan = Rasengan()
frame_shuriken = Shuriken()

# Background
bg = pg.image.load(os.path.join("pictures", "Grassbackground.jpg"))
bg = pg.transform.scale(bg, (1136 * 3 // 2, 640 * 4 // 3))

# Character declarations and frame assosciation
char_current = frame_player.moving_character()
player = Player(0, 600)

dragon = frame_dragon.fly()
boss = Enemy(1075, 25, frame_fire, 200, 200, 100, 1, 30)

old_man = frame_old_man.move()
mini_boss_1 = Enemy(100, 150, frame_rasengan, 60, 33, 30, 2, 5)

queen = frame_lady.move()
mini_boss_2 = Enemy(650, 150, frame_shuriken, 60, 33, 50, 3, 10)

player_list = [boss, player, mini_boss_1, mini_boss_2]

# variable for attack
attack_moving_p = False

# Start Screen Variables and Functions
start_screen = True
bg_start = pg.image.load(os.path.join("pictures", "lol.jpg"))
bg_start = pg.transform.scale(bg_start, (728 * 9 // 4 , 393 * 9 // 4))
pic = pg.image.load(os.path.join("pictures", "Controls.jpg"))
pic = pg.transform.scale(pic, (1920 * 5 // 9, 1080 * 5 // 9))
far = pg.image.load(os.path.join("pictures", "far.png"))
far = pg.transform.scale(far, (1224 // 2, 792 // 2))

square = pg.Rect(300, 700 , 180, 80)
square1 = pg.Rect(305 , 705, 170, 70)
square4 = pg.Rect(695, 700, 180, 80)
square5 = pg.Rect(700, 705, 170, 70)
square6 = pg.Rect(1125, 700, 180, 80)
square7 = pg.Rect(1130, 705, 170, 70)
square8 = pg.Rect(0, 0, 20, 20)
square10 = pg.Rect(0, 20, 20, 20)

music = True
control = False
def checking():
    global start_screen
    if 0 + 20 > mouse[0] > 0 and 0 + 20 > mouse[1] > 0:
        pg.draw.rect(screen, (255, 191, 127), square8)
        if click[0] == 1:
            pg.mixer.music.pause()
    else:
        pg.draw.rect(screen, (255, 166, 77), square8)

    if 0 + 20 > mouse[0] > 0 and 20 + 20 > mouse[1] > 20:
        pg.draw.rect(screen, (135,206,250), square10)
        if click[0] == 1:
            pg.mixer.music.unpause()
    else:
        pg.draw.rect(screen, (65,105,225), square10)

    if 305 + 170 > mouse[0] > 305 and 705 + 70 > mouse[1] > 705:
        pg.draw.rect(screen, (255, 191, 127), square1)
        if click[0] == 1:
            start_screen = False
    else:
        pg.draw.rect(screen, (255, 166, 77), square1)

    if 700 + 170 > mouse[0] > 700 and 705 + 70 > mouse[1] > 705:
        pg.draw.rect(screen, (255, 191, 127), square5)
        if click[0] == 1:
            screen.blit(pic, (280, 20))
            pg.display.update()

    else:
        pg.draw.rect(screen, (255, 166, 77), square5)

    if 1130 + 170 > mouse[0] > 1130 and 705 + 70 > mouse[1] > 705:
        pg.draw.rect(screen, (255, 191, 127), square7)
        if click[0] == 1:
            exit()
    else:
        pg.draw.rect(screen, (255, 166, 77), square7)

if music:
    pg.mixer.music.load(os.path.join("pictures", "music.mp3"))
    pg.mixer.music.play(-1)



while True:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
    if start_screen:
        # Start screen menu
        click = pg.mouse.get_pressed()
        screen.blit(bg_start, (0, 0))
        screen.blit(far, (480, 20))

        pg.draw.rect(screen, (255, 140, 26), square)
        pg.draw.rect(screen, (255, 166, 77), square1)
        pg.draw.rect(screen, (255, 140, 26), square4)
        pg.draw.rect(screen, (255, 166, 77), square5)
        pg.draw.rect(screen, (255, 140, 26), square6)
        pg.draw.rect(screen, (255, 166, 77), square7)
        pg.draw.rect(screen, (255, 140, 26), square8)
        pg.draw.rect(screen, (65, 105, 225), square10)
        mouse = pg.mouse.get_pos()
        checking()

        text_print(font, 40, "Start", BLACK, 390, 740)
        text_print(font, 40, "Controls", BLACK, 780, 740)
        text_print(font, 40, "Quit", BLACK, 1210, 740)
    elif team_health <= 0:
        text_print(font, 100, "Game Over", RED, screen_width // 2, screen_height // 2)
        pg.mixer.music.stop()
    elif drag_health <= 0:
        text_print(font, 100, "YOU WIN!", GRASS_GREEN, screen_width // 2, screen_height // 2)
        pg.mixer.music.stop()
    elif team_health > 0:
        # Game
        # Draw everything onto the screen
        screen.blit(bg, (0, 0))
        draw_attack()
        map()

        char_current = frame_player.moving_character()
        player.draw(char_current)

        char_bar()

        if drag_health > 0 and game_stage == 3:
            dragon = frame_dragon.fly()
            boss.draw(dragon)
        if mini_boss_1_health > 0 and game_stage == 1:
            old_man = frame_old_man.move()
            mini_boss_1.draw(old_man)
        if mini_boss_2_health > 0 and game_stage == 2:
            queen = frame_lady.move()
            mini_boss_2.draw(queen)

        # Health Bars
        text_print(font, font_size, "Team Health", WHITE, 775, 600)
        health_bar(725, 610, team_health, 100)
        health_bar(1190, 30, drag_health, 250)
        health_bar(200, 30, mini_boss_1_health, 50)
        health_bar(750, 30, mini_boss_2_health, 100)

        # Update the variables with all the changes
        attack_regen()
        game_stage_change()

        # Pause before drawing the next frame
        pg.time.delay(40)

    # Updating after every frame
    pg.display.update()
