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
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['luther strange', 'al-sen', 'alabama senate primaries', 'Roy Moore for Senate? I Think Not', 'Strange Has Alabama Conservatives Reeling', 'alabama senate poll', 'sen. strange', 'senator strange', 'the perfect alabama candidate', 'special election in alabama', 'alabama special election', 'Alabama Senate candidate', 'alabama senate race', 'Senate Seat in Alabama', 'How Roy Moore Won Alabama', 'Alabama Senate: Special Election', 'trump voters in alabama', 'back down from questioning Obama', 'alabama gop senate race', '\'Maybe Putin is right\': Republican Senate frontrunner on Russian leader', 'Trump-Backed Candidate in Alabama', 'no strange', 'alabama sen. candidate', 'alabama senate race']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register to Vote &#9733;&#9733;&#9733;](https://www.alabamainteractive.org/sos/voter_registration/voterRegistrationWelcome.action) \n\n"
            "[**Doug Jones**](http://dougjonesforsenate.com/) is running to represent Alabama in the U.S. Senate. \n\n "
            "[Donate](https://secure.actblue.com/donate/homepage-donate) | "
            "[Facebook](https://www.facebook.com/dougjonessenate) \n\n "

            "Jones supports universal health care, public schools, living wages, protecting Medicare, equal pay for equal work, and renewable energy.  \n\n "

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")
        print("Bot replying to : ", submission.title)
        submission.reply(text)

        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

text_file.close()
local_subs.close()