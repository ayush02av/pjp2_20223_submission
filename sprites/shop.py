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
            (450, 50),
            (80, 80)
        )
    
    def open_shop(self):
        self.update_visual(SHOP_OPEN_SPRITE_PATH)
        self.shop_state = "OPEN"
    
    def close_shop(self):
        self.update_visual(SHOP_CLOSE_SPRITE_PATH)
        self.shop_state = "CLOSED"
    
    def toggle_shop_state(self):
        if self.shop_state == "CLOSED":
            self.open_shop()
        
        elif self.shop_state == "OPEN":
            self.close_shop()