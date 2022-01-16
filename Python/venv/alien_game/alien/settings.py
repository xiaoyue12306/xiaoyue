import pygame.image


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.my_speed = 3
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230,160,60)
        # 子弹允许数
        self.bullet_allowed=3
        self.alien_ship_image=pygame.image.load(r'C:\Users\xyy\Desktop\xy\Python\venv\alien_game\images\alien_ship.bmp')
        self.my_ship_image=pygame.image.load(r'C:\Users\xyy\Desktop\xy\Python\venv\images\my_plane.bmp')
