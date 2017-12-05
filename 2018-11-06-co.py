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

local_subs = open("colorado.dat", "r")
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
            terms = ['Colorado becomes first in the nation to secure election system', 'Colorado CHIP notice letters sent out', 'mike coffman', 'co-06', 'co-6', 'rep. coffman', 'rep coffman', 'representative coffman', 'congressman coffman']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Colorado 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://www.sos.state.co.us/voter/pages/pub/olvr/verifyNewVoter.xhtml): June 18, 2018 \n\n"
            "[Primary Election Date](https://www.sos.state.co.us/pubs/elections/vote/VoterHome.html): June 26, 2018 \n\n"
            "[General Election Registration Deadline](https://www.sos.state.co.us/voter/pages/pub/olvr/verifyNewVoter.xhtml): October 29, 2018 \n\n"
            "[General Election](https://www.sos.state.co.us/pubs/elections/vote/VoterHome.html): November 6, 2018 \n\n")
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