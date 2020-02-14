import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():

    settings = Settings()
    # 初始化屏幕
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen, settings)
    bullets = Group()
    aliens = Group()
    gf.create_aliens(settings, screen, ship, bullets, aliens)

    #开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(settings, screen, ship, bullets)
        gf.update_bullets(settings, screen, ship, bullets, aliens)
        gf.update_aliens(settings, aliens, ship)
        #更新屏幕
        gf.update_screen(settings, screen, ship, bullets, aliens)

run_game()
