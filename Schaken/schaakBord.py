import numpy as np

class SchaakBord():
    def __init__(self):
        self.playerToMove = 'WHITE'
        self.bord = np.array([
            ['ZR', 'ZN', 'ZB', 'ZQ', 'ZK', 'ZB', 'ZN', 'ZR'],
            ['ZP', 'ZP', 'ZP', 'ZP', 'ZP', 'ZP', 'ZP', 'ZP'],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
            ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        ])

    def changePlayer(self):
        if self.playerToMove == 'WHITE':
            self.playerToMove == 'BLACK'
        else:
            self.playerToMove == 'WHITE'
