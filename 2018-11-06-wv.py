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

local_subs = open("wv.dat", "r")
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
            terms = ['rally in west virginia', 'west virginia is bleeding out', 'West Virginia District Trump Won', 'W.Va. Supreme Court', 'West Virginia Supreme Court', 'WV Supreme Court Justice', 'west virginia strike', 'blankenship wages war on gop', 'west virginia republican', 'west virginia primary', 'ex-con coal baron', 'wv attorney General', 'senate bid in west virginia', 'Revolt in West Virginia', 'kendra fershee', 'worst state economies in the US', 'democrats in coal country', 'first deregulated bridge', 'wv teachers walkout', 'west virginia teacher strike', 'w.va lawmaker', 'west virginia teachers\'', 'West Virginia politician', 'Thousands rally to defend teachers in Charleston, West Virginia', 'Trump Can\'t Save Coal', 'lissa lucas', 'Applause for Candidate Who Called Out Big Oil Donors', 'west virginia legislat', 'West Virginia was dragged out of the capitol', 'WV House Chambers', 'I would LOVE to see TYT interview this woman', 'West Virginia Democratic Candidate', 'dragged out of West Virginia house hearing listing oil and gas contributions', 'kicked out of a town hall in west Virginia for simply listing corporate donors', 'wv-sen', 'West Virginia Senate GOP Primary', 'Trump is on his way to West Virginia', 'manchin', 'paulajean2018', 'West Virginia started drug testing welfare recipients', 'Richard Ojeda', 'Appalachia poor, sick, and stuck on coal', 'Dire Impressions From His Report On Poverty In U.S.', 'dead because of this coal baron', 'CEO who oversaw a mine where 29 workers were killed']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        # Early voting over
        text = ("West Virginia 2018 Election \n\n"
            "[General Election](https://services.sos.wv.gov/Elections/Voter/FindMyPollingPlace): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our post id back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()