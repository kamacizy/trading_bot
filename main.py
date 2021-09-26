import robinhood
import reddit

prompt = input('What are you using?').upper()

def MAIN(): 

    if prompt == 'ROBINHOOD':
        robinhood.PROFILE()
    else:
        reddit.REDDIT()

MAIN()