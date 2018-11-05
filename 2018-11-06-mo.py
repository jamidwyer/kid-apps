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

local_subs = open("missouri.dat", "r")
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
            terms = ['missouri senate', 'poll shows amendment 2', 'st. louis abortion', 'Red State Victory for Voting Rights', 'yes on amendment 2', 'Missouri industries feel the pain of tariffs', 'hitler was right', 'billy long', 'missouri house primary', 'st. louis prosecutor', 'ferguson reformer', 'missouri election', 'ferguson prosecutor', 'missouri gop', 'wesley bell', 'bob mcculloch', 'right to work in missouri', 'missouri state primary', 'missouri vote', 'missouri 2018 primary', 'j.p johnson', 'mo-7', 'st. louis minimum wage', 'missouri congress', 'michael brown was shot', 'curtiswylde', 'greitens', 'lauren arthur', 'missouripolitics', 'ferguson city council', 'missouri house moves', 'kc voters', 'osmack', 'missouri bill', 'new approach missouri', 'Missouri lawmaker', 'austin petersen', 'Missouri Medical Marijuana Campaign', 'josh hawley', 'courtland sykes', 'US Senate in Missouri', 'MO GOP Senate Nomination', 'snake-filled heads', 'career obsessed banshees', 'Missouri pregnancy mortality', 'sam graves', 'Blaine Luetkemeyer', 'kathy ellis', 'mccaskill', 'top 10 Senate races of 2018', 'ann wagner', 'mo-2', 'jenna marie bourgeois', 'hartzler', 'mo-4', 'How Missouri previewed Democrats']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Missouri 2018 Election \n\n"
            "[General Election](https://voteroutreach.sos.mo.gov/PRD/VoterOutreach/VOSearch.aspx): November 6, 2018 \n\n\n\n"

            "[Check Your Voter Registration](https://s1.sos.mo.gov/elections/voterlookup/) \n\n")
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