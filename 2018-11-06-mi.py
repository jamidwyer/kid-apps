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

local_subs = open("michigan.dat", "r")
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
            terms = ['political fliers on detroit', 'devos family', 'Pence event provokes backlash', '4 states could legalize', 'candidates in michigan', 'ballot as Proposal 1', 'clean water for michigan', 'votes in michigan', 'mi11', 'tlaib', 'vote in michigan', 'michigan primary', 'wimmer', 'tom mair', 'michigan redistricting', 'gerrymandered michigan', 'fix flint', 'water in flint', 'Flint, Michigan', 'niles niemuth', 'upton stands against', 'Michigan Department of Civil Rights', 'gubernatorial candidate in Michigan', 'ballot in michigan', 'legalization in michigan', 'eponine garrod', 'state house in lansing', 'detroit dsa', 'governor in michigan', 'dana nessel', 'edgar prince', 'poppy sias', 'bobby holley', 'Michigan House votes', 'gerrymandering in Michigan', 'Green Party of Michigan', 'Mich. ballot campaign', 'Rep. Dingell', 'abdulelsayed', 'brenda lawrence', 'Michigan Senate candidate', 'saari', 'schuette', 'Flint drinks poison', 'Cop Caught on Video Smashing Handcuffed Woman', 'ICE deports Jorge Garcia', '️solar power installed on michigan', 'Michigan ballot', 'el-sayed', 'Will Michigan Legalize Marijuana', 'Bannon v Trump', 'Year Michigan Legalizes Marijuana', 'record number of women are eyeing a run for governor', 'The year ahead in pot', 'Nothing in Moderation', 'HENRY YANEZ', 'gretchen whitmer', 'Michigan, these are your Members of Congress', 'Tim Kelly', 'Michigan still a blue state', 'Joe Schwarz', 'Political Issues in Michigan', 'sandy levin', 'jack bergman', 'marijuana legalization in Michigan', 'fred upton', 'mi-06', 'mi-6', 'michigan\'s 6th District', 'rep. upton', 'rep upton', 'representative upton', 'congressman upton', 'benac', '^(?!.*trotte).*trott.*$', 'Mercurial Trump Rattles Republican Party Ahead of Midterms', '2018 as 3rd House Republican Says He', 'Michigan Republican congressman won\'t seek re-election', 'Congressional GOP Retirement Surge', 'mike bishop', 'rep. bishop', 'rep bishop', 'representative bishop', 'congressman bishop', 'mi-08', 'mi-8', 'Michigan\'s 8th District', 'prohibit protecting the ocean as national park, place extreme restrictions on national parks', 'rick snyder', 'governor snyder', 'gov snyder', 'gov. snyder', 'michigan governor', 'governor of michigan', 'michigan\'s governor', 'stabenow', 'kid rock', 'john james', 'Robert Ritchie', '^(?!.*yamashiro).*amash.*$', 'mi-03', 'mi-3', 'michigan\'s 3rd District']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Michigan 2018 Election \n\n"
            "[General Election](https://webapps.sos.state.mi.us/MVIC/votersearch.aspx): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")


for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()