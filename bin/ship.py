import pygame

class Ship():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def move(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.ship_speed
        elif self.move_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.ship_speed
        elif self.move_up and self.rect.top >= 0:
            self.rect.centery -= self.settings.ship_speed
        elif self.move_down and self.rect.bottom <= self.settings.screen_height:
            self.rect.centery += self.settings.ship_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

