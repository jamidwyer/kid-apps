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

local_subs = open("pennsylvania.dat", "r")
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
            terms = ['Women Run in Pennsylvania', 'anxious whites feel left behind', 'philly teens to florida teens', 'nick miccarelli', 'revolt in trump country', 'saccone', 'conor lamb', 'blue wave just got 10 feet taller', 'prepare for a massive midterm wave', 'pa.\'s redistricting', 'Pittsubrgh anti-abortion health-care centers', 'christina hartman', 'Rick Santorum', 'rep costello', 'congressman costello', 'representative costello', 'rep. costello', 'New Congressional Map in Pennsylvania', 'Pennsylvania\'s Gerrymandered Congressional Map', 'Daryl Metcalfe', 'pennsylvania voters', 'Trump defending gerrymandering', 'PA\'s new congressional map', 'Court-Drawn Map in Pennsylvania', 'New map for Pennsylvania', 'Pennsylvania Supreme Court draw', 'Pennsylvania House District', 'Court-Drawn Map in Pa.', 'hal english', 'pennsylvania voting map', 'new Pennsylvania map', 'pa. congressional map', 'turzai', 'Pennsylvania congressional map', 'Pennsylvania will require voting machines', 'Pennsylvania to require voting machines', 'Pennsylvania Republican launches effort', 'Pennsylvania GOP lawmaker', 'Pennsylvania congressional redistricting', 'Pennsylvania Republicans Delay', 'pa redistricting', 'Recreational Pot For Pennsylvania', 'Pennsylvania GOP\'s leading Senate candidate', 'Pa. governor', 'lou barletta', 'legalizing marijuana in PA', 'Vincent Hughes', 'PA\'s 16th Congressional', 'Pennsylvania coal mine closes', 'stable genius act', 'Pennsylvania redistricting', 'pennsylvania state senate', 'smucker', 'pa-16', 'joe billie', 'pa-7', 'pa-07', '^(?!.*john meehan).*meehan.*$', 'pennsylvania gerrymandering', 'ryan costello', 'Democrats back military veterans as candidates']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Pennsylvania 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://www.pavoterservices.pa.gov/Pages/VoterRegistrationApplication.aspx): April 16, 2018 \n\n"
            "[Primary Election](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx): May 15, 2018 \n\n"
            "[General Election Registration Deadline](https://www.pavoterservices.pa.gov/Pages/VoterRegistrationApplication.aspx): October 7, 2018 \n\n"
            "[General Election](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx): November 6, 2018 \n\n")
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