import pygame.font
from pygame.sprite import Group
from elements.gun import Gun

class Score():
    """Вывод игровой статистики"""
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (168, 230, 29)
        self.font = pygame.font.SysFont(None, 36,)
        self.font_game_over = pygame.font.SysFont(None, 60,)
        self.image_score()
        self.image_high_score()
        self.image_guns()
        self.game_over()
    
    def image_high_score(self):
        """преобразовывает текст счета в фото"""
        self.high_score_img  = self.font.render(str(self.stats.high_score), True, self.text_color, (0,0,0))
        self.high_score_rect = self.score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20
    
    
    def image_score(self):
        """преобразовывает текст счета в фото"""
        self.score_img  = self.font.render(str(self.stats.score), True, self.text_color, (0,0,0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20
    
    def game_over(self):
        """Игра окончена"""
        
        self.game_over_img  = self.font_game_over.render('Игра окончена', True, self.text_color, (0,0,0))
        self.game_over_rect = self.game_over_img.get_rect()
        self.game_over_rect.centerx = self.screen_rect.centerx
        self.game_over_rect.top = self.screen_rect.top + 20
        
    
    def image_guns(self):
        '''Количество жизней'''
        self.guns = Group()
        for gun_num in range(self.stats.hp):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_num * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)
    
    def show_score(self):
        """Ввывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.guns.draw(self.screen)
    
    def show_game_over(self):
        self.screen.blit(self.game_over_img, self.game_over_rect)
        self.guns.draw(self.screen)
        



