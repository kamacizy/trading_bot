import robinhood
import reddit

prompt = input('What are you using?\n').upper()

def MAIN(): 

    if prompt == 'ROBINHOOD':
        robinhood.PROFILE()
    else:
        reddit.CROSS_CHECK()

MAIN()