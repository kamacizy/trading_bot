import praw
import csv

f = open('count.txt', 'w', encoding='utf-8')
c = csv.reader(open('nasdaq.csv'))

rows = []
for row in c:
    rows.append(row)
#print(rows)

lines = open('secret.txt').read().splitlines()

def REDDIT():
    reddit = praw.Reddit(
        client_id=lines[3],
        client_secret=lines[4],
        username='kamacizy2',
        password=lines[5],
        user_agent="Kamacizy"
    )
    print(reddit.read_only)
    
    for submission in reddit.subreddit("wallstreetbets").hot(limit=100):
        x = str(submission.title).upper().split()
        for y in range(len(x)):
            if len(x[y]) >= 3 or len(x[y]) <= 5:
                #print(x[y])
                for z in range(len(rows)):
                    #print(rows[z], "   ", x[y])
                    if str(rows[z]).upper() == str(x[y]).upper():
                        print(rows[z])
                    #f.write(x[y])
                    #f.write('\n')
                    else:
                        pass
            else:
                pass
        #print("Article mame: ", submission.title, '\n')
#( or x[y] !='the' or x[y] != 'the' or x[y] !='and' or x[y] != 'got')
