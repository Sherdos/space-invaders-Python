import pygame, controls
from elements.gun import Gun
from elements.stats import Stats
from elements.scores import Score


from pygame.sprite import Group

# class Game():
    
#     def __init__(self,):
    

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    sc = Score(screen,stats)
    
    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update_screen(bg_color, screen, stats, sc, gun, aliens, bullets)
            controls.update_bullets(screen, stats, sc, aliens, bullets)
            controls.update_aliens(stats,screen, sc, gun,aliens,bullets)
        
        

run()