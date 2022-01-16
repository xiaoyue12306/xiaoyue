import pygame
import sys
from bullet import Bullet
from alien import Alien

# 按下检测
def check_keydown_events(event,settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        print('➡')
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        print('⬅')
        ship.moving_left = True
    if event.key==pygame.K_SPACE:
        print('空格')
        fire_bullets(settings,screen,ship,bullets)
    if event.key == pygame.K_UP:
        print('⬆')
        ship.moving_up =True
    if event.key == pygame.K_DOWN:
        print('⬇')
        ship.moving_down = True
# 松开检测
def check_keyup_events(ship,event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #     根据按下松开调整移动开关
        elif event.type ==pygame.KEYDOWN:
            check_keydown_events(event,settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship,event)

def update_screen(settings,screen,ship,aliens,bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # aliens.blitme()
    aliens.draw(screen)
    ship.blitme()

    pygame.display.flip()

def fire_bullets(settings,screen,ship,bullets):
    # 射击
    bullet_allowed = settings.bullet_allowed
    if len(bullets) < bullet_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(settings,screen,aliens):
    # 创建外星人群
    alien=Alien(settings,screen)
    number_aliens_x=get_number_aliens_x(settings,alien.rect.width)

    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(settings,screen,aliens,alien_number)

def get_number_aliens_x(settings,alien_width):
    # 计算可容纳的外星人数量
    available_space_x=settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(settings,screen,aliens,alien_number):
    # 创建一个外星人
    alien = Alien(settings, screen)
    alien_width=alien.rect.width
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    aliens.add(alien)