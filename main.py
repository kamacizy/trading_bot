import robinhood
import reddit
import twitter

prompt = input('What you want?')

def MAIN(): 

    if prompt == 'ROBINHOOD':
        robinhood.PROFILE()
    elif prompt == 'REDDIT':
        reddit.CROSS_CHECK()
    else:  
        twitter.search()





MAIN()