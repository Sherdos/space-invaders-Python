import pygame

class Alien(pygame.sprite.Sprite):
    """Класс пришелца"""
    
    
    def __init__(self, screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('./media/image/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def draw(self):
        """Отресовка пришелца"""
        self.screen.blit(self.image, self.rect)
        
        
    def update(self):
        """Перемежение на пушку"""
        self.y += 0.1
        self.rect.y = self.y