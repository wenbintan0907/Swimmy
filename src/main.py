import pygame
import random
import os

ASSET_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets'))

# Set up the Bubble's brain
class Bubble():
    # Bubble construtor function
    def __init__(self, x, y):
        # Make the enemy's variables
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.pic = pygame.image.load(os.path.join(ASSET_DIR, "Bubble.png"))
        self.on_screen = True

        # Shrink the bubble down
        self.pic = pygame.transform.scale(self.pic, (15, 15))
    
    # Bubble update function
    def update(self, screen):
        self.y -= self.speed
        screen.blit(self.pic, (self.x, self.y))
        
        if self.y < 0 - 15:
            self.on_screen = False 

# End of Bubble class

# Set up the Enemy's brain 
class Enemy():
    # Enemy constructor function
    def __init__(self, x, y, speed, size):
        # Make the enemy's variables
        self.x = x
        self.y = y
        self.type = random.randint(0, 3)
        if self.type == 0:
            self.pic = pygame.image.load(os.path.join(ASSET_DIR, "Fish01_A.png"))
            self.pic2 = pygame.image.load(os.path.join(ASSET_DIR, "Fish01_B.png"))
        if self.type == 1:
            self.pic = pygame.image.load(os.path.join(ASSET_DIR, "Fish02_A.png"))
            self.pic2 = pygame.image.load(os.path.join(ASSET_DIR, "Fish02_B.png"))
        if self.type == 2:
            self.pic = pygame.image.load(os.path.join(ASSET_DIR, "Fish03_A.png"))
            self.pic2 = pygame.image.load(os.path.join(ASSET_DIR, "Fish03_B.png"))
        if self.type == 3:
            self.pic = pygame.image.load(os.path.join(ASSET_DIR, "Fish04_A.png"))
            self.pic2 = pygame.image.load(os.path.join(ASSET_DIR, "Fish04_B.png"))
        self.speed = speed
        self.size = size
        self.hitbox = pygame.Rect(self.x, self.y, int(self.size*1.25), self.size)
        self.animation_timer_max = 15
        self.animation_timer = self.animation_timer_max
        self.animation_frame = 0

        # Shrink the enemy pic
        self.pic = pygame.transform.scale(self.pic, (int(self.size*1.25), self.size))
        self.pic2 = pygame.transform.scale(self.pic2, (int(self.size*1.25), self.size))

        # Flip the pic if the enemy is moving to left
        # True to flip horizontally
        # False to flip vertically
        # True, True to flip both horizontally and vertically
        # False, True to flip vertically
        # True, False to flip horizontally
        if self.speed < 0:
            self.pic = pygame.transform.flip(self.pic, True, False)
            self.pic2 = pygame.transform.flip(self.pic2, True, False)
    
    # Enemy update function (stuff to happen over and over again)
    def update(self, screen):
        self.animation_timer -= 1
        if self.animation_timer <= 0:
            self.animation_timer = self.animation_timer_max
            self.animation_frame += 1
            if self.animation_frame > 1:
                self.animation_frame = 0
        self.x += self.speed
        self.hitbox.x += self.speed
        # pygame.draw.rect(screen, (255, 0, 255), self.hitbox)
        if self.animation_frame == 0:
            screen.blit(self.pic, (self.x, self.y))
        else:
            screen.blit(self.pic2, (self.x, self.y))
        
# End of Enemy class

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

# Load all the required pictures
background_pic_A = pygame.image.load(os.path.join(ASSET_DIR, "Scene_A.png"))
background_pic_B = pygame.image.load(os.path.join(ASSET_DIR, "Scene_B.png"))
player_pic = pygame.image.load(os.path.join(ASSET_DIR, "wenxi.png"))
player_pic2 = pygame.image.load(os.path.join(ASSET_DIR, "wenxi2.png"))
player_eating_pic = pygame.image.load(os.path.join(ASSET_DIR, "wenxi_open.png"))

# Make some variables for background animation
background_animation_timer_max = 25
background_animation_timer = background_animation_timer_max
background_animation_frame = 0

# Make some varibles for our player
player_starting_x = 480
player_starting_y = 310
player_starting_size = 30
player_x = player_starting_x
player_y = player_starting_y
player_size = player_starting_size
player_speed = 0.3
player_speed_x = 0
player_speed_y = 0
player_facing_left = False
player_hitbox = pygame.Rect(player_x, player_y, int(player_size * 1.25), player_size)
player_alive = False

# Make some variables for the player_animation
player_eating_timer_max = 15
player_eating_timer = 0
player_swimming_timer_max = 15
player_swimming_timer = player_swimming_timer_max
player_swimming_frame = 0

# Make some variables for the HUD (heads-up display)
score = -1
score_font = pygame.font.SysFont("default", 30)
score_text = score_font.render("Score: "+str(score), 1, (255, 255, 255))
final_text = score_font.render("Final Score: "+str(score), 1, (255, 255, 255))
play_button_pic =  pygame.image.load(os.path.join(ASSET_DIR, "BtnPlayIcon.png"))
play_button_x = game_width/2 - play_button_pic.get_width()/2
play_button_y = game_height/2 - play_button_pic.get_height()/2 + 50
title_pic = pygame.image.load(os.path.join(ASSET_DIR, "Title.png"))
title_x = game_width/2 - title_pic.get_width()/2
title_y = play_button_y - 150

# Make the enemy spawning timer
enemy_timer_max = 40
enemy_timer = enemy_timer_max

# Make the enemies array
enemies = []
enemies_to_remove = []

# Make the bubbles array and timer
bubbles = []
bubbles_to_remove = []

bubble_timer = 0

# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Check to see what key player is pressing
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_speed_x += player_speed
    if keys[pygame.K_LEFT]:
        player_speed_x -= player_speed
    if keys[pygame.K_DOWN]:
        player_speed_y += player_speed
    if keys[pygame.K_UP]:
        player_speed_y -= player_speed
    
    # Make the player slow down over time
    if player_speed_x > 1:
        player_speed_x -= 0.1
    if player_speed_x < -1:
        player_speed_x += 0.1
    if player_speed_y > 1:
        player_speed_y -= 0.1
    if player_speed_y < -1:
        player_speed_y += 0.1

    # Move the player
    player_x += player_speed_x
    player_y += player_speed_y

    # Figure out whether or not to flip the player
    if player_speed_x > 0:
        player_facing_left = False
    else:
        player_facing_left = True

    # Stop the player from leaving the screen
    if player_x < 0:
        player_x = 0
        player_speed_x = 0
    if player_x > game_width - player_size*1.25:
        player_x = game_width - player_size*1.25
        player_speed_x = 0
    if player_y < 0:
        player_y = 0
        player_speed_y = 0
    if player_y > game_height - player_size:
        player_y = game_height - player_size
        player_speed_y = 0
    
    # Do the background animation timer
    background_animation_timer -= 1
    if background_animation_timer <= 0:
        background_animation_frame += 1
        if background_animation_frame > 1:
            background_animation_frame = 0
        background_animation_timer = background_animation_timer_max

    if background_animation_frame == 0:
        screen.blit(background_pic_A, (0, 0))
    else:
        screen.blit(background_pic_B, (0, 0))

    # Spawn a new timer enemy_timer hits 0
    enemy_timer -= 1
    if enemy_timer <= 0:
        new_enemy_y = random.randint(0, game_height)
        new_enemy_speed = random.randint(2, 5)
        new_enemy_size = random.randint(int(player_size/2), int(player_size*2))
        if random.randint(0, 1) == 0:
            enemies.append(Enemy(-new_enemy_size*2, new_enemy_y, new_enemy_speed, new_enemy_size))
        else:
            enemies.append(Enemy(game_width, new_enemy_y, -new_enemy_speed, new_enemy_size))
            
        enemy_timer = enemy_timer_max
        
    for enemy in enemies_to_remove:
        enemies.remove(enemy)
    enemies_to_remove = []

    # Update all the enemies
    for enemy in enemies:
        enemy.update(screen)
        if enemy.x < -1000 or enemy.x > game_width + 1000:
            enemies_to_remove.append(enemy)

    # Make a new bubble when the bubble timer reaches 0
    bubble_timer -= 1
    if bubble_timer <= 0 and player_alive:
        if player_facing_left:
            bubbles.append(Bubble(player_x, player_y))
        else:
            bubbles.append(Bubble(player_x + player_size*1.25, player_y))
        bubble_timer = random.randint(40, 90)
        
    # Update all the bubbles
    for bubble in bubbles:
        if bubble.on_screen:
            bubble.update(screen)
        else:
            bubbles_to_remove.append(bubble)

    # Remove the bubbles in bubbles_to_remove
    for bubble in bubbles_to_remove:
        bubbles.remove(bubble)
    bubbles_to_remove = []

    if player_alive:
        # Update the enemy hibox
        player_hitbox.x = player_x
        player_hitbox.y = player_y
        player_hitbox.width = int(player_size*1.25)
        player_hitbox.height = player_size
        # pygame.draw.rect(screen, (255, 255, 255), player_hitbox)

        # Check to see when the player hits an Enemy
        for enemy in enemies:
            if player_hitbox.colliderect(enemy.hitbox):
                if player_size >= enemy.size:
                    player_size += 2
                    enemies.remove(enemy)
                    score += enemy.size
                    player_eating_timer = player_eating_timer_max
                else:
                    player_alive = False
                    score == score
                    
        # Do the player swimming timer animation
        player_swimming_timer -= 1
        if player_swimming_timer <= 0:
            player_swimming_timer = player_swimming_timer_max
            player_swimming_frame += 1
            if player_swimming_frame > 1:
                player_swimming_frame = 0

        # Draw the player pic
        if player_eating_timer > 0:
            player_pic_small = pygame.transform.scale(player_eating_pic, (int(player_size*1.25), player_size))
            player_eating_timer -= 1
        else:
            if player_swimming_frame == 0:
                player_pic_small = pygame.transform.scale(player_pic, (int(player_size*1.25), player_size))
            else:
                player_pic_small = pygame.transform.scale(player_pic2, (int(player_size*1.25), player_size))
        if player_facing_left:
            player_pic_small = pygame.transform.flip(player_pic_small, True, False)
        screen.blit(player_pic_small, (player_x, player_y))

    # Draw the score text
    if player_alive:
        screen.blit(score_text, (30, 30))
        score_text = score_font.render("Score: "+str(score), 1, (255, 255, 255))
    else:
        final_text = score_font.render("Final Score: "+str(score), 1, (255, 255, 255))
        if score >= 0:
            screen.blit(final_text, (30, 30))
        
    # Draw the menu when the player is dead
    if not player_alive:
        screen.blit(play_button_pic, (play_button_x, play_button_y))
        screen.blit(title_pic, (title_x, title_y))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Check to see if the player clicks the play button
        if pygame.mouse.get_pressed()[0]:
            if mouse_x > play_button_x and mouse_x < play_button_x+play_button_pic.get_width():
                if mouse_y > play_button_y and mouse_y < play_button_y+play_button_pic.get_height():
                    # Restart the game
                    player_alive = True
                    score = 0
                    player_x = player_starting_x
                    player_y = player_starting_y
                    player_size = player_starting_size
                    player_speed_x = 0
                    player_speed_y = 0
                    for enemy in enemies:
                        enemies_to_remove.append(enemy)
                    
    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
