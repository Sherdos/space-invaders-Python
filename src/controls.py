import pygame, sys, time
from pygame.sprite import Group
from typing import List
from elements.gun import Gun
from elements.bullet import Bullet
from elements.aliens import Alien
from elements.scores import Score
from elements.stats import Stats

def events(screen, gun:Gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # В право
            
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.mright = True
            # В лево
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.mleft = True
            # Стрелять
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # В право
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.mright = False
            # В лево
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.mleft = False

def update_screen(bg_color, screen:pygame.Surface, stats:Stats, sc:Score, gun:Gun, aliens:Alien, bullets:Group):
    # Обновление экрана
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.out_put()
    aliens.draw(screen)
    pygame.display.flip()
    

def update_bullets(screen, stats, sc,aliens, bullets ):
    """Обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
            
    collitions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collitions:
        for aliens in collitions.values():
            stats.score +=10 * len(aliens)
            sc.image_score()
        sc.image_score()
        check_high_score(stats,sc)
        sc.image_guns()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)

def gun_kill(stats, screen, sc, gun, aliens, bullets):
    """Столкновение пушки и армии"""
    if stats.hp > 0:
        stats.hp -= 1
        sc.image_guns()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        gun.create_gun()
        time.sleep(1)
    else:
        sc.show_game_over()
        
        time.sleep(1)
        stats.run_game = False
        sys.exit()
    
def update_aliens( stats,screen,sc, gun, aliens, bullets ):
    """ Обновление позиции пришелцов  """
    aliens.update()
    if pygame.sprite.spritecollideany(gun,aliens):
        gun_kill(stats,screen, sc, gun, aliens,bullets)
    aliens_check(stats,screen,sc, gun, aliens, bullets)


def aliens_check(stats, screen,sc, gun, aliens, bullets):
    """Проверка, пошла ли пришелцы """
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats,screen,sc, gun, aliens, bullets)
            break

def create_army(screen, aliens):
    """Создание армии пришелсов"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_heigth = alien.rect.height
    count_of_aliens_x = int((700 - 2*alien_width ) /  alien_width) 
    count_of_aliens_y = int((700 - 100 - 2*alien_heigth ) /  alien_heigth) 
    for row_number in range(count_of_aliens_y-2):
        for alien_num in range(count_of_aliens_x-1):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_num)
            alien.y = alien_heigth + (alien_heigth * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height*row_number)
            aliens.add(alien)
        
        
def check_high_score(stats, sc):
    """Проверка нового рекорда"""
    
    if stats.score > stats.high_score:
        stats.high_score = stats.score 
        sc.image_high_score()
        with open('./high_score.txt', 'w') as f:
            f.write(str(stats.high_score))