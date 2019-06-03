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

local_subs = open("louisiana.dat", "r")
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
            terms = ['keep marriage legal for 15, 16', 'protest louisiana', 'Very sad day to be a Louisianian', 'the current state of American liberalism', 'nungesser', 'us children are living below the poverty line', 'louisiana decided to curb mass incarceration', 'louisiana fall elections', 'louisiana governor']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Louisiana 2019 Election \n\n"
            "[Primary Registration Deadline](https://voterportal.sos.la.gov/VoterRegistration): September 21, 2019 \n\n"
            "[Primary Early Voting](https://www.sos.la.gov/ElectionsAndVoting/Vote/VoteEarly/Pages/default.aspx): September 28 - October 5, 2019 \n\n"
            "[Primary Election](https://voterportal.sos.la.gov/Home/VoterLogin): October 12, 2019 \n\n"
            "[General Voter Registration Deadline](https://voterportal.sos.la.gov/VoterRegistration): October 26, 2019 \n\n"
            "[Early Voting](https://www.sos.la.gov/ElectionsAndVoting/Vote/VoteEarly/Pages/default.aspx): November 2 - November 9, 2019 \n\n"
            "[General Election](https://voterportal.sos.la.gov/Home/VoterLogin): November 16, 2019")
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