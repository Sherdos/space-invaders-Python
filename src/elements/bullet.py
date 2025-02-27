import pygame

from elements.gun import Gun

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, screen, gun:Gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,12)
        self.color = (168, 230, 29)
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
        
    def update(self):
        """Перемешение пули вверх"""
        self.y -= self.speed    
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Отрисовываем пулю"""
        pygame.draw.rect(self.screen, self.color, self.rect)