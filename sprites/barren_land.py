from sprites.base import Base

class BarrenLand(Base):
    def __init__(
        self,
        position: tuple
    ):
        super().__init__(
            "images/barren_land.png",
            position,
            (50, 50)
        )