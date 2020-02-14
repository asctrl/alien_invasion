class Settings():

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1300
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 250, 10, 10
        self.alien_speed_x = 0.2
        self.alien_speed_y = 10
        self.alien_direction = 1
