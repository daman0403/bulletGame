from numpy import void
import pygame
from random import randint

       

pygame.init()
clock=pygame.time.Clock()
gravity=0

shooting=0

Screen = pygame.display.set_mode((550,350))
pygame.display.set_caption("Daman's game")
sky=pygame.image.load('graphics/sky.png')
ground=pygame.image.load('graphics/ground.png')

player_shoot=pygame.image.load('graphics/playerShoot.png')
player_shoot=pygame. transform. scale(player_shoot, (40, 60))
player_shoot_rect=player_shoot.get_rect(midbottom=(50,250))


bullet=pygame.image.load('graphics/bullet3.png')
bullet=pygame.transform.scale(bullet,(10,20))
bullet_rect=bullet.get_rect(midtop=(player_shoot_rect.right+2,player_shoot_rect.bottom-40))

game_active=True


while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_SPACE :
                        gravity=-8
                    if events.key==pygame.K_a:
                        shooting+=15
                    if events.key==pygame.K_x:
                        shooting-=2                      
                   

                        
                        



    if game_active:
        Screen.blit(sky,(0,-50))
        Screen.blit(ground,(0,250))
        Screen.blit(player_shoot,player_shoot_rect)
        gravity+=0.7
        player_shoot_rect.y+=gravity
        if player_shoot_rect.bottom>=250:
            player_shoot_rect.bottom=250

        if player_shoot_rect.y<=0:
            player_shoot_rect.y=0

        Screen.blit(bullet,(bullet_rect))
        bullet_rect.y+=gravity
        if bullet_rect.top>=player_shoot_rect.bottom-40:
            bullet_rect.top=player_shoot_rect.bottom-40
        if bullet_rect.y<=player_shoot_rect.bottom-40:
            bullet_rect.y=player_shoot_rect.bottom-40

        bullet_rect.x+=shooting
        if bullet_rect.x>=550:
            bullet_rect.x=player_shoot_rect.right+2
        if shooting<=6:
            bullet_rect.x=player_shoot_rect.right+2
        if shooting>=45:
            shooting=5

    


    pygame.display.update()
    clock.tick(60)
