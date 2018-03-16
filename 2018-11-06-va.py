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

local_subs = open("virginia.dat", "r")
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
            terms = ['fake news in black churches', 'alex jones is a menace to society', 'gerrymandering in virginia', 'Mary checking visa status of prospective students', 'fredy burgos', 'va-5', 'tim kaine', 'Va. House seat', 'corey stewart', 'rob wittman', 'scott taylor', 'rep. taylor', 'congressman taylor', 'rep taylor', 'Virginia Congressional Election', 'dave brat', 'rep. brat', 'congressman brat', 'rep brat', 'representative brat', 'Conservatives drop demands for bigger spending cuts to get to tax reform', 'GOP Congressmen Call For Mueller Hearings', 'Republicans in Congress Cheered', 'Freedom Caucus endorses GOP tax plan', 'goodlatte', 'wave of Republicans leaving Congress', 'House Judiciary chairman', 'U.S. House panels open probe into Justice Department', 'House GOP leaders open probe into FBI', 'latest Republican patsy', 'Lawmakers grapple with warrantless wiretapping program', 'barbara comstock', 'rep. comstock', 'congresswoman comstock', 'rep comstock', 'representative comstock', 'va-10', 'comstock challenger', 'Dems think Trump can deliver suburbs to their party', 'Every Member of Congress Who Took Money From the NRA and Tweeted', 'who in Congress is getting money from the NRA', 'Obamacare repeal effort into doubt', 'tom hicks']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Virginia 2018 General Election \n\n"
            "[Primary Election Registration Deadline](https://vote.elections.virginia.gov/Registration/Eligibility): May 21, 2018 \n\n"
            "[Primary Election](http://www.elections.virginia.gov/voter-outreach/where-to-vote.html): June 12, 2018 \n\n"
            "[General Election Registration Deadline](https://vote.elections.virginia.gov/Registration/Eligibility): October 15, 2018 \n\n"
            "[General Election](http://www.elections.virginia.gov/voter-outreach/where-to-vote.html): November 6, 2018 \n\n")
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