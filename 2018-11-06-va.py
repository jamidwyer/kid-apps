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
            terms = ['GOP operatives for Southside and Central VA', 'pat robertson', 't give a fuck about life.', 'election in virginia', 'Trump Says Kavanaugh Is a Good Man', 'legalize virginia', 'Loudoun Board of Supervisors', 'laura ingraham', 'shortchanging park rangers and postal carriers', 'virginia, republicans', 'virginia beach sheriff', 'strapped to chairs and had bags', 'party of white supremacy', 'kaine 49', 'kaine leads', 'monetize being a nazi', 'dan helmer', 'cockburn', 'cracking Nazi skulls', 'marijuana in virginia', 'va-07', '^(?!.*west virginia gop).*virginia gop.*$', 'heather heyer', 'the red hen', 'virginia beach city council', 'danica roem', 'pro-incest, pedophilia, and rape', 'unite the right', 'jason kessler', 'virginia Congressional Candidate', 'Congressional Candidate In Virginia', 'virginia senate', 'virginiapolitics', 'cynthia dunbar', 'richardbspencer', 'richard spencer', 'house bill 83', 'naomi wadler', 'gerrymandering in virginia', 'burgos', 'va-5', 'tim kaine', 'Va. House', 'corey stewart', 'rob wittman', 'scott taylor', 'rep. taylor', 'congressman taylor', 'rep taylor', 'Virginia Congressional Election', 'dave brat', 'rep. brat', 'congressman brat', 'rep brat', 'representative brat', 'goodlatte', 'House Judiciary chairman', 'House GOP leaders open probe into FBI', 'latest Republican patsy', 'Lawmakers grapple with warrantless wiretapping program', 'barbara comstock', 'rep. comstock', 'congresswoman comstock', 'rep comstock', 'representative comstock', 'va-10', 'comstock challenger', 'Dems think Trump can deliver suburbs to their party', 'Every Member of Congress Who Took Money From the NRA and Tweeted', 'who in Congress is getting money from the NRA', 'Obamacare repeal effort into doubt', 'tom hicks']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Virginia 2018 General Election \n\n"
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