import sys
import pygame
from bullet import Bullet
from alien import Alien

# 监视键盘和鼠标事件
def check_events(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, screen, ship, bullets)

def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False


def update_bullets(settings, screen, ship, bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_collision(settings, screen, ship, bullets, aliens)

def check_collision(settings, screen, ship, bullets, aliens):
    pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        create_aliens(settings, screen, ship, bullets, aliens)


def create_aliens(settings, screen, ship, bullets, aliens):
    alien = Alien(settings, screen)
    alien_number_x = get_alien_number_x(settings, screen, alien.rect.width)
    alien_number_y = get_alien_number_y(settings, screen, alien.rect.height, ship.rect.height)
    for y_num in range(alien_number_y):
        for x_num in range(alien_number_x):
            create_alien(settings, screen, aliens, x_num, y_num)

def get_alien_number_x(settings, screen, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    return int(available_space_x / (alien_width * 2))

def get_alien_number_y(settings, screen, alien_height, ship_height):
    available_space_y = settings.screen_height - 3 * alien_height - ship_height
    return int(available_space_y / (alien_height * 2))

def create_alien(settings, screen, aliens, x_num, y_num):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * x_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + y_num  * alien.rect.height * 2
    aliens.add(alien)

def update_aliens(settings, aliens, ship):
    if pygame.sprite.spritecollideany(ship, aliens):
        print('ship hit!!!')
    check_alien_edges(settings, aliens)
    aliens.update()

def check_alien_edges(settings, aliens):
    for alien in aliens:
        if alien.check_edges():
            change_alien_direction(settings, aliens)
            break

def change_alien_direction(settings, aliens):
    for alien in aliens:
        alien.rect.y += settings.alien_speed_y
    settings.alien_direction *= -1


def update_screen(settings, screen, ship, bullets, aliens):
    screen.fill(settings.bg_color)

    for bullet in bullets:
        bullet.draw_bullet()
    ship.move()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()
