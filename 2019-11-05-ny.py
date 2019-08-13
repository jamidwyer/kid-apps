#!/usr/bin/python
# coding: utf-8

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

local_subs = open("newyork.dat", "r")
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
            terms = ['murdering jeffrey epstein', 'fbi agents are livid', 'officials say epstein', 'epstein conspiracy', 'epstein found dead', 'death of jeffrey epstein', 'epstein suicide', 'killed for having information that would implicate top government officials', 'epstein death', 'cop walks up to crowd and punches 70 year old', 'AOC promotes local elections', 'NYPD officer', 'eric garner', 'nypd used deadly force', 'rally for Cabán', 'latina backed by aoc', 's policy on Immigration Status.', 'epstein died', 'tiffany caban', 'DA candidate Cab', 'new york city is creating jobs', 'Protestors in NYC', 'No Blind People are Going to Live in Trump Tower', 'new york chapter of the proud boys', 'bronx dsa', 'activists in new york', 'taxi driver in debt', 'new york\'s housing crisis', 'marijuana charges in new york', 'new york city dsa', 'Billionaires Row']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post

        text = ("New York 2019 Election \n\n"
            "[General Election Registration Deadline](https://voterlookup.elections.state.ny.us/votersearch.aspx): October 11, 2019 \n\n"
            "[General Election](https://voterlookup.elections.state.ny.us/votersearch.aspx): November 5, 2019")
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