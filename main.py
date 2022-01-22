import sqlite3
from start import main as start
from pretraining import main as pretraining
from training import main as training
from settings import main as settings
from pregame import main as pregame
from game import main as game
from end import main as end

cur = sqlite3.connect('settings.db').cursor()
PLAYER1 = cur.execute('SELECT nickname FROM nicknames WHERE id = 1').fetchone()[0]
PLAYER2 = cur.execute('SELECT nickname FROM nicknames WHERE id = 2').fetchone()[0]

while True:
    st = start()
    if st == 'start':
        while True:
            try:
                PLACEMENT1 = pregame(PLAYER1, 1)
                PLACEMENT2 = pregame(PLAYER2, 0)
                a = game(PLAYER1, PLAYER2, PLACEMENT1, PLACEMENT2)
                break
            except ConnectionRefusedError:
                settings()
                continue
    elif st == 'training':
        lvl = pretraining()
        if lvl == 'quit':
            continue
        a = training(lvl)
    elif st == 'settings':
        settings()
        continue
    elif st == 'quit':
        break
    print(a)
    end()
