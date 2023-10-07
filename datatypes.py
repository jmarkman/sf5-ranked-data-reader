from enum import Enum

class GameResult(Enum):
    WIN = 0,
    LOSS = 1

    @staticmethod
    def from_str(val: str):
        if val.lower() == "w":
            return GameResult.WIN
        elif val.lower() == "l":
            return GameResult.LOSS
        else:
            raise NotImplementedError
        
class RankedMatch:
    def __init__(self, points: int, result: GameResult, opponent: str, replay_id: str) -> None:
        self.points = points
        self.result = result
        self.opponent = opponent
        self.replay_id = replay_id

class RankedSession:
    def __init__(self, date: str, points_start: int, points_end: int, matches: list[RankedMatch]) -> None:
        self.date = date
        self.points_start = points_start
        self.points_end = points_end
        self.matches = matches