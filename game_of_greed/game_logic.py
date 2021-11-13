import random
class GameLogic:
    def roll_dice(input):
        return tuple(random.randint(1,6) for _ in range(0,input))

    def calculate_score(shelved):
            rules =[
            (tuple(), 0),
            ((1,), 100),
            ((1, 1), 200),
            ((1, 1, 1), 1000),
            ((1, 1, 1, 1), 2000),
            ((1, 1, 1, 1, 1), 3000),
            ((1, 1, 1, 1, 1, 1), 4000),
            ((2,), 0),
            ((2, 2), 0),
            ((2, 2, 2), 200),
            ((2, 2, 2, 2), 400),
            ((2, 2, 2, 2, 2), 600),
            ((2, 2, 2, 2, 2, 2), 800),
            ((3,), 0),
            ((3, 3), 0),
            ((3, 3, 3), 300),
            ((3, 3, 3, 3), 600),
            ((3, 3, 3, 3, 3), 900),
            ((3, 3, 3, 3, 3, 3), 1200),
            ((4,), 0),
            ((4, 4), 0),
            ((4, 4, 4), 400),
            ((4, 4, 4, 4), 800),
            ((4, 4, 4, 4, 4), 1200),
            ((4, 4, 4, 4, 4, 4), 1600),
            ((5,), 50),
            ((5, 5), 100),
            ((5, 5, 5), 500),
            ((5, 5, 5, 5), 1000),
            ((5, 5, 5, 5, 5), 1500),
            ((5, 5, 5, 5, 5, 5), 2000),
            ((6,), 0),
            ((6, 6), 0),
            ((6, 6, 6), 600),
            ((6, 6, 6, 6), 1200),
            ((6, 6, 6, 6, 6), 1800),
            ((6, 6, 6, 6, 6, 6), 2400),
            ((1, 2, 3, 4, 5, 6), 1500),
            ((2, 2, 3, 3, 4, 6), 0),
            ((2, 2, 3, 3, 6, 6), 1500),
            ((1, 1, 1, 2, 2, 2), 1200),
            ((1,5),150),
            ((5, 5, 5, 2, 2, 3),500),
            ((1, 1, 1, 2, 3, 4),1000),
            ((1, 1, 1, 5),1050),
            ((1, 6, 3, 2, 5, 4),1500),
            ((1, 1, 2, 2, 3, 3),1500),
            ((4, 4, 4, 4, 1),900)
        ]
            for i,value in rules:
                if shelved == i:
                    return value
