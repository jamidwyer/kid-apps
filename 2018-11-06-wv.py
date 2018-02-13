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
            terms = ['Candidate KICKED OUT For Reading Politicians', 'Police officer fired for not shooting black suspect', 'West Virginia Woman Dragged Out of Capitol', 'West Virginia was dragged out of the capitol', 'WV House Chambers', 'I would LOVE to see TYT interview this woman', 'West Virginia Democratic Candidate', 'dragged out of West Virginia house hearing listing oil and gas contributions', 'kicked out of a town hall in west Virginia for simply listing corporate donors', 'wv-sen', 'West Virginia Senate GOP Primary', 'Trump is on his way to West Virginia', 'manchin', 'paulajean2018', 'West Virginia started drug testing welfare recipients', 'Richard Ojeda', 'Appalachia poor, sick, and stuck on coal', 'Dire Impressions From His Report On Poverty In U.S.', 'dead because of this coal baron', 'CEO who oversaw a mine where 29 workers were killed']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("West Virginia 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://ovr.sos.wv.gov/Register/Landing#Qualifications): April 10, 2018 \n\n"
            "[Primary Election Date](https://services.sos.wv.gov/Elections/Voter/FindMyPollingPlace): May 8, 2018 \n\n"
            "[General Election Registration Deadline](https://ovr.sos.wv.gov/Register/Landing#Qualifications): October 16, 2018 \n\n"
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