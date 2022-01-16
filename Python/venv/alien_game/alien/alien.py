import pygame,sys
from pygame.sprite import Sprite

class Alien(Sprite):
    # 表示单个外星人的类
    def __init__(self,settings,screen):
        # 初始化外星人，并设置其位置
        super().__init__()
        self.screen=screen
        self.settings=settings
        # 加载外星人图像
        self.image=settings.alien_ship_image
        self.rect=self.image.get_rect()
        # 每个外星人的位置都在屏幕左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image,self.rect)
