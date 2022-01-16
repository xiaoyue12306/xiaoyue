import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,settings,screen,ship):
        # 在飞船位置处创建一个子弹对象
        super().__init__()
        self.screen=screen

        # 在00处创建一个子弹矩形，并设置位置
        self.rect=pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        self.y=float(self.rect.y)
        self.color=settings.bullet_color
        self.bullet_speed=settings.bullet_speed


    def update(self):
        self.y -= self.bullet_speed
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

    def remove_bullet(bullets):
        for bullet in bullets:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)