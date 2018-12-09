from datetime import datetime

odds=range(1,77,2)

right_this_minute=datetime.today().minute

def odd_clock(x):
    if right_this_minute in odds:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute.')
odd_clock(right_this_minute)