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

local_subs = open("alabama.dat", "r")
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
            terms = ['elsie bodiford', '200 women on abortion', 'bernie in birmingham', 'Alabama sentences more people to death', 'alabama\'s strict abortion', 'alabama women worried', 'pro-forced-birth', 'alabama boycott', 'what christian sharia looks like', 'Robertson believes the anti-abortion laws are too extreme', 'abortion in alabama', ' al abortion ban', 'abortion is a constitutional right', 'bans in alabama', '3 grams of weed', 'voting is being suppressed in Alabama', 'Alabama 4th congressional dist', 'Voter registration numbers on the rise in Alabama', 'darwin brazier', 'Alabama \'Families Belong Together\'', 'sen. jones', 'dougjones', 'lee auman', 'mo brooks', 'alabama congressman', 'alabama elections chief', 'alabama state lege. seat', 'candidates in alabama', 'roy moore', 'alabama lawmaker', 'Etowah County sheriff', 'Alabama\'s 2018 elections', 'house seat in alabama', 'sue bell cobb', 'al-03', 'chris christie', 'bill passed by Alabama House', 'Alabama state House', 'jason childs', 'bradley byrne', 'Alabama violated federal law', 'Doug Jones', 'tommy battle', 'gerrymandered Alabama', 'Alabama\'s Secretary of State', 'Congressman Brooks town hall', 'al-gov', 'alabama governor', 'ala. gov', 'Alabama Secretary of State', 'John Merrill', 'Alabama election official']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        # No early voting
        text = ("Alabama 2020 Election \n\n"
            "[Primary Election Voter Registration Deadline](https://www.sos.alabama.gov/alabama-votes/voter/register-to-vote): February 15, 2020 \n\n"
            "[Primary Election](https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do): March 3, 2020 \n\n"
            "[General Election Voter Registration Deadline](https://www.sos.alabama.gov/alabama-votes/voter/register-to-vote): October 19, 2020 \n\n"
            "[General Election](https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do): November 3, 2020 \n\n")
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