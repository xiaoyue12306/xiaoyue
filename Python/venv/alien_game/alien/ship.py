import pygame

class Ship():
    def __init__(self,screen,settings):
        # 初始化飞船并设置初始位置
        self.screen=screen
        self.settings=settings
        # 加载飞船图像并获取其外接矩形
        self.image=settings.my_ship_image
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.my_speed=settings.my_speed
        # 将飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.center=self.screen_rect.center
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up=False
        self.moving_down = False

    def blitme(self):
        # 在指定位置放置飞船
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.my_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -=self.my_speed
        if self.moving_up and self.rect.top<self.screen_rect.top:
            self.rect.center += self.my_speed