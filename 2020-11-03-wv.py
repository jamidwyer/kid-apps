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
            terms = ['sen. mike maroney', 'evangelicals chafe at trump', 'racist rally, some christians', 'dea tracked every opioid pill', 'swearengin', 'west virginia expands medical marijuana', 'west virginia governor', 'warren in heart of maga country', 'knock down the house', 'knockdownthehouse', 'basic income mean for appalachia', 'a democrat thing\"', 'rally in west virginia', 'West Virginia District', 'W.Va. Supreme Court', 'West Virginia Supreme Court', 'WV Supreme Court', 'west virginia strike', 'west virginia republican', 'west virginia primary', 'ex-con coal baron', 'wv attorney General', 'senate bid in west virginia', 'Revolt in West Virginia', 'kendra fershee', 'worst state economies in the US', 'democrats in coal country', 'first deregulated bridge', 'wv teachers walkout', 'west virginia teacher strike', 'w.va lawmaker', 'west virginia teachers\'', 'West Virginia politic', 'Trump Can\'t Save Coal', 'lissa lucas', 'west virginia legislat', 'WV House Chambers', 'West Virginia Democratic Candidate', 'West Virginia house hearing', 'town hall in west Virginia', 'wv-sen', 'West Virginia Senate GOP Primary', 'Trump is on his way to West Virginia', 'manchin', 'Richard Ojeda', 'Appalachia poor']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("West Virginia 2020 Election \n\n"
            "[Primary Election Voter Registration](https://ovr.sos.wv.gov/Register/Landing#Qualifications): April 21, 2020 \n\n"
            "[Primary Election](https://services.sos.wv.gov/Elections/Voter/FindMyPollingPlace): May 12, 2020 \n\n"
            "[General Election Voter Registration](https://ovr.sos.wv.gov/Register/Landing#Qualifications): October 13, 2020 \n\n"
            "[General Election](https://services.sos.wv.gov/Elections/Voter/FindMyPollingPlace): November 3, 2020 \n\n")
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