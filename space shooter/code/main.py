import pygame
from os.path import join
from random import randint

#general setup 
pygame.init() # initialize everything 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))    # display surface
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 300

# improting an image
player_surf = pygame.image.load(join('space shooter','images', 'player.png')).convert_alpha()    #convert() if image has not transparent pixels, conver_alpha if it has transparent pixel -----make run faster
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
player_direction = pygame.math.Vector2()
player_speed = 300

star_surf = pygame.image.load(join('space shooter', 'images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]   #20 random positions

meteor_surf = pygame.image.load(join('space shooter', 'images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load(join('space shooter', 'images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))


while running:  
    dt = clock.tick() / 1000 #turn into seconds
    # event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print(1)
        # if event.type == pygame.MOUSEMOTION:
        #     player_rect.center = event.pos
            
    #input 
    # print(pygame.mouse.get_rel())
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    player_direction = player_direction.normalize() if player_direction else player_direction
    player_rect.center += player_direction * player_speed * dt

    recent_keys = pygame.key.get_just_pressed()
    if recent_keys[pygame.K_SPACE]:
        print(1)

    # draw the game
    display_surface.fill('darkgray') 
    for pos in star_positions:
        display_surface.blit(star_surf, pos) 
        
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(player_surf, player_rect.topleft)                  # put one surface on another surface (Block image transfer)
    
    pygame.display.update()

pygame.quit() #uninitialize everything

