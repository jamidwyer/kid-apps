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
            terms = ['easier to fire women who act', 'garypeters', 'may god ruin trump', 'coverage of his racism', 'Trump Won Because Of Lower Democratic Turnout', 'Trump supporters deported back to Iraq', 'Jimmy Aldaoud', 'detroit ahead of the second debate', 'insulin saves my life', '3 republicans drop out', 'MI, MN and WI', 'second democratic debate', 'detroit police board', 'inslee opposes pipeline plan', 'debate in detroit', 'unflattering numbers leak', 'DNC Army That Could Soon Descend', 'flint officials', 'what happened in flint', '12 points in michigan', 'Michigan Doctor Accused of Overprescribing', 'michigan jail', 'Trump Would Have Lost Election Without Russian Help', 'trump in PA, WI and MI', 'michigan lawmak', 'participating in their lives', 'dems in michigan', 'michigan democrat', 'michigan absentee', 'political fliers on detroit', 'devos family', 'candidates in michigan', 'clean water for michigan', 'votes in michigan', 'mi11', 'tlaib', 'vote in michigan', 'michigan primary', 'tom mair', 'michigan redistricting', 'gerrymandered michigan', 'fix flint', 'water in flint', 'Flint, Michigan', 'niles niemuth', 'upton stands against', 'Michigan Department of Civil Rights', 'gubernatorial candidate in Michigan', 'ballot in michigan', 'legalization in michigan', 'eponine garrod', 'state house in lansing', 'detroit dsa', 'governor in michigan', 'dana nessel', 'edgar prince', 'poppy sias', 'bobby holley', 'Michigan House votes', 'gerrymandering in Michigan', 'Green Party of Michigan', 'Mich. ballot campaign', 'Rep. Dingell', 'abdulelsayed', 'brenda lawrence', 'Michigan Senate candidate', 'saari', 'schuette', 'Flint drinks poison', 'Michigan ballot', 'el-sayed', 'Michigan Legalize Marijuana', 'Michigan Legalizes Marijuana', 'HENRY YANEZ', 'gretchen whitmer', 'Tim Kelly', 'Michigan still a blue state', 'Joe Schwarz', 'Political Issues in Michigan', 'sandy levin', 'jack bergman', 'marijuana legalization in Michigan', 'fred upton', 'mi-06', 'mi-6', 'michigan\'s 6th District', 'rep. upton', 'rep upton', 'representative upton', 'congressman upton', 'benac', '^(?!.*trotte).*trott.*$', 'michigan congress', 'Michigan Republican congressman', 'mike bishop', 'rep. bishop', 'rep bishop', 'representative bishop', 'congressman bishop', 'mi-08', 'mi-8', 'Michigan\'s 8th District', 'rick snyder', 'governor snyder', 'gov snyder', 'gov. snyder', 'michigan governor', 'governor of michigan', 'michigan\'s governor', 'stabenow', 'john james', 'Robert Ritchie', '^(?!.*yamashiro).*amash.*$', 'mi-03', 'mi-3', 'michigan\'s 3rd District']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Michigan 2020 Election \n\n"
            "[Register to Vote](https://www.michigan.gov/documents/MIVoterRegistration_97046_7.pdf) \n\n"
            "[Primary Election](https://www.michigan.gov/sos/0,4670,7-127-1633_8716_8728-21037--,00.html): March 10, 2020 \n\n"
            "[General Election](https://www.michigan.gov/sos/0,4670,7-127-1633_8716_8728-21037--,00.html): November 3, 2020 \n\n")
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