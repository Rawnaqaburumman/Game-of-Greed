from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic

class Game:
    gameBank= Banker()
    def __init__(self, roller=None): self.roller, self.round = roller, 1

    def roll_dice_play(self):
        print('Rolling 6 dice...')
        dice = self.roller(6)
        printableDice = ','.join([str(d) for d in dice])
        print(printableDice)
        keepOrQuit = input("Enter dice to keep (no spaces), or (q)uit: ")
        if keepOrQuit == 'q': self.userQuit()
        else:
            userChoice = self.user_choice_to_tuple(keepOrQuit)
            self.gameBank.shelf(userChoice)
            print(f'You have {userChoice} unbanked points and 5 dice remaining')
            userInput22 = input('(r)oll again, (b)ank your points or (q)uit ')
            self.userChoTwo(userInput22)

    def user_choice_to_tuple(self,userInput):
            List=list(userInput)
            intValue=[int(x)for x in List ]
            rollingScore=GameLogic.calculate_score(tuple(intValue))
            return rollingScore

    def userQuit(self):
        if self.gameBank.balance != 0:
            print(f"Total score is {self.gameBank.balance} points")
        print(f'Thanks for playing. You earned {self.gameBank.balance} points')

    def userChoTwo(self,userChoice):
        if userChoice == 'r':
                self.roll_dice_play()
        elif userChoice =='b':
            print(f'You banked {self.gameBank.shelved} points in round {self.round}')
            self.gameBank.bank()
            print(f'Total score is {self.gameBank.balance} points')
            self.round+=1
            self.rolling()
        elif userChoice == 'q':
            self.userQuit()

    def rolling(self):
            print(f'Starting round {self.round}')
            self.roll_dice_play()
  
                
    def play(self):
        print("Welcome to Game of Greed")
        userInput = input("Wanna play? ")
        if userInput == 'n':
            print("OK. Maybe another time")
        else:
            self.rolling()

if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()