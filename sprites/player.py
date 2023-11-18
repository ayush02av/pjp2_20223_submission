from sprites.base import Base
from config import config

PLAYER_FRAME_1_SPRITE_PATH = "images/player_frame_1.png"
PLAYER_FRAME_2_SPRITE_PATH = "images/player_frame_2.png"

class Player(Base):
    def __init__(
        self
    ):
        super().__init__(
            "images/player_frame_1.png",
            (config.window_size[0] // 2, config.window_size[1] // 2),
            (50, 50),
            animation_frames = [
                f"images/player_frame_{i + 1}.png"
                for i in range(2)
            ],
            speed = 18
        )