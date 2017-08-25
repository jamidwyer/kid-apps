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

local_subs = open("idaho.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=500):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['zollinger', 'Republican promotes theory that Obama plotted Charlottesville neo-Nazi rally', 'Obama staged Charlottesville riots', 'Idaho state rep shares conspiracy theory accusing George Soros of staging Charlottesville', 'Idaho GOP politician shares conspiracy theory accusing Obama of staging Charlottesville', 'Idaho state rep shares conspiracy theory accusing Obama of staging Charlottesville']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.idahovotes.gov/VoterReg/voter_registration.pdf) \n\n"
        "Bryan Zollinger is currently unopposed in 2018. Know someone who should [run](https://www.runforoffice.org/elected_offices/32566-state-representative-id-33-seat-2/interest_form)? \n\n"

        "[Map of Idaho State House District 33](https://www.google.com/maps/d/u/2/viewer?mid=1DWB6vryl4ZZTyplk4s_Iiwt8ih0&hl=en_US&authuser=2&ll=43.48927161166976%2C-112.03849150000002&z=12) \n\n"

        "^(I'm a bot and I'm learning. Let me know how I can do better.)")
        submission.reply(text)
        print("Bot replying to : ", submission.title)

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