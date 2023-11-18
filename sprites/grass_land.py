from sprites.base import Base
from config import config
import random

class GrassLand(Base):
    def __init__(
        self,
        position: tuple
    ):
        animation_frames = [
            f"images/grass_frame_{i + 1}.png"
            for i in range(4)
        ]

        super().__init__(
            random.choice(animation_frames),
            position,
            (50, 50),
            animation_frames = animation_frames,
            animation_frame_cooldown = random.randint(195, 205)
        )