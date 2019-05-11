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

local_subs = open("tennessee.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['1400 nashville teachers', 'office attempt to frame activist', 'could you buy a house in nashville', 'GRASSHOPPER LEARNING FROM MASTER GRIFTER', 'exploited sanitation workers', 'james mackler', 'lamar alexander', 'senate race in tennessee', 'rally in tennessee', 'thongnopnua', 'comstock on npr', 'tn politic', 'Pro-Trump Tennessee', 'Blue Wave hits Shelby County', 'nathan farnor', 'Pence to Visit Chattanooga', 'tn-sen', 'diane black', 'nashville pride', 'ICE Came for a Tennessee Town', 'pride of knoxville', 'knoxville straight pride', 'trump rally in nashville', 'corker and alexander', 'tennessee\'s candidate', 'trey palmedo', 'waffle house shooting', 'pro-trump tennessee', 'tennessee house', 'tn house', 'vanhuss', 'tn6', 'bill halted in tennessee', 'tn state Representative', 'memphis trees community', 'lee beaman', 'dawnbarlow', 'tennessee Republican', 'tn01', 'state Representative for tennessee', 'tennessee gop', 'oddie shoupe', 'Tennessee Heritage Protection Act', 'TN State Legislature', 'phil roe', 'Greenville local races', 'House Bill 2381', 'Tennessee bill', 'tennessee judge', 'Tennessee to legalize medical marijuana', 'TN Representative Candidate', 'tennessee lawmaker', 'john duncan', 'Tennessee House Republicans', 'corker kick back', 'Corker asks', 'corker kickback', 'corkerkickback', 'corker demands', 'CORker says', 'Senate in Tennessee', 'TN Democrats Vote', 'bredesen', 'kustoff', 'tennessee governor', 'tn gubernatorial', 'gov. of tn', 'tennessee gubernatorial candidate', 'governor haslam', 'randy boyd', 'kay white', 'tn governor', 'bill lee', 'beth harwell', 'karl dean', 'mae beavers', 'tennessee senat', 'bob corker', 'sen. corker', 'blackburn', 'corker\'s u.s. senate seat', 'replace corker', 'Corker fight', 'andy ogles', 'senator corker', 'Corkers seat', 'tn-6', 'tn-7', 'tn-07']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Tennessee 2020 Election \n\n"
            "[Register to Vote](https://ovr.govote.tn.gov/Registration/RegistrationDetails/BM) \n\n"
            "[General Election](http://web.go-vote-tn.elections.tn.gov/): November 3, 2020 \n\n")
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