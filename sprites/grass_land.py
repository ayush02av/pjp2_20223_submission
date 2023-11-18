from sprites.base import Base
from config import config

class GrassLand(Base):
    def __init__(
        self
    ):
        super().__init__(
            "images/grass_frame_1.png",
            (config.window_size[0] // 2, config.window_size[1] // 2),
            animation_frames = [
                f"images/grass_frame_{i + 1}.png"
                for i in range(4)
            ],
            animation_frame_cooldown = 150
        )