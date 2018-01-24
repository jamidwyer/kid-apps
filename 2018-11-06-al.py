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
            terms = ['Alabama ladies and gentlemen, democracy', 'Alabama state House votes to end special elections', 's March in Huntsville', '49 Alabama Sheriffs Sued', 'Alabama Republicans seek to censure GOP Senator Shelby', 'Tiny lives will be lost for the GOP\'s greed.', 'jason childs', 'Alabama officials pray to God before certifying Doug Jones', 'bradley byrne', 'Alabama may have violated federal law', 'Alabama violated federal law', 'Doug Jones would have carried 3 Cong. districts', 'ALABAMA: Trump Job Approval', 'Doug Jones Would Have Won by Tens of Thousands More', 'tommy battle', 'how gerrymandered Alabama is', 'Republicans At Roy Moore\'s Party', 'every single county shifted toward the Democrats', '2017 Alabamian election results', 'Alabama is a red state', 'Black voters in Alabama are getting blocked from voting at polls', 'Alabama\'s Secretary of State', 'poverty in rural Alabama', 'Alabama worst poverty in the world', 'Alabama Has The Worst Poverty', 'U.N. officials touring rural Alabama', 'UN poverty official touring Alabama', '\"poverty official\" touring Alabama', 'United Nations official visiting Alabama to investigate', 'Congressman Brooks town hall', 'al-gov', 'alabama governor', 'ala. gov', 'too poor to vote', 'Alabama Secretary of State', 'John Merrill', 'top election official learn from monitoring Russian election', 'Alabama election officials remain confused']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Alabama 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://www.alabamainteractive.org/sos/voter_registration/voterRegistrationWelcome.action): May 21, 2018 \n\n"
            "[Primary Election](https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do): June 5, 2018 \n\n"
            "[General Election](https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do): November 6, 2018 \n\n")
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