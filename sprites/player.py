from sprites.base import Base
from config import config

PLAYER_FRAME_1_SPRITE_PATH = "images/player_frame_1.png"
PLAYER_FRAME_2_SPRITE_PATH = "images/player_frame_2.png"

class Player(Base):
    def __init__(
        self
    ):
        self.player_frames = [
            PLAYER_FRAME_1_SPRITE_PATH,
            PLAYER_FRAME_2_SPRITE_PATH
        ]
        self.player_frame = 0
        
        self.player_frame_cooldown = 200
        self.last_tick = 0
    
        super().__init__(
            self.player_frames[self.player_frame],
            (config.window_size[0] // 2, config.window_size[1] // 2)
        )
    
    def animate(
        self,
        tick: int
    ):
        if tick - self.last_tick < self.player_frame_cooldown:
            return
        
        self.last_tick = tick
    
        self.player_frame += 1
        if self.player_frame >= len(self.player_frames):
            self.player_frame = 0
        
        self.update_visual(self.player_frames[self.player_frame])