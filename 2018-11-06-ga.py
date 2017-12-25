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

local_subs = open("georgia.dat", "r")
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
            terms = ['Journalist found guilty of obstruction of justice after suing Sheriff Candidate', 'In Georgia, battle of the \'Staceys\'', 'Black women are the backbone of the Democratic Party', 'signal boosting black female candidates for elected office', 'want to live in a kleptocratic plutocracy', 'jeffares' 'buddy carter', 'lisaringga', 'lisa ring', 'reason for Republicans to start panicking about 2018', 'Republican congressman from the state wants to withhold federal dollars to test these kits', 'withhold federal funding to test rape kits', '@repbuddycarter', 'Senate opponents of Trumpcare should be beaten', 'another round of anger over health care', 'fantasizes about beating up a female Republican Senator', 'snatch a knot']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Georgia 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://www.mvp.sos.ga.gov/MVP/mvp.do): April 23, 2018 \n\n"
            "[Primary Election](https://www.mvp.sos.ga.gov/MVP/mvp.do): May 22, 2018 \n\n"
            "[General Election Registration Deadline](https://www.mvp.sos.ga.gov/MVP/mvp.do): October 9, 2018 \n\n"
            "[General Election](https://www.mvp.sos.ga.gov/MVP/mvp.do): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()