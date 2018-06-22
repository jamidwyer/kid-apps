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

local_subs = open("oklahoma.dat", "r")
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
            terms = ['teach pay and weed', 'rogers county sheriff', 'on 788', '30 minute special hosted by Jessica Schambach', 'Oklahoma may vote to allow medical marijuana', 'gubernatorial race have on the marijuana vote', 't always show up to vote....', 'Medical Cannabis Conference and Expo coming to Oklahoma City', 'the marijuana question', 'Authors of medical marijuana measure', 'sq788', 'state question 788', 'sq 788', ' The Marijuana Question', 'Oklahoma Will Vote on Medical Marijuana in June', 'say yes to 788', 'Is this the year we legalize Medical Marijauna', 'Mother calls Fallin a', '72yo Woman Shot Dead as SWAT Raided Her Home To Arrest Her Son For Cannabis', 'Oklahomans support medical marijuana measure', 'Oklahoma Medical Marijuana Access Initiative']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Oklahoma 2018 Primary Election \n\n"
            "[Early Voting](https://www.ok.gov/elections/Early_Voting.html): June 21-23, 2018 \n\n"
            "[Primary Election Date](https://services.okelections.us/voterSearch.aspx): June 26, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        submission.reply(text)

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()