"""Place in root of Game of Greed Project,
at same level as pyproject.toml
"""
import collections
import builtins
import re
from abc import abstractmethod



from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic


class BasePlayer:
    sum = 0
    def __init__(self):
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print # Methods overriding
        builtins.input = self._mock_input # Methods overriding
        self.total_score = 0

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    # The default behaviour
    @abstractmethod
    def _mock_print(self, *args):
        self.old_print(*args)

    @abstractmethod
    def _mock_input(self, *args):
        return self.old_input(*args)

    @classmethod
    def play(cls, num_games=10):

        mega_total = 0

        for i in range(num_games):
            player = cls()
            game = Game(GameLogic.roll_dice)
            try:
                game.play()
                print ( f'sum = {BasePlayer.sum}')
            except SystemExit:
                pass
            mega_total += player.total_score
            player.reset()

        # if game.total == 0:
        #     rawnaq.play()
        # else:
        #     print(
        #         f"Congrats! {num_games} games (maybe) played with average score of {game.total //( num_games-1)}"
        #     )
        print(
            f"Congrats! {num_games} games (maybe) played with average score of {BasePlayer.sum //num_games}"
        )


class NervousNellie(BasePlayer):
    

    def _mock_print(self, *args):
        self.old_print(*args) 
        printed_data = str(args[0])
        if printed_data[0].isdigit():
            self.rolled_dice = tuple(int(ch) for ch in printed_data.split(','))
            # '2,3,1,2,6,4' ==> (2,3,1,2,6,4)
        if printed_data.startswith('Thanks for playing. You earned'):
            self.total_score = int ((printed_data.replace('Thanks for playing. You earned ','')).replace(' points',''))
            BasePlayer.sum += self.total_score/2
     

    def _mock_input(self, *args):
        self.old_print(*args)
        if args[0].startswith('Wanna play'):
            return 'y'
        elif args[0].startswith('Enter dice'):
            # self.old_print(self.rolled_dice)
            "".join([str(i) for i in self.rolled_dice])
            if 1 in self.rolled_dice:
                return '1'
            elif 5 in self.rolled_dice:
                return '5'
            else:
                return 'q'
        elif args[0].startswith('(r)oll again, (b)ank your points or (q)ui'):
            return 'b'
        else:
            return 'q'

    



if __name__=="__main__":
    rawnaq= NervousNellie()
    rawnaq.play()