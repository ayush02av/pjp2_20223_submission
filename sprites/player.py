from sprites.base import Base
from config import config

PLAYER_SPRITE_PATH = "images/player.png"

class Player(Base):
    def __init__(
        self
    ):
        super().__init__(
            PLAYER_SPRITE_PATH,
            (config.window_size[0] // 2, config.window_size[1] // 2)
        )