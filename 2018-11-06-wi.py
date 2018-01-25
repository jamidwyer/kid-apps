# coding: utf-8
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

local_subs = open("wisconsin.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Wisconsin Republicans Abruptly Decide To Oust Top State Elections', 'gop rigs elections', 'How Trump is Destroying the GOP', 'Kochs made huge donations to Republicans shortly after tax plan passed', 'Republicans control the Senate, House and White House', 'Foxconn cost to public', 'House Majority Leader', 'Wisconsin Senate Committee', 'neverryan', 'tammy baldwin', 'entitlement reform', 'matt flynn', 'Sensenbrenner', 'randy bryce', 'scott walker', 'governor walker', 'wisconsin governor', 'wi governor\'s', 'Wisconsin gubernatorial candidate', 'Wisconsin democratic governor candidate', 'Wisconsin Democratic candidates for governor', 'Wisconsin\'s partisan gerrymander', 'Deterred Voters in Wisconsin', 'Wisconsin Strict ID Law', 'Republican Governors Association', 'Republican Gov Association', 'paul ryan', 'rep. ryan', 'congressman ryan', 'rep ryan', 'speaker ryan', '@speakerryan', 'IronStache', 'Republican tax scam', 'Middle-Class Tax Hike', 'Wisconsin\'s First Congressional District', 'brad schimel']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Wisconsin 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://myvote.wi.gov/en-us/registertovote): August 14, 2018 \n\n"
            "[Primary Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): August 14, 2018 \n\n"
            "[General Election Registration Deadline](https://myvote.wi.gov/en-us/registertovote): November 6, 2018 \n\n"
            "[General Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): November 6, 2018 \n\n")
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