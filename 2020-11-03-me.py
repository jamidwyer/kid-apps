#!/usr/bin/python
import praw
import pdb
import re
import os

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

local_subs = open("maine.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['super tuesday', 'flip the senate', 'maine to allowed ranked vot', \
                '20 republican senators', \
                'nervous republicans', 'maine families face elder boom', 'STATES WITH MORE GUN OWNERS HAVE MORE MURDERS IN THE HOME', 'donations to senate republicans', 'armbands come next', 'sara gideon', 'war against free and fair elections', 'Maine inches closer to shutting down', 'susan collins', 'maine prison', 'outbreak spreads to maine', 'maine lawmaker', 'first state to ban styrofoam', 'wave of clean energy legislation', 'maine senate', 'me-gov', 'Maine Democratic Senate', 'maine vot', 'maine gop', 'maine state house', 'maine election', 'maine house candidate', 'eryn gilchrist', 'steve deangelis', 'mainepolitics', 'mainegreens', 'maine gov', 'Maine town councilor', 'maine\'s governor', 'Maine State Representative', 'lepage', 'ME\'s next governor ', 'governor of maine', 'me governor\'s', 'gov. lepage']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Maine Election 2020 \n\n"
            "[Register to Vote](https://www.maine.gov/sos/cec/elec/voter-info/voterguide.html) \n\n"
            "[Primary Election](https://www1.maine.gov/portal/government/edemocracy/voter_lookup.php): March 3, 2020 \n\n"
            "[General Election](https://www1.maine.gov/portal/government/edemocracy/voter_lookup.php): November 3, 2020 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()