from banker import Banker


class Game:
    def __init__(self, roller = None):
        self.round = 0
        self.banker = Banker()
        self.roller = roller
        self.total = 0
    
    def play(self):
        # playing the game:
        # 1.print welcome msg
        # 2.ask if play? (y or n)

        # starting the game:
        # 3.Rolling (start game)
        # 4.ask a choice (dice or q)
        # 5.show round score
        # 6.ask for r(roll), b(bank), or q(quit)
        # 7. if b: go to banking
        # 8. give the user update about his points after every round
        

        # Quitting:
        # 1. show total score
        # 2. thanks msg

        # Banking:
        #   a. save the current score in total
        #   b. show banked points
        #   c. show total score
        #   d. go to step #3 above
        pass



# class Game:
#     def __init__(self, roller= None):
#         self.roller = roller
#         print('Welcome to the Game')

#     def play(self):
#         wanna_play = input('Wanna Play?')
#         if wanna_play == 'n':
#             print('ok maybe another Time')
#         else:
#             print('Starting round 1')
#             print('Rolling 6 dice...')
#             rolled_dice = self.roller(6)
#             nums = []
#             for i in rolled_dice:
#                 nums.append(str(i))
#             print(','.join(nums))
#             decison = input('Input?')


# if __name__=="__main__":
#     game = Game()
#     game.play()
