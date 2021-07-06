class Settings:
    """A class to store all settings for Game of Life"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (100,100,100)
        # Cell settings
        self.cell_colour = (250,250,250)