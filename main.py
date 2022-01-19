import sqlite3
from start import main as start
from training import main as training
from settings import main as settings
from pregame import main as pregame
from game import main as game
from end import main as end

while True:
    st = start()
    if st == 'start':
        while True:
            try:
                cur = sqlite3.connect('settings.db').cursor()
                PLAYER1 = cur.execute('SELECT nickname FROM nicknames WHERE id = 1').fetchone()[0]
                PLAYER2 = cur.execute('SELECT nickname FROM nicknames WHERE id = 2').fetchone()[0]
                PLACEMENT1 = pregame(PLAYER1, 1)
                PLACEMENT2 = pregame(PLAYER2, 0)
                # PLACEMENT1 = ([[4, 4, 4, 4, 0, 0, 3, 0, 2, 2],
                #               [0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
                #               [3, 3, 3, 0, 2, 0, 3, 0, 1, 0],
                #               [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                #               [0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
                #               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                #               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                #               [0, 0, 0, 0, 0, 1, 0, 0, 0, 7],
                #               [5, 5, 0, 0, 0, 0, 0, 0, 0, 0],
                #               [5, 5, 0, 0, 0, 0, 0, 0, 0, 6]], )
                #
                # PLACEMENT2 = ([[4, 4, 4, 4, 0, 2, 2, 0, 0, 0],
                #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                #               [3, 3, 3, 0, 1, 0, 0, 0, 0, 0],
                #               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                #               [0, 3, 3, 3, 0, 0, 0, 0, 5, 5],
                #               [0, 0, 0, 0, 0, 0, 0, 0, 5, 5],
                #               [2, 2, 0, 0, 1, 0, 0, 0, 0, 0],
                #               [0, 0, 0, 0, 0, 0, 1, 0, 0, 6],
                #               [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 7]], )
                #sc1, sc2, f1, f2 = game(PLAYER1, PLAYER2, PLACEMENT1, PLACEMENT2)
                end(24, 12, 1, 5, PLAYER1, PLAYER2)
                break
            except ConnectionRefusedError:
                settings()
                continue
    elif st == 'training':
        training()
        continue
    elif st == 'settings':
        settings()
        continue
    elif st == 'quit':
        break
