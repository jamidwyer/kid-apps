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

local_subs = open("ri.dat", "r")
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
            terms = ['wyatt detention center', 'ice agent runs over protestors', 'truck into ice protestors', 'protestors in rhode island', 'ri to lobby', 'equality act', 'rhode island bill', 'RI State Senator']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Rhode Island 2020 Election \n\n"
            "[Presidential Preference Primary Voter Registration Deadline](https://vote.sos.ri.gov/): March 29, 2020 \n\n"
            "[Presidential Preference Primary Election](https://vote.sos.ri.gov/#general-search): April 28, 2020 \n\n"
            "[Primary Election Voter Registration Deadline](https://vote.sos.ri.gov/): August 17, 2020 \n\n"
            "[Primary Election](https://vote.sos.ri.gov/#general-search): September 15, 2020 \n\n"
            "[General Election Voter Registration Deadline](https://vote.sos.ri.gov/): October 4, 2020 \n\n"
            "[General Election](https://vote.sos.ri.gov/#general-search): November 3, 2020 \n\n")
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