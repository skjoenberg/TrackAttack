def state(key):
    state_consts = {
        'drawn_self' : '^\[Zone.*\[name=(.*) id=.*zone=(HAND).*FRIENDLY DECK',
        'game_begin' : '^\[Bob\] legend',
        'turn' : r'^\[Zone.*change=powerTask.*tag=NEXT_STEP value=MAIN_ACTION',
        'played_self' : r'^\[Zone.*tag=JUST\_PLAYED.*\[name=(?P<name>.*) id=.*zone=(PLAY).* player=1',
        'played_oppo' : r'^\[Zone.*tag=JUST\_PLAYED.*\[name=(?P<name>.*) id=.*zone=(PLAY).* player=2'
    }

    return state_consts[key]
