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
            terms = ['kemp continues efforts to suppress', 'Studio to Pledge to Fight Georgia', 'Georgia Officials', 'kemp over vot', 'georgia \'exact match\'', 'georgia\'s \"exact match\"', 'Campaign in Georgia', 'marijuana in ga', 'abrams in georgia', 'stacy abrams', 'Georgia From Throwing Out Absentee Ballot', 'georgia from vot', 'georgia defends vot', 'georgia e-voting', 'representative spencer', 'ga06', 'ethan pham', 'Georgia Republican', 'deportation bus tour', 'blue-collar georgia tenants', 'stacey abrams', 'swastikas in a west Georgia field', 'law in georgia', 'georgia democrat', 'georgia congressman', 'georgia vote', ' ga. house', 'ga-12', 'casey cagle', 'trent nesmith', 'Gwinnett State House district', 'georgia legislat', 'georgia governor', 'georgia 6th', 'georgia lawmaker', 'Georgia Midterms', 'fran millar', 'Lawmakers propose switching Georgia', 'doug collins', 'rep. collins', 'rep collins', 'Reddest district in Georgia', 'representative collins', 'congressman collins', 'ga-9', 'ga-09', 'Georgia turns blue', 'kevin abel', 'approval ratings in Georgia', 'GA House of Representatives', 'Georgia\'s Election System', 'battle of the \'Staceys\'', 'jeffares' 'buddy carter', 'lisaringga', 'lisa ring', '@repbuddycarter']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Georgia 2020 Election \n\n"
            "[Primary Election Registration Deadline](https://registertovote.sos.ga.gov/GAOLVR/welcome.do#no-back-button): April 20, 2020 \n\n" 
            "[Primary Election](https://www.mvp.sos.ga.gov/MVP/mvp.do): May 19, 2020 \n\n"
            "[General Election Registration Deadline](https://registertovote.sos.ga.gov/GAOLVR/welcome.do#no-back-button): October 5, 2020 \n\n" 
            "[General Election](https://www.mvp.sos.ga.gov/MVP/mvp.do): November 3, 2020 \n\n")
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