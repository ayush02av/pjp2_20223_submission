from sprites.base import Base
from config import config

SHOP_CLOSE_SPRITE_PATH = "images/shop_close.png"
SHOP_OPEN_SPRITE_PATH = "images/shop_open.png"

class Shop(Base):
    def __init__(
        self
    ):
        self.shop_state = "CLOSED"

        super().__init__(
            SHOP_CLOSE_SPRITE_PATH,
            (config.window_size[0] // 2, config.window_size[1] // 2)
        )
    
    def toggle_shop_state(
        self
    ):
        if self.shop_state == "CLOSED":
            self.update_visual(SHOP_OPEN_SPRITE_PATH)
            self.shop_state = "OPEN"
        
        elif self.shop_state == "OPEN":
            self.update_visual(SHOP_CLOSE_SPRITE_PATH)
            self.shop_state = "CLOSED"