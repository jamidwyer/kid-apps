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

local_subs = open("florida.dat", "r")
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
            terms = ['lehtinen', 'fl-27']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://dos.myflorida.com/elections/for-voters/voter-registration/register-to-vote-or-update-your-information/) \n\n"
        "[**Michael Hepburn**](http://www.michaelhepburn.com/) is running against Ileana Ros-Lehtinen. \n\n"
        "[Donate](https://secure.actblue.com/contribute/page/hepburnforcongress) | "
        "[Facebook](https://www.facebook.com/VoteHepburn/) | "
        "[Twitter](https://twitter.com/VOTEHEPBURN) \n\n"
        "Hepburn supports universal health care, a living wage, college affordability, renewable energy, and campaign finance reform. \n\n\n "

        "Map of Florida District 27: https://www.govtrack.us/congress/members/FL/27 \n\n"

        "^(I'm a bot and I'm learning. Let me know how I can do better.)")
        submission.reply(text)

        print("Bot replying to : ", submission.title)
        submission.reply(text)

        # Store the current id into our list
        posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

text_file.close()
local_subs.close()