import praw
import csv

f = open('count.csv', 'w', encoding='utf-8')
c = csv.reader(open('nasdaq_w$.csv'))

rows = []
for row in c:
    rows.append(row)

lines = open('secret.txt').read().splitlines()

reddit = praw.Reddit(
        client_id=lines[3],
        client_secret=lines[4],
        username='kamacizy2',
        password=lines[5],
        user_agent="Kamacizy"
    )

def CROSS_CHECK():
        
    chosen_subreddit=input('What subreddit are you cross-checking?\n').upper()
    chosen_sort=input('What sort are you cross-checking with?\n[HOT, RELEVANCE, NEW, RISING, COMMENTS]\n').upper()
    sample_size=int(input('What sample size would you like?\n'))

    if chosen_sort=='HOT':
        for submission in reddit.subreddit(chosen_subreddit).hot(limit=sample_size):
            x = str(submission.title).upper().split()
            for y in range(len(x)):
                if len(x[y]) in range(3,6):
                    for z in range(len(rows)):
                        #turns rows into a str and compares
                        if ''.join(rows[z]).upper() == x[y].upper():
                            print(rows[z])
                        else:
                            pass
                else:
                    pass
    elif chosen_sort=='RELEVANCE':
        for submission in reddit.subreddit(chosen_subreddit).relevance(limit=sample_size):
            x = str(submission.title).upper().split()
            for y in range(len(x)):
                if len(x[y]) in range(3,6):
                    for z in range(len(rows)):
                        #turns rows into a str and compares
                        if ''.join(rows[z]).upper() == x[y].upper():
                            print(rows[z])
                        else:
                            pass
                else:
                    pass
    elif chosen_sort=='NEW':
        for submission in reddit.subreddit(chosen_subreddit).new(limit=sample_size):
            x = str(submission.title).upper().split()
            for y in range(len(x)):
                if len(x[y]) in range(3,6):
                    for z in range(len(rows)):
                        #turns rows into a str and compares
                        if ''.join(rows[z]).upper() == x[y].upper():
                            f. write(''.join(rows[z]).upper())
                            f. write('\n')
                        else:
                            pass
                else:
                    pass
    elif chosen_sort=='RISING':
        for submission in reddit.subreddit(chosen_subreddit).rising(limit=sample_size):
            x = str(submission.title).upper().split()
            for y in range(len(x)):
                if len(x[y]) in range(3,6):
                    for z in range(len(rows)):
                        #turns rows into a str and compares
                        if ''.join(rows[z]).upper() == x[y].upper():
                            print(rows[z])
                        else:
                            pass
                else:
                    pass
    #TODO fix this dumb crap to work on comments, it's currently looking at submission title which obv wouldn't work for comments
    else:
        for submission in reddit.subreddit(chosen_subreddit).comments(limit=sample_size):
                x = str(submission.title).upper().split()
                for y in range(len(x)):
                    if len(x[y]) >= 3 or len(x[y]) <= 6:
                        for z in range(len(rows)):
                            #turns rows into a str and compares
                            if ''.join(rows[z]).upper() == x[y].upper():
                                print(rows[z])
                            else:
                                pass
                    else:
                        pass

